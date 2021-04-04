import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox, ttk, OptionMenu
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
import xml.etree.ElementTree as ET 
from matriz import Matriz
from listaMatrices import lista
import tkinter as tk
from graphviz import Source
from encabezado import listaEncabezado
import PIL
from PIL import Image, ImageTk
from tkinter import messagebox

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
            efilas=listaEncabezado()
            ecolumnas=listaEncabezado()
            imagen=Matriz(efilas,ecolumnas)
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
        messagebox.showinfo(message="Archivo leido exitosamente", title="Done")
        ventana.destroy()

def ventanaOperaciones1():
    Vent1 = tk.Toplevel()
    Vent1.title("Operaciones")
    Vent1.geometry("500x400")
    Vent1.config(bg="grey14")

    boton1= Button(Vent1, text="Operaciones con Una Imagen",height = 1,width = 25, font=fontBotones,relief=RAISED, command= ventanaSingle)
    boton2= Button(Vent1, text="Operaciones con Dos Imagenes",height = 1,width = 25, font=fontBotones,relief=RAISED, command= ventanaDoble)

    boton1.pack()
    boton2.pack()
    boton1.place(relx=0.15, rely=0.2)
    boton2.place(relx=0.15, rely=0.5)
    boton2.config(bg="grey14",fg="white")
    boton1.config(bg="grey14",fg="white")

