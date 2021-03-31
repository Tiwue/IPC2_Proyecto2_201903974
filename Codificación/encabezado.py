from Nodos import NodoEncabezado, Nodocelda

class listaEncabezado:
    def __init__(self):
        self.primero=None 

    def setEncabezado(self, nuevo):
        if self.primero== None: 
            self.primero=nuevo
        elif int(nuevo.index) < int(self.primero.index):
            nuevo.siguiente=self.primero
            self.primero.anterior=nuevo
            self.primero=nuevo
        else:
            actual=self.primero
            while actual.siguiente is not None:
            
                if int(nuevo.index) < int(actual.siguiente.index):
                    nuevo.siguiente=actual.siguiente
                    actual.siguiente.anterior=nuevo
                    nuevo.anterior=actual
                    actual.siguiente=nuevo
                    break
                actual=actual.siguiente   

            if actual.siguiente==None:
                actual.siguiente=nuevo
                nuevo.anterior=actual

    def getEncabezado(self,index):
        actual=self.primero
        while actual != None:
            if actual.index == index:
                return actual
            actual=actual.siguiente
        return None
