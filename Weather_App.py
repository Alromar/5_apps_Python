from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False,False)

#icon
image_icon = PhotoImage(file="images/logo.png")
root.iconphoto(False,image_icon)

Round_box = PhotoImage(file="images/Rounded+Rectangle+1.png")
Label(root,image=Round_box, bg="#57adff").place(x=30, y=110)

#labels
label1=Label(root,text="Temperature", font=("Helvetica", 11), fg= "white", bg="#203243")
label1.place(x=50,y=120)

label2=Label(root,text="Humidity", font=("Helvetica", 11), fg= "white", bg="#203243")
label2.place(x=50,y=140)

label3 = Label(root,text="Pressure", font=("Helvetica", 11), fg= "white", bg="#203243")
label3.place(x=50,y=160)

label4=Label(root,text="Windspeed", font=("Helvetica", 11), fg= "white", bg="#203243")
label4.place(x=50,y=180)

label5=Label(root,text="Description", font=("Helvetica", 11), fg= "white", bg="#203243")
label5.place(x=50,y=200)

#search box
Search_image = PhotoImage(file="images/Rounded+Rectangle+3.png")
myimage= Label(image=Search_image, bg="#57adff")
myimage.place(x=270, y=120)

weat_image = PhotoImage(file="images/Layer+7.png")
weather_image = Label(root, image=weat_image, bg="#203243")
weather_image.place(x=290,y=127)

textfield = Entry(root,justify="center", width=15,font=("popins", 25,'bold'), bg="#203243",
                  border=0,fg='white')
textfield.place(x=370, y=130)
textfield.focus()

Search_icon = PhotoImage(file="Images/Layer+6 (1).png")
myimage_icon = Button(image=Search_icon,borderwidth=0,cursor='hand2',bg='#203243')
myimage_icon.place(x=645, y=125)

mainloop()