def invertirHorizontal():
    global eleccionSingle, frameSingle, frameBienvenida, Ventana, panel1 , img1, canvas1, img2, canvas2, panel2, frameDoble
    nombre= str(eleccionSingle.get())
    print("Esta es la matriz seleccionada:"+str(nombre))
    print("Rotando Horizontalmete...") 
    
    matriz = matrices.getMatriz(nombre)
    
    m=matriz.m
    n=matriz.n
    efilas=listaEncabezado()
    ecolumnas=listaEncabezado()
    resultado=Matriz(efilas,ecolumnas)
    generarImagen(matriz.matriz,m,n,nombre)
    
    for y in range(1, int(matriz.m)+1):
        nodo=matriz.matriz.getUltimoByFilas(str(y))
        x=1
        while nodo is not None:
            caracter=nodo.caracter
            resultado.add(str(y),str(x),caracter)
            x+=1
            nodo = nodo.izquierda
    nombreImagen= nombre+'_resultado'
    generarImagen(resultado,m,n,nombreImagen)
   
    img1 = Image.open( nombre+'.png')  
    img1 = img1.resize((450, 450), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(img1)
    canvas1.create_image(225,225,image=photo1)
    matriz.matriz.ecolumnas=resultado.ecolumnas
    matriz.matriz.efilas=resultado.efilas
    matrices.setMatriz(nombre,matriz.matriz)
    generarImagen(resultado,m,n,nombreImagen)
    canvas1.pack(fill=None, expand=False)

 
    
    img2 = Image.open( nombre+'_resultado.png')  
    img2 = img2.resize((450, 450), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(img2)
    canvas2.create_image(225,225,image=photo2)
    canvas2.pack(fill=None, expand=False)
    canvas2.update()
    frameSingle.pack()
    frameBienvenida.pack_forget()
    frameDoble.pack_forget()
    Ventana.mainloop()

def invertirVertical():
    global eleccionSingle, frameSingle, frameBienvenida, Ventana, panel1 , img1, canvas1, img2, canvas2, panel2,frameDoble
    nombre= str(eleccionSingle.get())
    print("Esta es la matriz seleccionada:"+str(nombre))
    print("Rotando Verticalmente...") 
    
    matriz = matrices.getMatriz(nombre)
    m=matriz.m
    n=matriz.n
    efilas=listaEncabezado()
    ecolumnas=listaEncabezado()
    resultado=Matriz(efilas,ecolumnas)
    generarImagen(matriz.matriz,m,n,nombre)
    
    for x in range(1, int(matriz.n)+1):
        nodo=matriz.matriz.getUltimoByColumnas(str(x))
        y=1
        while nodo is not None:
            caracter=nodo.caracter
            resultado.add(str(y),str(x),caracter)
            y+=1
            nodo = nodo.arriba
    nombreImagen= nombre+'_resultado'
    generarImagen(resultado,m,n,nombreImagen)
   
    img1 = Image.open( nombre+'.png')  
    img1 = img1.resize((450, 450), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(img1)
    canvas1.create_image(225,225,image=photo1)
    matriz.matriz.ecolumnas=resultado.ecolumnas
    matriz.matriz.efilas=resultado.efilas
    matrices.setMatriz(nombre,matriz.matriz)
    generarImagen(resultado,m,n,nombreImagen)
    canvas1.pack(fill=None, expand=False)
    
    img2 = Image.open( nombre+'_resultado.png')  
    img2 = img2.resize((450, 450), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(img2)
    canvas2.create_image(225,225,image=photo2)
    canvas2.pack(fill=None, expand=False)
    canvas2.update()
    frameSingle.pack()
    frameBienvenida.pack_forget()
    frameDoble.pack_forget()
    Ventana.mainloop()

def transponer():
    global eleccionSingle, frameSingle, frameBienvenida, Ventana, panel1 , img1, canvas1, img2, canvas2, panel2,frameDoble
    nombre= str(eleccionSingle.get())
    print("Esta es la matriz seleccionada:"+str(nombre))
    print("Transponiendo Imagen...")
    
    matriz = matrices.getMatriz(nombre)
    m=matriz.m
    n=matriz.n
    efilas=listaEncabezado()
    ecolumnas=listaEncabezado()
    resultado1=Matriz(efilas, ecolumnas)
    generarImagen(matriz.matriz,m,n,nombre)

    
    for x in range(1, int(matriz.n)+1):
        nodo=matriz.matriz.getUltimoByColumnas(str(x))
        y=1
        while nodo is not None:
            caracter=nodo.caracter
            resultado1.add(str(x),str(y),caracter)
            y+=1
            nodo = nodo.arriba
    efilas2=listaEncabezado()
    ecolumnas2=listaEncabezado()
    resultado2=Matriz(efilas2,ecolumnas2)

    for y in range(1, int(matriz.n)+1):
        nodo=resultado1.getUltimoByFilas(str(y))
        x=1
        while nodo is not None:
            caracter=nodo.caracter
            resultado2.add(str(y),str(x),caracter)
            x+=1
            nodo = nodo.izquierda
    nombreImagen= nombre+'_resultado'
    generarImagen(resultado2,n,m,nombreImagen)
   
    img1 = Image.open( nombre+'.png')  
    img1 = img1.resize((450, 450), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(img1)
    canvas1.create_image(225,225,image=photo1)
    matriz.matriz.ecolumnas=resultado2.ecolumnas
    matriz.matriz.efilas=resultado2.efilas
    matrices.setMatriz(nombre,matriz.matriz)
    matrices.setDimensiones(nombre,n,m)
    canvas1.pack(fill=None, expand=False)
    
    img2 = Image.open( nombre+'_resultado.png')  
    img2 = img2.resize((450, 450), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(img2)
    canvas2.create_image(225,225,image=photo2)
    canvas2.pack(fill=None, expand=False)
    canvas2.update()
    frameSingle.pack()
    frameBienvenida.pack_forget()
    frameDoble.pack_forget()
    Ventana.mainloop()

def Limpiar(init_x, init_y, end_x, end_y):
    global eleccionSingle, frameSingle, frameBienvenida, Ventana, panel1 , img1, canvas1, img2, canvas2, panel2,frameDoble
    nombre= str(eleccionSingle.get())
    print("Esta es la matriz seleccionada:"+str(nombre))
    print("Limpiando zona...") 
    
    matriz = matrices.getMatriz(nombre)
    m=matriz.m
    n=matriz.n
    efilas=listaEncabezado()
    ecolumnas=listaEncabezado()
    resultado=Matriz(efilas,ecolumnas)
    generarImagen(matriz.matriz,m,n,nombre)
    if int(init_x) <= int(n) and int(init_y)<=int(m) and int(end_x) <= int(n) and int(end_y) <= int(m):  
        
        i=int(init_x)
        
        for x in range(1, int(matriz.n)+1):
            cambios=False
            j=int(init_y)
            for y in range(1, int(matriz.m)+1):
                dato=matriz.matriz.getDatoByColumnas(str(x),str(y))
                if x==i and y==j:
                    caracter="-"
                    resultado.add(str(y),str(x),caracter)
                    if j < int(end_y):
                        j+=1
                    cambios=True
                else:
                    caracter=dato.caracter
                    resultado.add(str(y),str(x),caracter)
            if cambios==True:
                if i < int(end_x):
                    i+=1


        nombreImagen= nombre+'_resultado'
        generarImagen(resultado,m,n,nombreImagen)
    
        img1 = Image.open( nombre+'.png')  
        img1 = img1.resize((450, 450), Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(img1)
        canvas1.create_image(225,225,image=photo1)
        matriz.matriz.ecolumnas=resultado.ecolumnas
        matriz.matriz.efilas=resultado.efilas
        matrices.setMatriz(nombre,matriz.matriz)
        generarImagen(resultado,m,n,nombreImagen)
        canvas1.pack(fill=None, expand=False)
        
        img2 = Image.open( nombre+'_resultado.png')  
        img2 = img2.resize((450, 450), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(img2)
        canvas2.create_image(225,225,image=photo2)
        canvas2.pack(fill=None, expand=False)
        canvas2.update()
        frameSingle.pack()
        frameBienvenida.pack_forget()
        frameDoble.pack_forget()
        Ventana.mainloop()

    else:
        messagebox.showwarning(message="Debe elegir coordenadas dentro del rango de la matriz seleccionada", title="Error")

def lineaVertical(init_x, init_y, largo):
    global eleccionSingle, frameSingle, frameBienvenida, Ventana, panel1 , img1, canvas1, img2, canvas2, panel2, frameDoble
    nombre= str(eleccionSingle.get())
    print("Esta es la matriz seleccionada:"+str(nombre))
    print("Creando linea vertical...") 
    
    matriz = matrices.getMatriz(nombre)
    m=matriz.m
    n=matriz.n
    efilas=listaEncabezado()
    ecolumnas=listaEncabezado()
    resultado=Matriz(efilas,ecolumnas)
    generarImagen(matriz.matriz,m,n,nombre)

    if int(init_x) <= int(n) and int(init_y)<=int(m):  
        
        if (int(init_y)+int(largo)-1)<=int(m): 
            
            i=int(init_x)
            
            for x in range(1, int(matriz.n)+1):
                
                j=int(init_y)
                nodo=matriz.matriz.getPrimeroByColumnas(str(x))
                
                while nodo is not None:
                    
                    if int(nodo.columna)==i and int(nodo.fila)==j:
                        if j <= (int(init_y)+int(largo)-1):
                            caracter="*"
                            resultado.add(str(nodo.fila), str(nodo.columna), caracter)
                            if j < (int(init_y)+int(largo)-1):
                               j+=1
                    else:
                        caracter=nodo.caracter
                        resultado.add(str(nodo.fila),str(nodo.columna), caracter)           
                    nodo=nodo.abajo

            nombreImagen= nombre+'_resultado'
            generarImagen(resultado,m,n,nombreImagen)
        
            img1 = Image.open( nombre+'.png')  
            img1 = img1.resize((450, 450), Image.ANTIALIAS)
            photo1 = ImageTk.PhotoImage(img1)
            canvas1.create_image(225,225,image=photo1)
            matriz.matriz.ecolumnas=resultado.ecolumnas
            matriz.matriz.efilas=resultado.efilas
            matrices.setMatriz(nombre,matriz.matriz)
            generarImagen(resultado,m,n,nombreImagen)
            canvas1.pack(fill=None, expand=False)
            
            img2 = Image.open( nombre+'_resultado.png')  
            img2 = img2.resize((450, 450), Image.ANTIALIAS)
            photo2 = ImageTk.PhotoImage(img2)
            canvas2.create_image(225,225,image=photo2)
            canvas2.pack(fill=None, expand=False)
            canvas2.update()
            frameSingle.pack()
            frameBienvenida.pack_forget()
            frameDoble.pack_forget()
            Ventana.mainloop()
        else:
            messagebox.showwarning(message="Debe elegir una longitud dentro del tamaño de la imagen", title="Error")
    else:
        messagebox.showwarning(message="Debe elegir coordenadas dentro del rango de la matriz seleccionada", title="Error")  

def lineaHorizontal(init_x, init_y, largo):
    global eleccionSingle, frameSingle, frameBienvenida, Ventana, panel1 , img1, canvas1, img2, canvas2, panel2, frameDoble
    nombre= str(eleccionSingle.get())
    print("Esta es la matriz seleccionada:"+str(nombre))
    print("Creando linea horizontal...") 
    
    matriz = matrices.getMatriz(nombre)
    m=matriz.m
    n=matriz.n
    efilas=listaEncabezado()
    ecolumnas=listaEncabezado()
    resultado=Matriz(efilas,ecolumnas)
    generarImagen(matriz.matriz,m,n,nombre)

    if int(init_x) <= int(n) and int(init_y)<=int(m):  
        
        if (int(init_x)+int(largo)-1)<=int(n): 
            
            j=int(init_y)
            
            for y in range(1, int(matriz.m)+1):
                
                i=int(init_x)
                nodo=matriz.matriz.getPrimeroByFilas(str(y))
                
                while nodo is not None:
                    
                    if int(nodo.columna)==i and int(nodo.fila)==j:
                        if i <= (int(init_x)+int(largo)-1):
                            caracter="*"
                            resultado.add(str(nodo.fila), str(nodo.columna), caracter)
                            if i < (int(init_x)+int(largo)-1):
                               i+=1
                    else:
                        caracter=nodo.caracter
                        resultado.add(str(nodo.fila),str(nodo.columna), caracter)           
                    nodo=nodo.derecha

            nombreImagen= nombre+'_resultado'
            generarImagen(resultado,m,n,nombreImagen)
        
            img1 = Image.open( nombre+'.png')  
            img1 = img1.resize((450, 450), Image.ANTIALIAS)
            photo1 = ImageTk.PhotoImage(img1)
            canvas1.create_image(225,225,image=photo1)
            matriz.matriz.ecolumnas=resultado.ecolumnas
            matriz.matriz.efilas=resultado.efilas
            matrices.setMatriz(nombre,matriz.matriz)
            generarImagen(resultado,m,n,nombreImagen)
            canvas1.pack(fill=None, expand=False)
            
            img2 = Image.open( nombre+'_resultado.png')  
            img2 = img2.resize((450, 450), Image.ANTIALIAS)
            photo2 = ImageTk.PhotoImage(img2)
            canvas2.create_image(225,225,image=photo2)
            canvas2.pack(fill=None, expand=False)
            canvas2.update()
            frameSingle.pack()
            frameBienvenida.pack_forget()
            frameDoble.pack_forget()
            Ventana.mainloop()
        else:
            messagebox.showwarning(message="Debe elegir una longitud dentro del tamaño de la imagen", title="Error")
    else:
        messagebox.showwarning(message="Debe elegir coordenadas dentro del rango de la matriz seleccionada", title="Error")    

def ventanaCoordenadas():
    import tkinter as tk
    global eleccionSingle, Ventana

    Vent2=tk.Toplevel() 
    Vent2.title("Coordenadas para Limpiar")
    Vent2.geometry("300x400")
    Vent2.config(bg="grey14")

    

    label=Label(Vent2, text="Ingrese Coordenada de inicio:",font=('Arial', 12), fg="white", bg="grey14")
    label.pack()
    label.place(relx=0.05, rely=0.1)
    label2=Label(Vent2, text="Ingrese Coordenada de finalización:",font=('Arial', 12), fg="white", bg="grey14")
    label2.pack()
    label2.place(relx=0.05, rely=0.5)
    
    label3=Label(Vent2, text="x=",font=('Arial', 12), fg="white", bg="grey14")
    label3.pack()
    label3.place(relx=0.1, rely=0.2)

    label4=Label(Vent2, text="y=",font=('Arial', 12), fg="white", bg="grey14")
    label4.pack()
    label4.place(relx=0.45, rely=0.2)

    label5=Label(Vent2, text="x=",font=('Arial', 12), fg="white", bg="grey14")
    label5.pack()
    label5.place(relx=0.1, rely=0.6)

    label5=Label(Vent2, text="y=",font=('Arial', 12), fg="white", bg="grey14")
    label5.pack()
    label5.place(relx=0.45, rely=0.6)

    init_x=IntVar()
    init_y=IntVar()
    end_x=IntVar()
    end_y=IntVar()

    entry1=Entry(Vent2,textvariable=init_x, width=5)
    entry2=Entry(Vent2,textvariable=init_y,width=5)
    entry3=Entry(Vent2,textvariable=end_x,width=5)
    entry4=Entry(Vent2,textvariable=end_y,width=5)
    entry1.pack()
    entry2.pack()
    entry3.pack()
    entry4.pack()

    entry1.place(relx=0.2, rely=0.2)
    entry2.place(relx=0.6, rely=0.2)
    entry3.place(relx=0.2, rely=0.6)
    entry4.place(relx=0.6, rely=0.6)

    boton1=Button(Vent2, text="Limpiar!", command = lambda: Limpiar(entry1.get(),entry2.get(),entry3.get(),entry4.get()))
    boton1.pack()
    boton1.place(relx = 0.5, rely = 0.8)
    boton1.config(bg="grey14",fg="white")

def ventanaSingle():
    import tkinter as tk
    global nombresMatrices, eleccionSingle, Ventana

    Vent2=tk.Toplevel() 
    Vent2.title("Operaciones en Una Imagen")
    Vent2.geometry("600x500")
    Vent2.config(bg="grey14")

    label=Label(Vent2, text="Seleccione una matriz a Operar:",font=('Arial', 15), fg="white", bg="grey14")
    label.pack()
    label.place(relx=0.05, rely=0.3)

    if nombresMatrices[0] is not None:
        eleccionSingle.set(nombresMatrices[0])

    opt = OptionMenu(Vent2, eleccionSingle, *nombresMatrices)
    opt.config(width=10, font=('Arial', 12))
    opt.pack()
    opt.place(relx=0.15, rely= 0.4)

    boton1=Button(Vent2,text="Rotar Horizontal",height = 1,width = 18, font=('Arial', 10),relief="raised", command=invertirHorizontal)
    boton1.pack()
    boton1.place(relx = 0.7, rely = 0.1)
    boton1.config(bg="grey14",fg="white")

    boton2=Button(Vent2,text="Rotar Vertical",height = 1,width = 18, font=('Arial', 10),relief="raised", command=invertirVertical)
    boton2.pack()
    boton2.place(relx = 0.7, rely = 0.2)
    boton2.config(bg="grey14",fg="white")

    boton3=Button(Vent2,text="Transpuesta",height = 1,width = 18,  font=('Arial', 10),relief="raised", command=transponer)
    boton3.pack()
    boton3.place(relx = 0.7, rely = 0.3)
    boton3.config(bg="grey14",fg="white")

    boton4=Button(Vent2,text="Limpiar Zona",height = 1,width = 18, font=('Arial', 10),relief="raised", command=ventanaCoordenadas)
    boton4.pack()
    boton4.place(relx = 0.7, rely = 0.4)
    boton4.config(bg="grey14",fg="white")

    boton5=Button(Vent2,text="Agregar Linea Horizontal",height = 1,width = 18, font=('Arial', 10),relief="raised", command= ventanaLineaHorizontal)
    boton5.pack()
    boton5.place(relx = 0.7, rely = 0.5)
    boton5.config(bg="grey14",fg="white")

    boton6=Button(Vent2,text="Agregar Linea Vertical",height = 1,width = 18, font=('Arial', 10),relief="raised", command= ventanaLineaVertical)
    boton6.pack()
    boton6.place(relx = 0.7, rely = 0.6)
    boton6.config(bg="grey14",fg="white")

    boton7=Button(Vent2,text="Agregar Rectangulo",height = 1,width = 18, font=('Arial', 10),relief="raised")
    boton7.pack()
    boton7.place(relx = 0.7, rely = 0.7)
    boton7.config(bg="grey14",fg="white")

    boton8=Button(Vent2,text="Agregar Triangulo",height = 1,width = 18, font=('Arial', 10),relief="raised")
    boton8.pack()
    boton8.place(relx = 0.7, rely = 0.8)
    boton8.config(bg="grey14",fg="white")

def union():
    global eleccionDoble1, eleccionDoble2, frameSingle, Ventana, frameBienvenida ,frameDoble, panelDoble1,panelDoble2,panelDoble3, canvasDoble1,canvasDoble2,canvasDoble3, img2Doble, img1Doble, img3Doble
    nombre1= str(eleccionDoble1.get())
    nombre2=str(eleccionDoble2.get())
    print("Esta es la primer matriz seleccionada:"+str(nombre1))
    print("Esta es la segunda matriz seleccionada:"+str(nombre2))
    print("Uniendo...") 
    
    matriz1 = matrices.getMatriz(nombre1)
    matriz2 = matrices.getMatriz(nombre2)
    m1=matriz1.m
    n1=matriz1.n

    m2=matriz2.m
    n2=matriz2.n

    efilas=listaEncabezado()
    ecolumnas=listaEncabezado()
    resultado=Matriz(efilas,ecolumnas)
    
    if nombre1 != nombre2:
        if int(m1) == int(m2) and int(n1) == int(n2):
            
            for x in range(1, int(n1)+1):
                nodo1=matriz1.matriz.getPrimeroByColumnas(str(x))
                nodo2=matriz2.matriz.getPrimeroByColumnas(str(x))
                y=1
                while nodo1 is not None and nodo2 is not None:
                    caracter1=nodo1.caracter
                    caracter2=nodo2.caracter

                    if caracter1 == "*" or caracter2=="*":
                        caracter="*"
                        resultado.add(str(y), str(x), caracter)
                    else:
                        caracter="-"
                        resultado.add(str(y), str(x), caracter)
                    y+=1
                    nodo1=nodo1.abajo
                    nodo2=nodo2.abajo        

            nombreImagen= str(nombre1+'_U_'+ nombre2+'_Resultado')
            generarImagen(resultado,m1,n1,nombreImagen)
            
            img1Doble = Image.open( nombre1+'.png')  
            img1Doble = img1Doble.resize((325, 400), Image.ANTIALIAS)
            photo1 = ImageTk.PhotoImage(img1Doble)
            canvasDoble1.create_image(163,200,image=photo1)
            matrices.add(m1,n1,nombreImagen,resultado)
            nombresMatrices.append(nombreImagen)
            generarImagen(resultado,m1,n1,nombreImagen)
            canvasDoble1.pack(fill=None, expand=False)

        
            
            img2Doble = Image.open( nombre2+'.png')  
            img2Doble= img2Doble.resize((325, 400), Image.ANTIALIAS)
            photo2 = ImageTk.PhotoImage(img2Doble)
            canvasDoble2.create_image(163,200,image=photo2)
            canvasDoble2.pack(fill=None, expand=False)
            

            img3Doble = Image.open( nombreImagen+'.png')  
            img3Doble = img3Doble.resize((325, 400), Image.ANTIALIAS)
            photo3 = ImageTk.PhotoImage(img3Doble)
            canvasDoble3.create_image(163,200,image=photo3)
            canvasDoble3.pack(fill=None, expand=False)
            canvasDoble2.update()
            canvasDoble1.update()
            canvasDoble3.update()
            frameDoble.pack()
            frameBienvenida.pack_forget()
            frameSingle.pack_forget()
            Ventana.mainloop()
        else:
            messagebox.showwarning(message="Ambas matrices deben tener dimensiones iguales", title="Error")        
    else:
        messagebox.showwarning(message="Debe elegir matrices distintas", title="Error")

def ventanaDoble():
    
    import tkinter as tk
    global nombresMatrices, eleccionDoble1, Ventana, eleccionDoble2

    Vent2=tk.Toplevel()    
    Vent2.title("Operaciones con Dos Imagenes")
    Vent2.geometry("600x400")
    Vent2.config(bg="grey14")


    label=Label(Vent2, text="Seleccione Imagen 1:",font=('Arial', 10), fg="white", bg="grey14")
    label.pack()
    label.place(relx=0.15, rely=0.2)

    label2=Label(Vent2, text="Seleccione Imagen 2:",font=('Arial', 10), fg="white", bg="grey14")
    label2.pack()
    label2.place(relx=0.5, rely=0.2)

    if nombresMatrices[0] is not None:
        eleccionDoble1.set(nombresMatrices[0])
        eleccionDoble2.set(nombresMatrices[0])

    opt = OptionMenu(Vent2, eleccionDoble1, *nombresMatrices)
    opt.config(width=10, font=('Arial', 12))
    opt.pack()
    opt.place(relx=0.2, rely= 0.3)
    opt.update()

    opt2 = OptionMenu(Vent2, eleccionDoble2, *nombresMatrices)
    opt2.config(width=10, font=('Arial', 12))
    opt2.pack()
    opt2.place(relx=0.55, rely= 0.3)
    opt2.update()

    boton1=Button(Vent2,text="Union",height = 1,width = 18, font=('Arial', 10),relief="raised", command=union)
    boton1.pack()
    boton1.place(relx = 0.2, rely = 0.6)
    boton1.config(bg="grey14",fg="white")

    boton2=Button(Vent2,text="Intersección",height = 1,width = 18, font=('Arial', 10),relief="raised")
    boton2.pack()
    boton2.place(relx = 0.55, rely = 0.6)
    boton2.config(bg="grey14",fg="white")

    boton3=Button(Vent2,text="Diferencia",height = 1,width = 18, font=('Arial', 10),relief="raised")
    boton3.pack()
    boton3.place(relx = 0.2, rely = 0.75)
    boton3.config(bg="grey14",fg="white")

    boton4=Button(Vent2,text="Diferencia Simetrica",height = 1,width = 18, font=('Arial', 10),relief="raised")
    boton4.pack()
    boton4.place(relx = 0.55, rely = 0.75)
    boton4.config(bg="grey14",fg="white")

def ventanaLineaHorizontal():

    import tkinter as tk
    global eleccionSingle, Ventana

    Vent2=tk.Toplevel() 
    Vent2.title("Coordenadas para Insertar Linea")
    Vent2.geometry("300x200")
    Vent2.config(bg="grey14")

    

    label=Label(Vent2, text="Ingrese Coordenada de inicio:",font=('Arial', 12), fg="white", bg="grey14")
    label.pack()
    label.place(relx=0.03, rely=0.1)
    label2=Label(Vent2, text="Ingrese numero de elementos:",font=('Arial', 12), fg="white", bg="grey14")
    label2.pack()
    label2.place(relx=0.05, rely=0.5)
    
    label3=Label(Vent2, text="x=",font=('Arial', 12), fg="white", bg="grey14")
    label3.pack()
    label3.place(relx=0.1, rely=0.26)

    label4=Label(Vent2, text="y=",font=('Arial', 12), fg="white", bg="grey14")
    label4.pack()
    label4.place(relx=0.45, rely=0.26)


    init_x=IntVar()
    init_y=IntVar()
    elements=IntVar()
    

    entry1=Entry(Vent2,textvariable=init_x, width=5)
    entry2=Entry(Vent2,textvariable=init_y,width=5)
    entry3=Entry(Vent2,textvariable=elements,width=5)
    entry1.pack()
    entry2.pack()
    entry3.pack()

    entry1.place(relx=0.2, rely=0.25)
    entry2.place(relx=0.6, rely=0.25)
    entry3.place(relx=0.2, rely=0.65)
    

    boton1=Button(Vent2, text="Agregar Linea!",command= lambda: lineaHorizontal(entry1.get(),entry2.get(),entry3.get()))
    boton1.pack()
    boton1.place(relx = 0.5, rely = 0.8)
    boton1.config(bg="grey14",fg="white")

def ventanaLineaVertical():

    import tkinter as tk
    global eleccionSingle, Ventana

    Vent2=tk.Toplevel() 
    Vent2.title("Coordenadas para Insertar Linea")
    Vent2.geometry("300x200")
    Vent2.config(bg="grey14")

    

    label=Label(Vent2, text="Ingrese Coordenada de inicio:",font=('Arial', 12), fg="white", bg="grey14")
    label.pack()
    label.place(relx=0.03, rely=0.1)
    label2=Label(Vent2, text="Ingrese numero de elementos:",font=('Arial', 12), fg="white", bg="grey14")
    label2.pack()
    label2.place(relx=0.05, rely=0.5)
    
    label3=Label(Vent2, text="x=",font=('Arial', 12), fg="white", bg="grey14")
    label3.pack()
    label3.place(relx=0.1, rely=0.26)

    label4=Label(Vent2, text="y=",font=('Arial', 12), fg="white", bg="grey14")
    label4.pack()
    label4.place(relx=0.45, rely=0.26)


    init_x=IntVar()
    init_y=IntVar()
    elements=IntVar()
    

    entry1=Entry(Vent2,textvariable=init_x, width=5)
    entry2=Entry(Vent2,textvariable=init_y,width=5)
    entry3=Entry(Vent2,textvariable=elements,width=5)
    entry1.pack()
    entry2.pack()
    entry3.pack()

    entry1.place(relx=0.2, rely=0.25)
    entry2.place(relx=0.6, rely=0.25)
    entry3.place(relx=0.2, rely=0.65)
    

    boton1=Button(Vent2, text="Agregar Linea!",command= lambda: lineaVertical(entry1.get(),entry2.get(),entry3.get()))
    boton1.pack()
    boton1.place(relx = 0.5, rely = 0.8)
    boton1.config(bg="grey14",fg="white")

Ventana = Tk()
Ventana.title("Pricipal")
Ventana.geometry("1200x650")
Ventana.config(bg="grey14")

eleccionSingle = tk.StringVar()
eleccionDoble1= tk.StringVar()
eleccionDoble2= tk.StringVar()

fontBotones = tkFont.Font(family="Lucida Grande", size=18)

frameBotones=Frame(Ventana,width=1200, height=50)
frameBotones.pack(fill=tk.X, side='top')
frameBotones.config(bg="grey7")

frameBienvenida = Frame(Ventana,width=1200, height=600)
frameBienvenida.pack( side='bottom')
frameBienvenida.config(bg="grey14")

frameSingle = Frame(Ventana,width=1200, height=600)
frameSingle.config(bg="grey14")

frameDoble = Frame(Ventana,width=1200, height=600)
frameDoble.config(bg="grey14")


panelDoble1=Frame(frameDoble,width=325, height=400)
panelDoble1.pack()
panelDoble1.place(relx = 0.05, rely = 0.1)
panelDoble1.config(relief="sunken",bd=3) 

panelDoble2=Frame(frameDoble,width=325, height=400)
panelDoble2.pack()
panelDoble2.place(relx = 0.35, rely = 0.1)
panelDoble2.config(relief="sunken",bd=3) 

panelDoble3=Frame(frameDoble,width=325, height=400)
panelDoble3.pack()
panelDoble3.place(relx = 0.7, rely = 0.1)
panelDoble3.config(relief="sunken",bd=3) 

labelDoble1=Label(frameDoble, text="Matriz 1", font=('Verdana', 12), fg="white", bg="grey14")
labelDoble1.pack()
labelDoble1.place(relx = 0.15, rely = 0.8)

labelDoble2=Label(frameDoble, text="Matriz 2", font=('Verdana', 12), fg="white", bg="grey14")
labelDoble2.pack()
labelDoble2.place(relx = 0.45, rely = 0.8)

labelDoble2=Label(frameDoble, text="Resultado", font=('Verdana', 12), fg="white", bg="grey14")
labelDoble2.pack()
labelDoble2.place(relx = 0.8, rely = 0.8)

labelDoble3=Label(frameDoble, text="=", font=('Verdana', 20), fg="white", bg="grey14")
labelDoble3.pack()
labelDoble3.place(relx = 0.65, rely = 0.4)

img1Doble = Image.open( 'default.png')
canvasDoble1=Canvas(panelDoble1, height=400, width=325)
canvasDoble1.update()

img2Doble = Image.open( 'default.png')
canvasDoble2=Canvas(panelDoble2, height=400, width=325)
canvasDoble2.update()

img3Doble = Image.open( 'default.png')
canvasDoble3=Canvas(panelDoble3, height=400, width=325)
canvasDoble3.update()

boton1=Button(frameBotones,text="Cargar Archivo",height = 1,width = 15, font=fontBotones,relief="flat",command=carga)
boton1.pack()
boton1.place(relx = 0.0, rely = 0)
boton1.config(bg="grey14",fg="white")

boton2=Button(frameBotones,text="Operaciones",height = 1,width = 15, font=fontBotones,relief="flat", command=ventanaOperaciones1)
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

panel1=Frame(frameSingle,width=450, height=400)
panel1.pack()
panel1.place(relx = 0.05, rely = 0.1)
panel1.config(relief="sunken",bd=3)      

label3=Label(frameSingle, text="Imagen Original", font=('Verdana', 12), fg="white", bg="grey14")
label3.pack()
label3.place(relx = 0.2, rely = 0.9)

label4=Label(frameSingle, text="Resultado", font=('Verdana', 12), fg="white", bg="grey14")
label4.pack()
label4.place(relx = 0.7, rely = 0.9)

label5=Label(frameSingle, text="=", font=('Verdana', 20), fg="white", bg="grey14")
label5.pack()
label5.place(relx = 0.475, rely = 0.5)

panel2=Frame(frameSingle,width=450, height=450)
panel2.pack()
panel2.place(relx = 0.55, rely = 0.1)
panel2.config(relief="sunken",bd=3)

img1 = Image.open( 'default.png')
canvas1=Canvas(panel1, height=450, width=450)
canvas1.update()

img2 = Image.open( 'default.png')
canvas2=Canvas(panel2, height=450, width=450)
canvas2.update()

label = Label(frameBienvenida, text="Bienvenido", font=('Arial', 150), fg="white", bg="grey14")
label.pack()
label.place(relx = 0.1, rely = 0.3)

Ventana.mainloop()


def limpiar():
    global root, tree
    root=None
    tree=None