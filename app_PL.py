import json
from tkinter import *
from datetime import datetime

class HotelAppPL:
    def __init__(self, root):
        self.root = root
        self.guests = []
        self.setup_ui()

    def setup_ui(self):
        Label(self.root, text="Vendég neve:").pack()
        self.name_entry = Entry(self.root)
        self.name_entry.pack()

        Label(self.root, text="Érkezés (ÉÉÉÉ-HH-NN):").pack()
        self.checkin_entry = Entry(self.root)
        self.checkin_entry.pack()

        Label(self.root, text="Távozás (ÉÉÉÉ-HH-NN):").pack()
        self.checkout_entry = Entry(self.root)
        self.checkout_entry.pack()

        Button(self.root, text="Foglalás mentése", command=self.mentes_PL).pack(pady=10)
        Button(self.root, text="Foglalások listázása", command=self.listaz_PL).pack(pady=10)

        self.output = Text(self.root, height=10, width=50)
        self.output.pack()

    def mentes_PL(self):
        adat = {
            "nev": self.name_entry.get(),
            "erkezes": self.checkin_entry.get(),
            "tavozas": self.checkout_entry.get()
        }

        try:
            with open("foglalasok.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(adat)
        with open("foglalasok.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        self.output.insert(END, f"Mentve: {adat['nev']}\n")

    def listaz_PL(self):
        self.output.delete(1.0, END)
        try:
            with open("foglalasok.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            for item in data:
                self.output.insert(END, f"{item['nev']} – {item['erkezes']} → {item['tavozas']}\n")
        except FileNotFoundError:
            self.output.insert(END, "Nincs még foglalás.\n")
