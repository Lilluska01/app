from tkinter import *
from app_PL import HotelAppPL

root = Tk()
root.title("Hotel Foglalás App PL")
root.geometry("500x400")

app = HotelAppPL(root)

root.mainloop()
