# from tkinter import *
# import phonenumbers
# from phonenumbers import carrier
# from phonenumbers import geocoder
# from phonenumbers import timezone
# from PIL import Image,ImageTk

# from timezonefinder import TimezoneFinder
# from geopy.geocoders import Nominatim
# from datetime import datetime
# import pytz


# def tracker():
#     enter_numero = entry.get()
#     number = phonenumbers.parse(enter_numero)
#     local = geocoder.description_for_number(number,"br")
#     cidade.config(text=local)

#     operadora = carrier.name_for_number(number,"br")
#     sim.config(text=operadora)

#     time = timezone.time_zones_for_number(number)
#     zone.config(text=time)

#     geolocal = Nominatim(user_agent="geoapiExercises")
#     localizasao = geolocal.geocode(local)
#     lng = localizasao.longitude
#     lat = localizasao.latitude
#     longitude.config(text=lng)
#     latitude.config(text=lat)

#     obj = TimezoneFinder()
#     result = obj.timezone_at(lng=localizasao.longitude, lat=localizasao.latitude)
#     home = pytz.timezone(result)
#     local_time = datetime.now(home)
#     current_time = localizasao_time.strftime("%I:%M:%p")
#     clock.config(text=current_time)


# root = Tk()
# root.title("Rastreamento De Numeros")
# root.geometry("365x584")
# root.resizable(False,False)
# # Crregar o logo do sistema
# logo = PhotoImage(file="rastro1.png")
# Label(root,image=logo).place(x=240,y=70)
# # colocando icon no formulario
# icon = Image.open("rastro1.png")
# photo = ImageTk.PhotoImage(icon)
# root.wm_iconphoto(False,photo)
# # texto ao lado do icon
# cabecalho = Label(root,text="Rastreamento De Telefone", font=("arial",10,"bold"))
# cabecalho.place(x=70,y=115)
# #imagem do icon de pesquisa
# entry_cabecalho = PhotoImage(file="pesquiza.png")
# Label(root,image=entry_cabecalho).place(x=70,y=245)

# #campo de pesquisa
# entry = StringVar()
# enter_numero = Entry(root,textvariable=entry,width=15,bd=0,font=("arial",20),justify="center")
# enter_numero.place(x=84,y=270)

# # Botäo pesquizar o numero telefonico
# pesquisar_image = PhotoImage(file="texte2.png")
# pesquisar = Button(image=pesquisar_image,borderwidth=0,cursor="hand2",bd=0,font=("arial",15),command=tracker)
# pesquisar.place(x=64,y=305)


# box_pesquizar = PhotoImage(file="caixa.png")
# Label(root,image=box_pesquizar).place(x=6,y=380)


# cidade = Label(root,text="Cidade : ",bg="dim gray",fg="black", font=("arial",10,"bold"))
# cidade.place(x=50,y=390)

# sim = Label(root,text="Operadora : ",bg="dim gray",fg="black", font=("arial",10,"bold"))
# sim.place(x=200,y=390)

# zone = Label(root,text="Paiz : ",bg="dim gray",fg="black", font=("arial",10,"bold"))
# zone.place(x=50,y=470)

# clock = Label(root,text="Horario : ",bg="dim gray",fg="black", font=("arial",10,"bold"))
# clock.place(x=200,y=470)

# latitude = Label(root,text="Latitude : ",bg="dim gray",fg="black", font=("arial",10,"bold"))
# latitude.place(x=50,y=550)

# longitude = Label(root,text="Longitude : ",bg="dim gray",fg="black", font=("arial",10,"bold"))
# longitude.place(x=200,y=550)

# root.mainloop()
from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from PIL import Image, ImageTk

from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

def tracker():
    enter_numero = entry.get()
    number = phonenumbers.parse(enter_numero)
    local = geocoder.description_for_number(number, "pt")
    cidade.config(text="Cidade: " + local)

    operadora = carrier.name_for_number(number, "pt")
    sim.config(text="Operadora: " + operadora)

    time = timezone.time_zones_for_number(number)
    zone.config(text="País: " + str(time))

    geolocal = Nominatim(user_agent="geoapiExercises")
    localizacao = geolocal.geocode(local)
    if localizacao:
        lng = localizacao.longitude
        lat = localizacao.latitude
        longitude.config(text="Longitude: " + str(lng))
        latitude.config(text="Latitude: " + str(lat))

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=lng, lat=lat)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text="Horário: " + current_time)
    else:
        longitude.config(text="Longitude: Não encontrado")
        latitude.config(text="Latitude: Não encontrado")
        clock.config(text="Horário: Não encontrado")

root = Tk()
root.title("Rastreamento De Números")
root.geometry("365x584")
root.resizable(False, False)

# Carregar o logo do sistema
logo = PhotoImage(file="rastro1.png")
Label(root, image=logo).place(x=240, y=70)

# Colocando ícone no formulário
icon = Image.open("rastro1.png")
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False, photo)

# Texto ao lado do ícone
cabecalho = Label(root, text="Rastreamento De Telefone", font=("arial", 10, "bold"))
cabecalho.place(x=70, y=115)

# Imagem do ícone de pesquisa
entry_cabecalho = PhotoImage(file="pesquiza.png")
Label(root, image=entry_cabecalho).place(x=70, y=245)

# Campo de pesquisa
entry = StringVar()
enter_numero = Entry(root, textvariable=entry, width=15, bd=0, font=("arial", 20), justify="center")
enter_numero.place(x=84, y=270)

# Botão pesquisar o número telefônico
pesquisar_image = PhotoImage(file="texte2.png")
pesquisar = Button(image=pesquisar_image, borderwidth=0, cursor="hand2", bd=0, font=("arial", 15), command=tracker)
pesquisar.place(x=64, y=305)

box_pesquisar = PhotoImage(file="caixa.png")
Label(root, image=box_pesquisar).place(x=6, y=380)

cidade = Label(root, text="Cidade: ", bg="dim gray", fg="black", font=("arial", 10, "bold"))
cidade.place(x=50, y=390)

sim = Label(root, text="Operadora: ", bg="dim gray", fg="black", font=("arial", 10, "bold"))
sim.place(x=200, y=390)

zone = Label(root, text="País: ", bg="dim gray", fg="black", font=("arial", 10, "bold"))
zone.place(x=50, y=470)

clock = Label(root, text="Horário: ", bg="dim gray", fg="black", font=("arial", 10, "bold"))
clock.place(x=200, y=470)

latitude = Label(root, text="Latitude: ", bg="dim gray", fg="black", font=("arial", 10, "bold"))
latitude.place(x=50, y=550)

longitude = Label(root, text="Longitude: ", bg="dim gray", fg="black", font=("arial", 10, "bold"))
longitude.place(x=200, y=550)

root.mainloop()
