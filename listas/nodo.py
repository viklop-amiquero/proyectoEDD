class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.enlace = None

    def __str__(self):
        return str(self.dato)
