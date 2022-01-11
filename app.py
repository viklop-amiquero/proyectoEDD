from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import numpy as np
from pilas.pila import Pila
# from listas.nodo import Nodo
from listas.listaSimple import Linkedlist
from random import randint
from colas.colas import Cola
import matplotlib.pyplot as plt
from matplotlib_venn import venn2


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configuración inicial

        self.configure(bg='black')
        font.nametofont('TkDefaultFont').configure(size=12, underline=True)
        self.title('Proyecto Estructura de Datos')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # self.geometry('1200x720')

        # Contenedor principal
        contenedor_principal = tk.Frame(self, bg='#258BED')
        contenedor_principal.grid(
            row=0, column=0, columnspan=3, padx=20, pady=20)

        # Diccionario de Frames
        self.todos_los_frames = dict()

        for F in (Frame_1, Frame_2, Frame_3, Frame_4, Frame_5, Frame_6):

            frame = F(contenedor_principal, self)
            self.todos_los_frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Frame_1)

    def show_frame(self, contenedor_llamado):
        frame = self.todos_los_frames[contenedor_llamado]
        frame.tkraise()


class Frame_1(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        # Configuraión inicial
        self.configure(bg='#258BED')
        self.entrada_usuario = tk.StringVar()

        # Label
        titulo = tk.Label(self, text="Proyecto Final de Estructura de Datos", font=(
            "Roboto", 36, "bold"), bg="#258BED", fg="black")

        titulo.grid(row=1, column=0, columnspan=40,
                    padx=20, pady=20, sticky="n")

        # Datos
        estudiante = tk.Label(self, text="UNSCH",
                              font=("Roboto", 14), bg="#258BED", fg='black')
        estudiante.grid(row=3, column=3, sticky="w", padx=20)

        estudiante = tk.Label(self, text="EP: Ingeniería de Sistemas",
                              font=("Roboto", 14), bg="#258BED", fg='black')
        estudiante.grid(row=5, column=3, sticky="w",  padx=20)

        estudiante = tk.Label(self, text="Developed by:",
                              font=("Roboto", 12), bg="#258BED", fg='black')
        estudiante.grid(row=6, column=3, sticky="w", pady=10, padx=20)

        nombre = tk.Label(self, text="Víctor López Amiquero",
                          font=("Roboto", 12), bg="#258BED", fg='black')
        nombre.grid(row=7, column=3, sticky="w", padx=20)

        # Boton
        btnConjunto = ttk.Button(
            self, text="Conjuntos", command=lambda: controller.show_frame(Frame_2))

        btnConjunto.grid(row=8, column=3, pady=50, sticky="e")

        # Boton matrices
        btnConjunto = ttk.Button(
            self, text="Matrices", command=lambda: controller.show_frame(Frame_3))

        btnConjunto.grid(row=8, column=4, pady=50, padx=20, sticky="e")

        # Botón listas
        btnPilas = ttk.Button(
            self, text="Listas", command=lambda: controller.show_frame(Frame_4))

        btnPilas.grid(row=8, column=5, pady=50, padx=20, sticky="e")

        # Botón pilas
        btnPilas = ttk.Button(
            self, text="Pilas", command=lambda: controller.show_frame(Frame_5))

        btnPilas.grid(row=8, column=6, pady=50, padx=20, sticky="e")

        # Botón pilas
        btnPilas = ttk.Button(
            self, text="Colas", command=lambda: controller.show_frame(Frame_6))

        btnPilas.grid(row=8, column=7, pady=50, padx=20, sticky="e")

        # Botón pilas
        btnPilas = ttk.Button(
            self, text="Arboles", command=lambda: controller.show_frame(Frame_5))

        btnPilas.grid(row=8, column=8, pady=50, padx=20, sticky="e")

        # Botón pilas
        btnPilas = ttk.Button(
            self, text="Grafos", command=lambda: controller.show_frame(Frame_5))

        btnPilas.grid(row=8, column=9, pady=50, padx=20, sticky="e")


class Frame_2(tk.Frame):

    # Conjuntos

    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="#258BED")

        entrada_usuario = tk.StringVar()
        entrada_usuario2 = tk.StringVar()
        resultado = tk.StringVar()

        def union():
            listaA = str(entrada_usuario.get()).split(',')
            listaB = str(entrada_usuario2.get()).split(',')

            conjUnion = set(listaA+listaB)
            resultado.set(conjUnion)

        def interseccion():
            listaA = str(entrada_usuario.get()).split(',')
            listaB = str(entrada_usuario2.get()).split(',')

            conjInterseccion = []
            for i in listaA:
                if i in listaB:
                    conjInterseccion.append(i)

            resultado.set(set(conjInterseccion))
            if not conjInterseccion:
                resultado.set('No existe intersección')

        def diferencia():
            listaA = str(entrada_usuario.get()).split(',')
            listaB = str(entrada_usuario2.get()).split(',')

            for i in listaB:
                if i in listaA:
                    listaA.remove(i)
            conjDiferencia = set(listaA)
            resultado.set(conjDiferencia)

        def diferenciaSimetrica():

            listaA = str(entrada_usuario.get()).split(',')
            listaB = str(entrada_usuario2.get()).split(',')

            listaUnion = listaA + listaB
            listaSinrep = []

            for i in listaUnion:
                if i not in listaSinrep:
                    listaSinrep.append(i)

            conjInterseccion = []
            for i in listaA:
                if i in listaB:
                    conjInterseccion.append(i)

            for i in conjInterseccion:
                if i in listaSinrep:
                    listaSinrep.remove(i)
            conjDifSimetrica = set(listaSinrep)

            resultado.set(conjDifSimetrica)

        def limpiar():
            entrada_usuario.set('')
            entrada_usuario2.set('')
            resultado.set('')
            # print('Hola Mundo')

        # Label
        lblconjuntoA = tk.Label(self, text="Conjunto A", font=(
            "Roboto", 14, "bold"), bg="#258BED", fg="black")
        lblconjuntoA.grid(row=3, column=4, columnspan=20, sticky="n", pady=20)
        entryConjA = ttk.Entry(
            self, textvariable=entrada_usuario, width=50, font=("Roboto Cn", 20))
        entryConjA.grid(row=4, columnspan=20, padx=(10, 20))

        lblconjuntoB = tk.Label(self, text="Conjunto B", font=(
            "Roboto", 14, 'bold'), bg="#258BED")
        lblconjuntoB.grid(row=5, column=4, columnspan=20, sticky="n", pady=20)

        entryConjB = ttk.Entry(
            self, textvariable=entrada_usuario2, width=50, font=("Roboto Cn", 20))
        entryConjB.grid(row=6, column=4, columnspan=20, padx=(10, 20))

        lblconjuntoC = tk.Label(self, text="Resultado", font=(
            "Roboto", 14, 'bold'), bg="#258BED")
        lblconjuntoC.grid(row=7, column=4, columnspan=20, sticky="n", pady=20)

        boxresultado = ttk.Entry(
            self, textvariable=resultado, width=50, font=("Roboto Cn", 20))
        boxresultado.grid(row=8, column=4, columnspan=20, padx=(10, 20))

        btnUnion = ttk.Button(self, text="Unión", command=union)
        btnUnion.grid(row=10, column=4, pady=20, padx=20)

        btnInterseccion = ttk.Button(
            self, text="Intersección", command=interseccion)
        btnInterseccion.grid(row=10, column=5, pady=20, padx=20)

        btndiferencia = ttk.Button(self, text="Diferencia", command=diferencia)
        btndiferencia.grid(row=10, column=6, pady=20, padx=20)

        btnDifSimetrica = ttk.Button(
            self, text="Dif. Simétrica", command=diferenciaSimetrica)
        btnDifSimetrica.grid(row=10, column=7, pady=20, padx=20)

        btnLimpiar = ttk.Button(self, text="Limpiar", command=limpiar)
        btnLimpiar.grid(row=10, column=8, pady=20, padx=20)

        btnMenu = ttk.Button(self, text="Menú",
                             command=lambda: controller.show_frame(Frame_1))
        btnMenu.grid(row=10, column=9, pady=20, padx=20)


