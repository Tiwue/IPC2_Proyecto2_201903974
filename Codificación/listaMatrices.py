from Nodos import NodoListaMatrices
from matriz import Matriz

class lista:
    def __init__(self ):
        self.primero=None

    def add(self, m, n, nombre, matriz):
        nuevo= NodoListaMatrices(m,n,nombre,matriz)
        if self.primero is None:
            self.primero=nuevo
        else:
            actual=self.primero
            while actual.siguiente is not None:

                actual=actual.siguiente
            actual.siguiente=nuevo

    def length(self):
        contador=1
        temp=self.primero
        while temp.siguiente is not None:
            contador += 1
            temp = temp.siguiente            
        return contador

    def getMatriz(self, name):
        temp=self.primero
        while temp is not None:
            if str(temp.nombre) == str(name):
                return temp 
            temp=temp.siguiente    
        return None

    def setMatriz(self, name, matriz):
        temp=self.primero
        while temp is not None:
            if str(temp.nombre) == str(name):
                temp.matriz=matriz
            temp=temp.siguiente
            
    def setDimensiones(self, name, m, n):
        temp=self.primero
        while temp is not None:
            if str(temp.nombre) == str(name):
                temp.m=m
                temp.n=n
            temp=temp.siguiente



