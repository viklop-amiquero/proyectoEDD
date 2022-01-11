import sys


class arbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

    def crearnodo(self):
        try:
            auxiliar = nodo(int(self.ui.texto.text()))
            if self.raiz == None:
                self.raiz = auxiliar
            else:
                self.insertar(self.raiz, auxiliar)
            self.repaint()
        except:
            print("No es un numero")
        self.ui.texto.setText("")
        self.ui.texto.setFocus()

    def insertar(self, auxiliar, nuevo):
        if nuevo.dato < auxiliar.dato:
            if auxiliar.izquierda == None:
                auxiliar.izquierda = nuevo
            else:
                self.insertar(auxiliar.izquierda, nuevo)
        elif nuevo.dato > auxiliar.dato:
            if auxiliar.derecha == None:
                auxiliar.derecha = nuevo
            else:
                self.insertar(auxiliar.derecha, nuevo)

    def inicializareliminar(self):
        try:
            if self.raiz != None:
                if self.raiz.dato == int(self.ui.texto.text()):
                    if self.raiz.izquierda == None and self.raiz.derecha == None:
                        self.raiz = None
                    elif self.raiz.izquierda == None:
                        self.raiz = self.raiz.derecha
                    elif self.raiz.derecha == None:
                        self.raiz = self.raiz.izquierda
                    else:
                        auxiliar = self.raiz.izquierda
                        self.raiz = self.raiz.derecha
                        self.insertar(self.raiz, auxiliar)
                else:
                    try:
                        self.eliminar(self.raiz, nodo(
                            int(self.ui.texto.text())))
                    except AttributeError:
                        print("No esta el numero")
                self.repaint()
                self.ui.texto.setText("")
                self.ui.texto.setFocus()
        except ValueError:
            print("No esta el numero")

    def eliminar(self, auxiliar, numero):
        if numero.dato < auxiliar.dato:
            if numero.dato == auxiliar.izquierda.dato:
                if auxiliar.izquierda.izquierda == None and auxiliar.izquierda.derecha == None:
                    auxiliar.izquierda = None
                elif auxiliar.izquierda.izquierda == None:
                    auxiliar.izquierda = auxiliar.izquierda.derecha
                elif auxiliar.izquierda.derecha == None:
                    auxiliar.izquierda = auxiliar.izquierda.izquierda
                else:
                    auxiliar2 = auxiliar.izquierda.izquierda
                    auxiliar.izquierda = auxiliar.izquierda.derecha
                    self.insertar(auxiliar.izquierda, auxiliar2)
            else:
                self.eliminar(auxiliar.izquierda, numero)
        elif numero.dato > auxiliar.dato:
            if numero.dato == auxiliar.derecha.dato:
                if auxiliar.derecha.derecha == None and auxiliar.derecha.izquierda == None:
                    auxiliar.derecha = None
                elif auxiliar.derecha.izquierda == None:
                    auxiliar.derecha = auxiliar.derecha.derecha
                elif auxiliar.derecha.derecha == None:
                    auxiliar.derecha = auxiliar.derecha.izquierda
                else:
                    auxiliar2 = auxiliar.derecha.izquierda
                    auxiliar.derecha = auxiliar.derecha.derecha
                    self.insertar(auxiliar.derecha, auxiliar2)
            else:
                self.eliminar(auxiliar.derecha, numero)