class Frame_3(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="#258BED")

        entrada_usuario1 = tk.StringVar()
        entrada_usuario2 = tk.StringVar()
        entrada_usuario3 = tk.StringVar()
        entrada_usuario4 = tk.StringVar()
        resultado = tk.StringVar()

        def convertirArray():
            lista1 = str(entrada_usuario1.get()).split(',')
            lista2 = str(entrada_usuario2.get()).split(',')
            lista3 = str(entrada_usuario3.get()).split(',')
            lista4 = str(entrada_usuario4.get()).split(',')

            listaTotal = [lista1, lista2, lista3, lista4]

            listaEnt1 = []
            listaEnt2 = []
            listaEnt3 = []
            listaEnt4 = []

            listaEntTotal = [listaEnt1, listaEnt2, listaEnt3, listaEnt4]

            # Convertir lista de cadenas a elementos enteros
            def crearListaEnteros(listan, listEn):
                for i in range(len(listan)):
                    listEn.insert(i, int(listan[i]))

            for i in range(len(listaTotal)):
                crearListaEnteros(listaTotal[i], listaEntTotal[i])

            array2 = np.array([listaEnt1, listaEnt2, listaEnt3, listaEnt4])

            return array2

        def minimo():
            # print('Hola Mundo')
            elemMinimo = convertirArray().min()
            resultado.set(elemMinimo)

        def maximo():
            elemMaximo = convertirArray().max()
            resultado.set(elemMaximo)

        def suma():
            sumaTotal = convertirArray().sum()
            resultado.set(sumaTotal)

        def sumaFilas():

            sumaFilas = convertirArray().sum(axis=1)
            resultado.set(sumaFilas)

        def sumaColumnas():
            sumaColumnas = convertirArray().sum(axis=0)
            resultado.set(sumaColumnas)

        def matrizDiagonal():
            array2 = convertirArray()
            dim = array2.shape
            listDiagonal = []
            if dim[0] == dim[1]:
                for i in range(dim[0]):
                    for j in range(dim[1]):
                        if i == j:
                            listDiagonal.insert(i, array2[i][j])
            arrayDiagonal = np.array(listDiagonal)
            resultado.set(arrayDiagonal)

        def sumaDiagonal():
            array2 = convertirArray()
            dim = array2.shape
            suma = 0
            if dim[0] == dim[1]:
                for i in range(dim[0]):
                    for j in range(dim[1]):
                        if i == j:
                            suma += array2[i][j]
            resultado.set(suma)

        def limpiar():
            entrada_usuario1.set('')
            entrada_usuario2.set('')
            entrada_usuario3.set('')
            entrada_usuario4.set('')
            resultado.set('')

            # print('Hola Mundo')

        def rellenar():
            entrada_usuario1.set('17,32,58,151')
            entrada_usuario2.set('30,592,753,896')
            entrada_usuario3.set('81,123,159,389')
            entrada_usuario4.set('97,324,159,157')

        # Label
        lblconjuntoA = tk.Label(self, text="Matriz", font=(
            "Roboto", 14, "bold"), bg="#258BED", fg="black")
        lblconjuntoA.grid(row=3, column=1, pady=20)

        # Entrada1
        entryFila1 = ttk.Entry(
            self, textvariable=entrada_usuario1, width=25, font=("Roboto Cn", 20))
        entryFila1.grid(row=4, column=1, padx=10)

        # Entrada 2
        entryFila2 = ttk.Entry(
            self, textvariable=entrada_usuario2, width=25, font=("Roboto Cn", 20))
        entryFila2.grid(row=5, column=1, padx=10)

        # Entrada 3
        entryFila3 = ttk.Entry(
            self, textvariable=entrada_usuario3, width=25, font=("Roboto Cn", 20))
        entryFila3.grid(row=6, column=1, padx=10)

        # Entrada 4
        entryFila4 = ttk.Entry(
            self, textvariable=entrada_usuario4, width=25, font=("Roboto Cn", 20))
        entryFila4.grid(row=7, column=1, padx=10)

        # Label
        lblMatriz = tk.Label(self, text="Resultado", font=(
            "Roboto", 14, "bold"), bg="#258BED", fg="black")
        lblMatriz.grid(row=8, column=1, pady=20)

        # Caja resultado
        boxresultado = ttk.Entry(
            self, textvariable=resultado, width=25, font=("Roboto Cn", 20))
        boxresultado.grid(row=9, column=1, padx=10, pady=20)

        # Botones
        btnMinimo = ttk.Button(self, text="Elemento Mínimo", command=minimo)
        btnMinimo.grid(row=4, column=2, pady=20, padx=20)

        btnMaximo = ttk.Button(
            self, text="Elemento Máximo", command=maximo)
        btnMaximo.grid(row=4, column=3, pady=20, padx=20)

        btnSumaTotal = ttk.Button(self, text="Suma Total", command=suma)
        btnSumaTotal.grid(row=5, column=2, pady=20, padx=20)

        btnSumFilas = ttk.Button(
            self, text="Suma de Filas", command=sumaFilas)
        btnSumFilas.grid(row=5, column=3, pady=20, padx=20)

        btnSumColumnas = ttk.Button(
            self, text="Suma de Columnas", command=sumaColumnas)
        btnSumColumnas.grid(row=6, column=2, pady=20, padx=20)

        btnDiagonal = ttk.Button(
            self, text="Matriz diagonal", command=matrizDiagonal)
        btnDiagonal.grid(row=6, column=3, pady=20, padx=20)

        btnSumDiagonal = ttk.Button(
            self, text="Suma diagonal", command=sumaDiagonal)
        btnSumDiagonal.grid(row=7, column=2, pady=20, padx=20)

        btnAleatorio = ttk.Button(
            self, text="Rellenar Aleatorio", command=rellenar)
        btnAleatorio.grid(row=7, column=3, pady=20, padx=20)

        btnLimpiar = ttk.Button(self, text="Limpiar", command=limpiar)
        btnLimpiar.grid(row=9, column=2, pady=20, padx=20)

        btnMenu = ttk.Button(self, text="Menú",
                             command=lambda: controller.show_frame(Frame_1))
        btnMenu.grid(row=9, column=3, pady=20, padx=20)

