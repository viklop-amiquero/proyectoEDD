from listas.nodo import Nodo


class Linkedlist:
    def __init__(self):
        self.primero = None
        self.size = 0

    # Caso II insertar nodo en la primer posición
    def insertarPrimerPos(self, dato):

        nuevoNodo = Nodo(dato)
        nuevoNodo.enlace = self.primero
        self.primero = nuevoNodo

        return nuevoNodo

    # Caso III
    def insertarUltimaPos(self, dato):
        nuevoNodo = Nodo(dato)
        if self.size == 0:
            self.primero = nuevoNodo
        else:
            aux = self.primero
            while aux.enlace != None:
                aux = aux.enlace
            aux.enlace = nuevoNodo

        self.size += 1

        return nuevoNodo

    # Caso insertar un elemento después de un nodo buscado
    def insertarDespuesNodoBuscado(self, dato, datoBuscado):
        aux = aux1 = self.primero
        dato = dato
        nuevoNodo = Nodo(dato)
        datoBuscado = datoBuscado

        while aux1.dato != datoBuscado:
            aux1 = aux1.enlace
        nuevoNodo.enlace = aux1.enlace
        aux1.enlace = nuevoNodo

        return nuevoNodo

    def eliminar(self, dato):
        if self.size == 0:
            return False
        else:
            aux = self.primero
            try:
                while aux.enlace.dato != dato:
                    if aux.enlace == None:
                        return False
                    else:
                        aux = aux.enlace
                DeletedNode = aux.enlace
                aux.enlace = DeletedNode.enlace
            except AttributeError:
                return False
        self.size -= 1
        return DeletedNode

    def __len__(self):
        return self.size

    def __str__(self):
        string = "["
        aux = self.primero
        while aux != None:
            string += str(aux)
            # Este simple condicional para arreglar el tema de la coma
            if aux.enlace != None:
                string += str(", ")
            aux = aux.enlace
        string += "]"

        return string


# MyList = Linkedlist()
# MyList.insertarUltimaPos(789)
# MyList.insertarDespuesNodoBuscado(2, 3)
# MyList.insertarPrimerPos(1)
# MyList.insertarDespuesNodoBuscado(15, 2)
# MyList.eliminar(10)
# print(MyList)
