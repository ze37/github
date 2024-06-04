from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from PIL import Image,ImageTk

from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root = Tk()
root.title("Rastreamento De Numeros")
root.geometry("365x584")
root.resizable(False,False)

logo = PhotoImage(file="rastro1.png")
Label(root,image=logo).place(x=240,y=70)
# colocando icon no formulario
icon = Image.open("rastro.png")
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False,photo)

cabecalho = Label(root,text="Rastreamento De Telefone", font=("arial",10,"bold"))
cabecalho.place(x=70,y=115)

entry_cabecalho = PhotoImage(file="pesquiza.png")
Label(root,image=entry_cabecalho).place(x=70,y=245)


entry = StringVar()
enter_numero = Entry(root,textvariable=entry,width=15,bd=0,font=("arial",20),justify="center")
enter_numero.place(x=84,y=270)








root.mainloop()