# Hotel Booking App

## Hallgató
Pletser Lilla - WIUDUC

## Feladat leírása
Egyszerű hotel foglaláskezelő alkalmazás Pythonban, grafikus Tkinter felülettel.  
Vendégek felvétele, foglalások mentése, listázása és törlése azonosító alapján.  
A foglalások JSON fájlban kerülnek eltárolásra.

## Program felépítése
- Indítás: `main.py`
- Alapablak: `root`
- Programnév: `app` (példányosított objektum: `app = HotelAppPL(root)`)

## Modulok

### Tanult modulok
- `tkinter` - grafikus felület, eseménykezelés
- `json` - adatok mentése és betöltése fájlból

### Bemutatandó modul
  - `datetime`
  - `datetime.now()` - aktuális dátum és idő megjelenítése
  - `datetime.strptime()` - felhasználó által beírt dátum szövegből dátumobjektummá alakítása
  - `datetime.strftime()` - dátumobjektum formázott szöveggé alakítása
  - `uuid`
      - `uuid.uuid4()` - egyedi foglalásazonosító (ID) generálása

### Saját modul
- `app_PL.py`  
  Tartalmazza a grafikus felületet, az eseménykezelést, a fájlkezelést és a foglalásokkal kapcsolatos logikát.

## Osztályok
- `HotelAppPL`
  - Saját osztály.

## Saját függvények
- `mentes_PL()` - új foglalás mentése, dátumellenőrzéssel és árkalkulációval
- `listaz_PL()` - mentett foglalások listázása a szövegmezőben
- `torles_PL()` - foglalás törlése azonosító (ID) alapján
- További metódusok: `felulet()`, `frissit_ido()`, `betolt_adatok()`, `ment_adatok()`

## Eseménykezelés
- Gombnyomásra történik:
  - új foglalás mentése (`Foglalás mentése`)
  - foglalások listázása (`Foglalások listázása`)
  - foglalás törlése azonosító alapján (`Foglalás törlése ID alapján`)
- Az ablakban az idő folyamatosan frissül (`root.after` segítségével).

## Grafikus modul
- `tkinter`  
  - `Label`, `Entry`, `Button`, `Frame`, `Text`, `Tk`
