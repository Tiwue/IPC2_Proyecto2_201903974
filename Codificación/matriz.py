from Nodos import Nodocelda, NodoEncabezado
from encabezado import listaEncabezado

class Matriz:
    def __init__(self, m, n, nombre):
        self.efilas=listaEncabezado()
        self.ecolumnas=listaEncabezado()
        self.m=m 
        self.n=n
        self.nombre=nombre

    def add(self,fila, columna, caracter):
        nuevo = Nodocelda(fila, columna, caracter)

        efila=self.efilas.getEncabezado(fila)
        if efila == None:
            encabezadoFilas= NodoEncabezado(fila)
            encabezadoFilas.accesoNodo=nuevo
            self.efilas.setEncabezado(encabezadoFilas)
        else:
            if nuevo.columna < encabezadoFilas.accesoNodo.columna:
                nuevo.derecha=encabezadoFilas.accesoNodo
                encabezadoFilas.accesoNodo.izquierda=nuevo
                encabezadoFilas.accesoNodo=nuevo
            else:
                actual=encabezadoFilas.accesoNodo
                while actual.derecha!=None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha=actual.derecha
                        actual.derecha.izquierda =nuevo
                        nuevo.izquierda = actual
                        actual.derecha= nuevo
                        break
                    actual=actual.derecha

                if actual.derecha == None:
                    actual.derecha=nuevo
                    nuevo.izquierda =actual           

        encabezadoColumnas = self.ecolumnas.getEncabezado(columna)
        if encabezadoColumnas==None:
            encabezadoColumnas=NodoEncabezado(columna)
            encabezadoColumnas.accesoNodo=nuevo
            self.ecolumnas.setEncabezado(encabezadoColumnas)
        else:
            if nuevo.fila< encabezadoColumnas.accesoNodo.fila:
                nuevo.abajo=encabezadoColumnas.accesoNodo
                encabezadoColumnas.accesoNodo.arriba=nuevo
                encabezadoColumnas.accesoNodo=nuevo
            else:
                actual = encabezadoColumnas.accesoNodo
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo.fila
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba=nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo

                if actual.abajo == None:
                    actual.abajo=nuevo
                    nuevo.arriba= actual
