from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
# comentario de prueba
class App(tk.Tk):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        # Configuración inicial

        self.configure(bg='black')
        font.nametofont('TkDefaultFont').configure(size=12,underline=True)
        self.title('Proyecto Estructura de Datos')
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        # self.geometry('1200x720')

        # Contenedor principal 
        contenedor_principal = tk.Frame(self,bg='#258BED')
        contenedor_principal.grid(row=0, column=0,columnspan=3,padx=20,pady=20)

        # Diccionario de Frames
        self.todos_los_frames = dict()

        for F in (Frame_1, Frame_2,Frame_3):

            frame = F(contenedor_principal, self)
            self.todos_los_frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(Frame_1)
    
    def show_frame(self, contenedor_llamado):
        frame = self.todos_los_frames[contenedor_llamado]
        frame.tkraise()

class Frame_1(tk.Frame):
    def __init__(self,container,controller,*args,**kwargs):
        super().__init__(container,*args,**kwargs)
        
        # Configuraión inicial
        self.configure(bg='#258BED')
        self.entrada_usuario = tk.StringVar()


        # Label
        titulo = tk.Label(self, text="Proyecto Final de Estructura de Datos", font=(
             "Roboto",36, "bold"), bg="#258BED", fg="black")

        titulo.grid(row=10, column=2, columnspan=40, padx=20,pady=20,sticky="n")

        estudiante = tk.Label(self, text="Developed by: ",
                       font=("Roboto", 11), bg="#258BED",fg='black')
        estudiante.grid(row=15, column=3, sticky="w")

        nombre = tk.Label(self, text="Víktor López Amiquero",
                       font=("Roboto", 10), bg="#258BED",fg='black')
        nombre.grid(row=18, column=3, sticky="w")


        #Button
        btnConjunto = ttk.Button(self, text="Conjuntos" , command = lambda:controller.show_frame( Frame_2 ))

        btnConjunto.grid(row=20, column=2,pady=50, sticky="e")

        #buton matrices
        btnConjunto = ttk.Button(self, text="Matrices" , command = lambda:controller.show_frame( Frame_3 ))

        btnConjunto.grid(row=20, column=3,pady=50,padx=20, sticky="e")

class Frame_2(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="#258BED")
         
        entrada_usuario = tk.StringVar()
        entrada_usuario2 = tk.StringVar()
        resultado = tk.StringVar()

        def union():
            listaA =  str(entrada_usuario.get()).split(',')       
            listaB = str(entrada_usuario2.get()).split(',')

            conjUnion = set(listaA+listaB)
            resultado.set(conjUnion)

        
        def interseccion():
            listaA = str(entrada_usuario.get()).split(',') 
            listaB = str(entrada_usuario2.get()).split(',')
            
            conjInterseccion = []
            for i in listaA:
                if i in listaB: conjInterseccion.append(i)
            
            resultado.set(set(conjInterseccion))
            if not conjInterseccion: resultado.set('No existe intersección')
                
        
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
        lblconjuntoA.grid(row=3, column=4, columnspan=20, sticky="n",pady=20)
        entryConjA = ttk.Entry(self, textvariable=entrada_usuario,width=50,font=("Roboto Cn",20))
        entryConjA.grid(row=4, columnspan=20, padx=(10, 20))

        
        lblconjuntoB = tk.Label(self, text="Conjunto B", font=(
            "Roboto", 14, 'bold'), bg="#258BED")
        lblconjuntoB.grid(row=5, column=4,columnspan=20, sticky="n",pady=20)

        entryConjB = ttk.Entry(self,textvariable=entrada_usuario2,width=50,font=("Roboto Cn",20))
        entryConjB.grid(row=6,column = 4, columnspan=20,padx=(10,20))

        lblconjuntoC = tk.Label(self, text="Resultado", font=(
            "Roboto", 14, 'bold'), bg="#258BED")
        lblconjuntoC.grid(row=7, column=4,columnspan=20, sticky="n",pady=20)

        boxresultado = ttk.Entry(self,textvariable=resultado,width=50,font=("Roboto Cn",20))
        boxresultado.grid(row=8,column = 4, columnspan=20,padx=(10,20))
        
        btnUnion = ttk.Button(self, text="Unión",command=union)
        btnUnion.grid(row=10,column=4,pady=20,padx=20)

        btnInterseccion = ttk.Button(self, text="Intersección",command=interseccion)
        btnInterseccion.grid(row=10,column=5,pady=20,padx=20)

        btndiferencia = ttk.Button(self, text="Diferencia",command=diferencia)
        btndiferencia.grid(row=10,column=6,pady=20,padx=20)

        btnDifSimetrica = ttk.Button(self, text="Dif. Simétrica",command=diferenciaSimetrica)
        btnDifSimetrica.grid(row=10,column=7,pady=20,padx=20)

        btnLimpiar = ttk.Button(self, text="Limpiar",command=limpiar)
        btnLimpiar.grid(row=10,column=8,pady=20,padx=20)

        btnMenu = ttk.Button(self, text="Menú",
                            command=lambda: controller.show_frame(Frame_1))
        btnMenu.grid(row=10, column=9,pady=20,padx=20)

