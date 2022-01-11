class NodoD:
    def __init__(self, dato):
        self.dato = dato
        self.aux1 = None
        self.aux = None


class ListaD:
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__actual = None
        self.__n = 0

    def insertar_primero(self, dato):
        nodo = NodoD(dato)

        nodo.aux1 = self.__primero
        nodo.aux = None

        if (nodo.aux1 != None):
            nodo.aux1.aux = nodo

        self.__n = self.__n + 1
        self.__actual = nodo
        self.__primero = nodo

        if (self.__ultimo == None):
            self.__ultimo = nodo

    def insertar_ultimo(self, dato):
        nodo = NodoD(dato)

        nodo.aux1 = None
        nodo.aux = self.__ultimo

        nodo.aux.aux1 = nodo

        self.__n = self.__n + 1
        self.__actual = nodo
        self.__ultimo = nodo
        if (self.__primero == None):
            self.__primero = nodo

    def insertar(self, dato):
        if (self.__primero == None):
            self.insertar_primero(dato)
            return

        if (self.__actual == self.__ultimo):
            self.insertar_ultimo(dato)
            return

        nodo = NodoD(dato)

        nodo.aux1 = self.__actual.aux1
        nodo.aux = self.__actual

        nodo.aux1.aux = nodo
        nodo.aux.aux1 = nodo

        self.__n = self.__n + 1
        self.__actual = nodo

    def aux1(self):
        if (self.__actual != None and self.__actual != self.__ultimo):
            self.__actual = self.__actual.aux1

    def aux(self):
        if (self.__actual != None and self.__actual != self.__primero):
            self.__actual = self.__actual.aux

    def mostrar(self):
        nodo = self.__primero
        while (nodo != None):
            if (nodo == self.__actual):
                return nodo.dato
            else:
                nodo = nodo.aux1
                return nodo.dato

    def mostrar_inv(self):
        nodo = self.__ultimo
        while (nodo != None):
            if (nodo == self.__actual):
                return nodo.dato

            else:
                nodo = nodo.aux
                return nodo.dato
