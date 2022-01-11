from tkinter.constants import NO
from nodo import Nodo


class listaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def insertarPrimerPos(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.enlace = self.primero

        else:
            aux = Nodo(dato)
            aux.enlace = self.primero
            self.primero = aux
            self.ultimo.enlace = self.primero
        # return self.primero

    def insertarUltimaPos(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.enlace = Nodo(dato)
            self.ultimo.enlace = self.primero

    def recorrer(self):
        aux = self.primero
        while aux.enlace != self.primero:
            print(aux.dato)
            aux = aux.enlace
        return aux.dato