# Listas simples


class Frame_4(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="#258BED")

        # Creación del objeto lista
        listaSimple = Linkedlist()
        entrada_usuario1 = tk.StringVar()
        entrada_usuario2 = tk.StringVar()

        resultado = tk.StringVar()

        def insertarPrimerPos():
            listaSimple.insertarPrimerPos(int(entrada_usuario1.get()))
            resultado.set(listaSimple)

            # limpiar()

        def insertarUltimaPos():
            listaSimple.insertarUltimaPos(entrada_usuario1.get())
            resultado.set(listaSimple)

            # limpiar()

        def insertarDespuesNodoBuscado():
            listaSimple.insertarDespuesNodoBuscado(
                entrada_usuario1.get(), entrada_usuario2.get())
            resultado.set(listaSimple)

            # limpiar()

        def eliminar():
            listaSimple.eliminar(entrada_usuario1.get())
            resultado.set(listaSimple)

            limpiar()

        def limpiar():
            entrada_usuario1.set('')
            entrada_usuario2.set('')

        # Label
        lblconjuntoA = tk.Label(self, text="Operaciones con listas simples", font=(
            "Roboto", 16, "bold"), bg="#258BED", fg="black")
        lblconjuntoA.grid(row=0, column=1, pady=20)

        # Label
        lblconjuntoA = tk.Label(self, text="Ingrese Dato:", font=(
            "Roboto", 14, "bold"), bg="#258BED", fg="black")
        lblconjuntoA.grid(row=1, column=1, padx=10, pady=10)

        # Dato
        entryFila1 = ttk.Entry(
            self, textvariable=entrada_usuario1, width=25, font=("Roboto Cn", 20))
        entryFila1.grid(row=2, column=1, padx=10)

        # Label
        lblconjuntoA = tk.Label(self, text="Ingrese el dato a buscar:", font=(
            "Roboto", 16, "bold"), bg="#258BED", fg="black")
        lblconjuntoA.grid(row=3, column=1, pady=10)

        # Dato a buscar
        entryFila1 = ttk.Entry(
            self, textvariable=entrada_usuario2, width=25, font=("Roboto Cn", 20))
        entryFila1.grid(row=4, column=1, padx=10)

        # Label resultado
        lblconjuntoA = tk.Label(self, text="Resultado:", font=(
            "Roboto", 16, "bold"), bg="#258BED", fg="black")
        lblconjuntoA.grid(row=5, column=1, pady=20)

        # Caja resultado
        boxresultado = ttk.Entry(
            self, textvariable=resultado, width=25, font=("Roboto Cn", 20))
        boxresultado.grid(row=6, column=1, padx=10)

        # Botones
        btnInsertarPrimero = ttk.Button(
            self, text="Insertar primero", command=insertarPrimerPos)
        btnInsertarPrimero.grid(row=1, column=2, padx=20)

        btnInsertarUltimo = ttk.Button(
            self, text="Insertar último", command=insertarUltimaPos)
        btnInsertarUltimo.grid(row=1, column=3, padx=20)

        btnInsertarDespues = ttk.Button(
            self, text="Insertar (dato)", command=insertarDespuesNodoBuscado)
        btnInsertarDespues.grid(row=2, column=2, padx=20)

        btnEliminar = ttk.Button(
            self, text="Eliminar", command=eliminar)
        btnEliminar.grid(row=2, column=3, padx=20)

        btnMenu = ttk.Button(self, text="Menú",
                             command=lambda: controller.show_frame(Frame_1))
        btnMenu.grid(row=4, column=3, padx=20)


