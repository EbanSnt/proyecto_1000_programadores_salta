from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import sys

class VentanaInicio:
    def __init__(self):
        self.ventana_inicio()
    def ventana_inicio(self):
        # Configuracion de ventana
        self.ventana = Tk()
        self.ventana.geometry("400x400")
        self.ventana.title("SuperMarket")
        self.ventana.resizable(False,False)
        self.ventana.config(background="#fff")
        #self.ventana.iconbitmap("favicon.ico")
        self.imagen = Image.open("./imagenes/carrito_logo.png")
        self.imagen = self.imagen.resize((200,200))
        self.imagen_inicio = ImageTk.PhotoImage(self.imagen)
        Label(self.ventana,image=self.imagen_inicio).place(x=100,y=30)

        # Logo de 1000 programadores salteños
        self.logo_1000 = Image.open("./imagenes/logo_inicio.jpg")
        self.logo_1000 = self.logo_1000.resize((50, 50))
        self.logo_1000_inicio = ImageTk.PhotoImage(self.logo_1000)
        Label(self.ventana, image=self.logo_1000_inicio).place(x=330, y=320)

        # BOTONES
            # Boton para entrar a la ventana de usuario
        self.boton_consumidor = ttk.Button(self.ventana,text="USUARIO")
        self.boton_consumidor.place(x=100,y=250,height=50)
            # Boton para entrar a la ventana de administrador
        self.boton_administrador = ttk.Button(self.ventana, text="ADMINISTRADOR")
        self.boton_administrador.place(x=220, y=250, height=50)
        # Boton para salir y cerrar la ventana
        self.boton_salir = ttk.Button(self.ventana, text="SALIR", command=self.salir)
        self.boton_salir.place(x=30, y=340, height=50)

        # Derechos de Autor
        Label(self.ventana,text="Creado por Esteban Santillan ©").place(x=220,y=370)

        self.ventana.mainloop()

    def salir(self):
        sys.exit()
    def siguiente(self):
        pass  #REVISAR

VentanaInicio()