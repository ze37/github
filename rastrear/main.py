from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root = Tk()
root.title("Rastreamento De Numeros")
root.geometry("365x584")
root.resizable(False,False)

logo = PhotoImage(file="card.png")
Label(root,image=logo).place(x=240,y=70)

root.mainloop()