class Frame_5(tk.Frame):

    tam = 10
    # Posicion del rectangulo
    x0 = 120
    y0 = 200
    x1 = 220
    y1 = 220

    pila = None
    figuras = None

    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="#258BED")

        pila = Pila(self.tam)

        self.canvas = tk.Canvas(
            self,
            width=300,
            height=220,
            background='white'
        )
        self.canvas.grid(row=3, column=1, sticky='n')

        frame = tk.Frame(self)
        frame.grid(row=0, column=0, sticky='n')

        def push():
            # print('hiciste clic en push')
            if pila.llena():
                # ALERTA
                return
            else:
                rand1 = randint(10, 99)
                rand2 = randint(10, 99)
                pila.push(self.canvas.create_rectangle(
                    self.x0, self.y0, self.x1, self.y1,
                    fill="#" + str(rand1) + "ff" + str(rand2)
                ))
                self.y0 -= 20
                self.y1 -= 20

        def pop():
            # print('Hiciste clic en pop')
            if pila.vacia():
                # ALERTA
                return
            else:
                figura = pila.pop()
                self.canvas.delete(figura)
                self.y0 += 20
                self.y1 += 20

        # Label
        lblconjuntoA = tk.Label(self, text="Pilas", font=(
            "Roboto", 14, "bold"), bg="#258BED", fg="black")
        lblconjuntoA.grid(row=0, column=1, pady=20)

        # Botones
        btnPush = ttk.Button(self, text="Push", command=push)
        btnPush.grid(row=1, column=0, pady=5, padx=20)

        btnPop = ttk.Button(
            self, text="Pop", command=pop)
        btnPop.grid(row=2, column=0, pady=5, padx=20)

        btnMenu = ttk.Button(self, text="Menú",
                             command=lambda: controller.show_frame(Frame_1))
        btnMenu.grid(row=4, column=2, pady=10, padx=20)