class Frame_3(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="#258BED")
         
        entrada_usuario = tk.StringVar()
        entrada_usuario2 = tk.StringVar()
        resultado = tk.StringVar()

        def union():
            listaA =  str(entrada_usuario.get()).split(',')       
            listaB = str(entrada_usuario2.get()).split(',')

            conjUnion = set(listaA+listaB)
            resultado.set(conjUnion)

        
        def interseccion():
            listaA = str(entrada_usuario.get()).split(',') 
            listaB = str(entrada_usuario2.get()).split(',')
            
            conjInterseccion = []
            for i in listaA:
                if i in listaB: conjInterseccion.append(i)
            
            resultado.set(set(conjInterseccion))
            if not conjInterseccion: resultado.set('No existe intersección')
                
        
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
        lblconjuntoA = tk.Label(self, text="Campo Matrices", font=(
            "Roboto", 14, "bold"), bg="#258BED", fg="black")
        lblconjuntoA.grid(row=3, column=4, columnspan=20, sticky="n",pady=20)
        entryConjA = ttk.Entry(self, textvariable=entrada_usuario,width=50,font=("Roboto Cn",20))
        entryConjA.grid(row=4, columnspan=20, padx=(10, 20))

        
        lblconjuntoB = tk.Label(self, text="Conjunto B", font=(
            "Roboto", 14, 'bold'), bg="#258BED")
        lblconjuntoB.grid(row=5, column=4,columnspan=20, sticky="n",pady=20)

        entryConjB = ttk.Entry(self,textvariable=entrada_usuario2,width=50,font=("Roboto Cn",20))
        entryConjB.grid(row=6,column = 4, columnspan=20,padx=(10,20))

        lblconjuntoC = tk.Label(self, text="Resultado", font=(
            "Roboto", 14, 'bold'), bg="#258BED")
        lblconjuntoC.grid(row=7, column=4,columnspan=20, sticky="n",pady=20)

        boxresultado = ttk.Entry(self,textvariable=resultado,width=50,font=("Roboto Cn",20))
        boxresultado.grid(row=8,column = 4, columnspan=20,padx=(10,20))
        
        btnUnion = ttk.Button(self, text="Unión",command=union)
        btnUnion.grid(row=10,column=4,pady=20,padx=20)

        btnInterseccion = ttk.Button(self, text="Intersección",command=interseccion)
        btnInterseccion.grid(row=10,column=5,pady=20,padx=20)

        btndiferencia = ttk.Button(self, text="Diferencia",command=diferencia)
        btndiferencia.grid(row=10,column=6,pady=20,padx=20)

        btnDifSimetrica = ttk.Button(self, text="Dif. Simétrica",command=diferenciaSimetrica)
        btnDifSimetrica.grid(row=10,column=7,pady=20,padx=20)

        btnLimpiar = ttk.Button(self, text="Limpiar",command=limpiar)
        btnLimpiar.grid(row=10,column=8,pady=20,padx=20)

        btnMenu = ttk.Button(self, text="Menú",
                            command=lambda: controller.show_frame(Frame_1))
        btnMenu.grid(row=10, column=9,pady=20,padx=20)
        


root = App()

root.mainloop()