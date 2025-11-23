from tkinter import *
from app_PL import HotelAppPL

root = Tk()
root.title("Hotel Booking App")
root.geometry("720x480")

app = HotelAppPL(root)

root.mainloop()
