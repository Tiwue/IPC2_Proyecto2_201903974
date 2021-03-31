# ------------------------- Clases para crear las listas doblemente enlazadas de las cabeceras/cabezas para filas y para columnas
class NodoEncabezado:
	def __init__(self, index):
		self.index = index
		self.anterior = None
		self.siguiente = None
		self.accesoNodo=None
#-----------------------------Codigo para empezar la Lista Ortogonal -----> MATRIZ <----------------
class Nodocelda:
	def __init__(self, fila, columna, caracter):
		self.caracter = caracter # * o -
		self.fila = fila
		self.columna = columna
		self.arriba = None
		self.abajo = None 
		self.derecha = None 
		self.izquierda = None

class NodoListaMatrices:
    def __init__(self, m, n, nombre, matriz):
        self.m=m 
        self.n=n
        self.nombre=nombre
        self.matriz=matriz
        self.siguiente=None 
