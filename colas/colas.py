class Cola():
    def __init__(self):
        self.entrada = []
        self.tamanio = 0
        self.cabeza = 0

    def encolar(self, item):
        self.entrada.append(item)
        self.tamanio = self.tamanio + 1

    def desencolar(self):
        self.tamanio = self.tamanio - 1
        desencolar = self.entrada[self.cabeza]
        self.cabeza -= 1
        self.entrada = self.entrada[self.cabeza:]
        return desencolar

    def __str__(self):
        printed = '<' + str(self.entrada)[1:-1] + '>'
        return printed


# miCola = Cola()
# miCola.encolar(2)
# miCola.encolar(3)
# miCola.encolar(4)
# miCola.encolar(5)
# print(miCola)
