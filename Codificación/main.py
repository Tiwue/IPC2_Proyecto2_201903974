import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
import xml.etree.ElementTree as ET 
from matriz import Matriz
from listaMatrices import lista
import tkinter as tk
from graphviz import Source

import PIL
from PIL import Image, ImageTk

tree = None
root=None
matrices=lista()
nombresMatrices=list()

def generarImagen(matriz, m , n, nombre):
   
    llena='<td bgcolor="black">   </td>'
    vacia='<td>   </td>' 
    inicio='digraph G { tbl [ shape=plaintext label=<<table color="gray25" border="1" cellborder=\'1\' cellspacing="0"><tr > <td colspan="'+n+'">'+nombre+'</td></tr>'
    fila=0
    columna=0
    cadena=''
    for i in range(1, int(m)+1):
        fila+=1
        cadena+='<tr>'
        for j in range(1, int(n)+1):
            columna+=1
            celda=matriz.getDatoByColumnas(str(j),str(i))
            if celda.caracter == "*":
                cadena +=llena
            elif celda.caracter == "-":
                cadena += vacia
        cadena+= '</tr>'
    cadena +='</table>>];'
    fin="}"
    temp = inicio+cadena+fin 
    s = Source(temp, filename=nombre, format="png") 
    s.render()

def carga():
        global tree,root,matrices,nombresMatrices
    
        ventana=Tk()
       
        ventana.filename = filedialog.askopenfilename()
        tree=ET.parse(ventana.filename)
        root=tree.getroot() 
        for element in root:
            elementNombre = element.find('nombre')
            nombre=elementNombre.text
            elementM= element.find('filas')
            m=elementM.text
            elementN= element.find('columnas')
            n=elementN.text
            elementTextoImagen= element.find('imagen')
            textoImagen=str(elementTextoImagen.text)
            imagen=Matriz()
            fila=0
            columna=0
            for caracter in str(textoImagen):
                if caracter == ' ':
                    continue
                elif caracter == '\t':
                    continue
                elif caracter == '-':
                    columna+=1
                    imagen.add(str(fila),str(columna),caracter)
                elif caracter == '*':
                    columna+=1
                    imagen.add(str(fila),str(columna),caracter)
                elif caracter== '\n':
                    fila+=1
                    columna=0
            matrices.add(m,n,nombre,imagen)
            nombresMatrices.append(nombre)                   
            generarImagen(imagen,m,n,nombre)

        ventana.destroy()

def mostrarSingle():
    frameSingle.pack( side='bottom')
    frameBienvenida.pack_forget()
  
def recuperarBienvenida():
    frameBienvenida.pack(side='bottom')
    frameSingle.pack_forget()

Ventana = Tk()
Ventana.title("Pricipal")
Ventana.geometry("1200x650")
Ventana.config(bg="grey14")

fontBotones = tkFont.Font(family="Lucida Grande", size=18)

frameBotones=Frame(Ventana,width=1200, height=50)
frameBotones.pack(fill=tk.X, side='top')
frameBotones.config(bg="grey7")

frameBienvenida = Frame(Ventana,width=1200, height=600)
frameBienvenida.pack( side='bottom')
frameBienvenida.config(bg="grey14")

frameSingle = Frame(Ventana,width=1200, height=600)
frameSingle.config(bg="grey14")

boton1=Button(frameBotones,text="Cargar Archivo",height = 1,width = 15, font=fontBotones,relief="flat",command=carga)
boton1.pack()
boton1.place(relx = 0.0, rely = 0)
boton1.config(bg="grey14",fg="white")

boton2=Button(frameBotones,text="Operaciones",height = 1,width = 15, font=fontBotones,relief="flat", command=mostrarSingle)
boton2.pack()
boton2.place(relx = 0.2, rely = 0)
boton2.config(bg="grey14",fg="white")

boton3=Button(frameBotones,text="Reportes",height = 1,width = 15, font=fontBotones,relief="flat", command=recuperarBienvenida)
boton3.pack()
boton3.place(relx = 0.4, rely = 0)
boton3.config(bg="grey14",fg="white")

boton4=Button(frameBotones,text="Ayuda",height = 1,width = 15, font=fontBotones,relief="flat")
boton4.pack()
boton4.place(relx = 0.6, rely = 0)
boton4.config(bg="grey14",fg="white")

panel1=Frame(frameSingle,width=450, height=400)
panel1.pack()
panel1.place(relx = 0.05, rely = 0.1)
panel1.config(relief="sunken",bd=3)      



img = Image.open('A.png')
canvas=Canvas(panel1, height=450, width=450)

img = img.resize((450, 450), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)
canvas=Canvas(panel1, height=450, width=450)
canvas.create_image(210,200,image=photo)
canvas.pack(fill=None, expand=False)


panel2=Frame(frameSingle,width=450, height=450)
panel2.pack()
panel2.place(relx = 0.55, rely = 0.1)
panel2.config(relief="sunken",bd=3)



label = Label(frameBienvenida, text="Bienvenido", font=('Modern', 100), fg="white", bg="grey14")
label.pack()
label.place(relx = 0.3, rely = 0.1)
Ventana.mainloop()

 

def limpiar():
    global root, tree
    root=None
    tree=None
       



