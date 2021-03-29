import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
import xml.etree.ElementTree as ET 
from matriz import Matriz

import PIL
from PIL import Image, ImageTk

tree = None
root=None

def carga():
    global tree,root
    
    ventana=Tk()
    try:    
        ventana.filename = filedialog.askopenfilename()
        tree=ET.parse(ventana.filename)
        root=tree.getroot() 
        for element in root:
            for subelement in element:
                print(subelement.text)
                
    except:
        print("No fue posible leer el archivo")    
    
    ventana.destroy()




Ventana = Tk()
Ventana.title("Pricipal")
Ventana.geometry("1200x650")
Ventana.config(bg="grey14")

fontBotones = tkFont.Font(family="Lucida Grande", size=18)

frameBotones=Frame(Ventana,width=1200, height=50)
frameBotones.pack(side='top')
frameBotones.config(bg="grey7")

frame = Frame(Ventana,width=1200, height=600)
frame.pack(side='bottom')
frame.config(bg="grey14")

boton1=Button(frameBotones,text="Cargar Archivo",height = 1,width = 15, font=fontBotones,relief="flat",command=carga)
boton1.pack()
boton1.place(relx = 0.0, rely = 0)
boton1.config(bg="grey14",fg="white")

boton2=Button(frameBotones,text="Operaciones",height = 1,width = 15, font=fontBotones,relief="flat")
boton2.pack()
boton2.place(relx = 0.2, rely = 0)
boton2.config(bg="grey14",fg="white")

boton3=Button(frameBotones,text="Reportes",height = 1,width = 15, font=fontBotones,relief="flat")
boton3.pack()
boton3.place(relx = 0.4, rely = 0)
boton3.config(bg="grey14",fg="white")

boton4=Button(frameBotones,text="Ayuda",height = 1,width = 15, font=fontBotones,relief="flat")
boton4.pack()
boton4.place(relx = 0.6, rely = 0)
boton4.config(bg="grey14",fg="white")

panel1=Frame(frame,width=450, height=450)
panel1.pack()
panel1.place(relx = 0.05, rely = 0.1)
panel1.config(relief="sunken",bd=3)

image = Image.open('imagen.png')
canvas=Canvas(panel1, height=450, width=450)
basewidth = 450
image = image.resize((450, 480), PIL.Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
item4 = canvas.create_image(225,200,image=photo)
canvas.pack(expand=True, fill=BOTH)

panel2=Frame(frame,width=450, height=450)
panel2.pack()
panel2.place(relx = 0.55, rely = 0.1)
panel2.config(relief="sunken",bd=3)
Ventana.mainloop()

 

def limpiar():
    global root, tree
    root=None
    tree=None
       
 
 