class Frame_6(tk.Frame):

    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="#258BED")

        # Creación del objeto cola
        nuevaCola = Cola()

        entrada_usuario1 = tk.StringVar()

        resultado = tk.StringVar()

        def encolar():
            nuevaCola.encolar(int(entrada_usuario1.get()))
            resultado.set(nuevaCola)

        def desencolar():
            nuevaCola.desencolar()
            resultado.set(nuevaCola)

        # Label
        lblconjuntoA = tk.Label(self, text="Colas", font=(
            "Roboto", 14, "bold"), bg="#258BED", fg="black")
        lblconjuntoA.grid(row=0, column=1, pady=20)

        # Botones
        btnEncolar = ttk.Button(self, text="Encolar", command=encolar)
        btnEncolar.grid(row=1, column=0, pady=5, padx=20)

        # Entrada1
        entryFila1 = ttk.Entry(
            self, textvariable=entrada_usuario1, width=25, font=("Roboto Cn", 20))
        entryFila1.grid(row=1, column=1, padx=10)

        btnDesencolar = ttk.Button(
            self, text="Desencolar", command=desencolar)
        btnDesencolar.grid(row=2, column=0, pady=5, padx=20)

        # Label resultado
        lblResultado = tk.Label(self, text="Resultado:", font=(
            "Roboto", 16, "bold"), bg="#258BED", fg="black")
        lblResultado.grid(row=3, column=1, pady=20)

        # Caja resultado
        boxresultado = ttk.Entry(
            self, textvariable=resultado, width=25, font=("Roboto Cn", 20))
        boxresultado.grid(row=4, column=1, padx=10)

        btnMenu = ttk.Button(self, text="Menú",
                             command=lambda: controller.show_frame(Frame_1))
        btnMenu.grid(row=5, column=2, pady=10, padx=20)


root = App()

root.mainloop()
