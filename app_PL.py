import json
import uuid
from tkinter import *
from datetime import datetime

class HotelAppPL:
    def __init__(self, root):
        self.root = root
        self.fajl = "foglalasok.json"
        self.felulet()
        self.frissit_ido()

    def felulet(self):
        frame_felso = Frame(self.root)
        frame_felso.pack(pady=5)

        Label(frame_felso, text="Vendég neve:").grid(row=0, column=0, sticky=W)
        self.name_entry = Entry(frame_felso, width=25)
        self.name_entry.grid(row=0, column=1, sticky=W)

        Label(frame_felso, text="Érkezés (ÉÉÉÉ-HH-NN):").grid(row=1, column=0, sticky=W)
        self.checkin_entry = Entry(frame_felso, width=15)
        self.checkin_entry.grid(row=1, column=1, sticky=W)
        self.checkin_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

        Label(frame_felso, text="Távozás (ÉÉÉÉ-HH-NN):").grid(row=2, column=0, sticky=W)
        self.checkout_entry = Entry(frame_felso, width=15)
        self.checkout_entry.grid(row=2, column=1, sticky=W)
        self.checkout_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

        Label(frame_felso, text="Éjszakánkénti ár (Ft):").grid(row=3, column=0, sticky=W)
        self.rate_entry = Entry(frame_felso, width=10)
        self.rate_entry.grid(row=3, column=1, sticky=W)
        self.rate_entry.insert(0, "20000")

        frame_gomb = Frame(self.root)
        frame_gomb.pack(pady=5)

        Button(frame_gomb, text="Foglalás mentése", command=self.mentes_PL, width=18).grid(row=0, column=0, padx=5)
        Button(frame_gomb, text="Foglalások listázása", command=self.listaz_PL, width=18).grid(row=0, column=1, padx=5)
        Button(frame_gomb, text="Foglalás törlése ID alapján", command=self.torles_PL, width=24).grid(row=0, column=2, padx=5)

        frame_id = Frame(self.root)
        frame_id.pack(pady=5)

        Label(frame_id, text="Törlendő foglalás ID:").grid(row=0, column=0, sticky=W)
        self.id_entry = Entry(frame_id, width=40)
        self.id_entry.grid(row=0, column=1, sticky=W)

        self.ido_label = Label(self.root, text="", font=("Arial", 10))
        self.ido_label.pack()

        self.output = Text(self.root, height=15, width=90)
        self.output.pack(pady=5)

    def frissit_ido(self):
        most = datetime.now()
        self.ido_label.config(text="Jelenlegi idő: " + most.strftime("%Y-%m-%d %H:%M:%S"))
        self.root.after(1000, self.frissit_ido)

    def mentes_PL(self):
        nev = self.name_entry.get().strip()
        erkezes_szoveg = self.checkin_entry.get().strip()
        tavozas_szoveg = self.checkout_entry.get().strip()

        if not nev:
            self.output.insert(END, "Hiányzó név.\n")
            return

        try:
            erkezes = datetime.strptime(erkezes_szoveg, "%Y-%m-%d")
            tavozas = datetime.strptime(tavozas_szoveg, "%Y-%m-%d")
        except ValueError:
            self.output.insert(END, "Hibás dátumformátum. Használd: ÉÉÉÉ-HH-NN.\n")
            return

        if tavozas <= erkezes:
            self.output.insert(END, "A távozás dátumának későbbinek kell lennie, mint az érkezésnek.\n")
            return

        try:
            ar = int(self.rate_entry.get())
        except ValueError:
            self.output.insert(END, "Hibás ár.\n")
            return

        napok = (tavozas - erkezes).days
        osszeg = napok * ar

        foglalas = {
            "id": str(uuid.uuid4()),
            "nev": nev,
            "erkezes": erkezes.strftime("%Y-%m-%d"),
            "tavozas": tavozas.strftime("%Y-%m-%d"),
            "napok": napok,
            "ar": ar,
            "osszeg": osszeg
        }

        adatok = self.betolt_adatok()
        adatok.append(foglalas)
        self.ment_adatok(adatok)

        self.output.insert(END, f"Mentve: {foglalas['nev']} | ID: {foglalas['id']} | {napok} éj | {osszeg} Ft\n")

    def betolt_adatok(self):
        try:
            with open(self.fajl, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def ment_adatok(self, adatok):
        with open(self.fajl, "w", encoding="utf-8") as f:
            json.dump(adatok, f, indent=2, ensure_ascii=False)

    def listaz_PL(self):
        self.output.delete(1.0, END)
        adatok = self.betolt_adatok()
        if not adatok:
            self.output.insert(END, "Nincs még foglalás.\n")
        else:
            for foglalas in adatok:
                sor = (
                    f"{foglalas['id']} | "
                    f"{foglalas['nev']} | "
                    f"{foglalas['erkezes']} → {foglalas['tavozas']} | "
                    f"{foglalas['napok']} éj | "
                    f"{foglalas['osszeg']} Ft\n"
                )
                self.output.insert(END, sor)

    def torles_PL(self):
        torlendo = self.id_entry.get().strip()
        if not torlendo:
            self.output.insert(END, "Adj meg egy ID-t a törléshez.\n")
            return

        adatok = self.betolt_adatok()
        uj_lista = [f for f in adatok if f["id"] != torlendo]
        if len(uj_lista) == len(adatok):
            self.output.insert(END, "Nem található ilyen ID.\n")
        else:
            self.ment_adatok(uj_lista)
            self.output.insert(END, "Foglalás törölve.\n")
