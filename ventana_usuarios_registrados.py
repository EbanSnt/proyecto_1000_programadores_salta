from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import sys
import sqlite3
from base_de_datos import BaseDatos
class UsuariosRegistrados:
    def __init__(self):
        self.principal()
    def principal(self):
        self.ventana = Tk()
        self.ventana.geometry("600x400")
        self.ventana.resizable(False, False)
        self.ventana.config(background="#fff")

        # Contenedor de tabla
        self.contenedor_tabla = Frame(self.ventana, background="#8DEEF7")
        self.contenedor_tabla.place(x=10,y=10,height=350,width=350)
        # Configuracion de la tabla
        self.tabla = ttk.Treeview(self.contenedor_tabla, height=15,
                                  columns=("#1", "#2", "#3", "#4"))
        self.tabla.place(relx=0, rely=0)

        self.tabla.column("#1", width=65, anchor=CENTER)
        self.tabla.column("#2", width=90, anchor=CENTER)
        self.tabla.column("#3", width=90, anchor=CENTER)
        self.tabla.column("#4", width=90, anchor=CENTER)

        self.tabla["show"] = "headings"
        self.tabla.heading("#1", text="CLIENTE", anchor=CENTER)
        self.tabla.heading("#2", text="DNI", anchor=CENTER)
        self.tabla.heading("#3", text="NOMBRE", anchor=CENTER)
        self.tabla.heading("#4", text="APELLIDO", anchor=CENTER)

        # Insercion de datos en la tabla
        self.base = BaseDatos()
        self.base.crear_base_clientes()
        self.conexion = sqlite3.connect("./base_datos/clientes.db")
        self.cursor = self.conexion.cursor()
        self.insertar = self.cursor.execute("SELECT * FROM CLIENTES")
        for dato in self.insertar:
            self.tabla.insert('', 0, values=(dato[0], dato[1], dato[2], dato[3]))
        self.conexion.commit()
        self.conexion.close()


        # Tomar los valores de la tabla, en donde el usuario haya hecho clic
    def valores(self):
        self.seleccion = self.tabla.focus()
        self.detalles = self.tabla.item(self.seleccion)
        self.valor1 = self.detalles.get("values")[0]
        self.valor2 = self.detalles.get("values")[1]
        self.valor3 = self.detalles.get("values")[2]
        self.valor4 = self.detalles.get("values")[3]





        self.ventana.mainloop()



UsuariosRegistrados()