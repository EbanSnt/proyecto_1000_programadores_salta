from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import sys
import sqlite3

from base_de_datos import BaseDatos


class Administrador:
    def __init__(self):
        self.principal()

    def principal(self):
        # Cofiguracion de ventana
        self.ventana = Tk()
        self.height = self.ventana.winfo_screenheight()
        self.width = self.ventana.winfo_screenwidth()
        self.ventana.geometry("%dx%d" % (self.width, self.height))
        self.ventana.resizable(False, False)
        self.ventana.config(background="#fff")

        # contenedores
        self.contenedor_tabla = Frame(self.ventana, background="#8DEEF7")
        self.contenedor_tabla.place(relx=0.03, rely=0.05, relwidth=0.7, relheight=0.6)

        self.contenedor_entry = Frame(self.ventana, background="#DFDFDF")
        self.contenedor_entry.place(relx=0.75, rely=0.05, relwidth=0.22, relheight=0.6)

        self.contenedor_tabla_ventas = Frame(self.ventana,background="black")
        self.contenedor_tabla_ventas.place(relx=0.05,rely=0.67,relheight=0.25,relwidth=0.4)

        # Label y Entry para el ingreso de productos
        self.cartel_label = Label(self.contenedor_entry, text="ENVIOS/ACTUALIZACION \nDE DATOS",font=("Verdana",12),fg="red").place(relx=0.08, rely=0.05)


        self.producto_label = Label(self.contenedor_entry, text="PRODUCTO").place(relx=0.08, rely=0.15)
        self.producto_entry = Entry(self.contenedor_entry)
        self.producto_entry.place(relx=0.08, rely=0.2)

        self.marca_label = Label(self.contenedor_entry, text="MARCA").place(relx=0.08, rely=0.25)
        self.marca_entry = Entry(self.contenedor_entry)
        self.marca_entry.place(relx=0.08, rely=0.3)

        self.seccion_label = Label(self.contenedor_entry, text="SECCION").place(relx=0.08, rely=0.35)
        # self.valores_seccion = (" ","Comida","Limpieza","Higiene","Deportes","Libreria","Tecnologia","Hogar","Otros")
        self.seccion_entry = Entry(self.contenedor_entry)
        self.seccion_entry.place(relx=0.08, rely=0.4)

        self.precio_label = Label(self.contenedor_entry, text="PRECIO").place(relx=0.08, rely=0.45)
        self.precio_entry = Entry(self.contenedor_entry)
        self.precio_entry.place(relx=0.08, rely=0.5)

        self.stock_label = Label(self.contenedor_entry, text="STOCK").place(relx=0.08, rely=0.55)
        self.stock_entry = Entry(self.contenedor_entry)
        self.stock_entry.place(relx=0.08, rely=0.6)

        self.descripcion_label = Label(self.contenedor_entry, text="DESCRIPCION").place(relx=0.08, rely=0.65)
        self.descripcion_entry = Entry(self.contenedor_entry)
        self.descripcion_entry.place(relx=0.08, rely=0.7)

        # Botones del contenedor Entry
        self.enviar_boton = Button(self.contenedor_entry, text="ENVIAR", command=self.enviar_datos,width=10,height=2,fg="white",bg="green").place(relx=0.65,rely=0.7)
        self.refrescar_pantalla_boton = Button(self.contenedor_entry, text="ACTUALIZAR",width=10,height=2,fg="white",bg="black").place(relx=0.65,rely=0.85)# Revisar estilos y tamaño
        self.actualizar_datos_boton = Button(self.contenedor_entry, text="REFRESCAR PAG",command=self.refrescar, width=15,height=2, fg="white", bg="red").place(relx=0.20, rely=0.85)

        # Creacion de la tabla principal (productos)
        self.tabla = ttk.Treeview(self.contenedor_tabla, height=20,
                                  columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7"))
        self.tabla.place(relx=0, rely=0)

        self.tabla.column("#1", width=120, anchor=CENTER)
        self.tabla.column("#2", width=120, anchor=CENTER)
        self.tabla.column("#3", width=120, anchor=CENTER)
        self.tabla.column("#4", width=120, anchor=CENTER)
        self.tabla.column("#5", width=120, anchor=CENTER)
        self.tabla.column("#6", width=120, anchor=CENTER)
        self.tabla.column("#7", width=174, anchor=CENTER)

        self.tabla["show"] = "headings"
        self.tabla.heading("#1", text="CODIGO", anchor=CENTER)
        self.tabla.heading("#2", text="PRODUCTO", anchor=CENTER)
        self.tabla.heading("#3", text="MARCA", anchor=CENTER)
        self.tabla.heading("#4", text="SECCION", anchor=CENTER)
        self.tabla.heading("#5", text="PRECIO", anchor=CENTER)
        self.tabla.heading("#6", text="STOCK", anchor=CENTER)
        self.tabla.heading("#7", text="DESCRIPCION", anchor=CENTER)

        # Introducir los valores en la tabla de productos
        self.base_de_datos = BaseDatos()
        self.base_de_datos.crear_base_productos()
        self.conexion = sqlite3.connect("./base_datos/productos.db")
        self.cursor = self.conexion.cursor()
        self.insertar = self.cursor.execute("SELECT * FROM PRODUCTOS")
        for dato in self.insertar:
            self.tabla.insert('', 0, values=(dato[0], dato[1], dato[2], dato[3], dato[4],
                                             dato[5], dato[6],))
        self.conexion.commit()
        self.conexion.close()

        self.ventana.mainloop()

    # Creacion de tabla de ventas realizadas

        self.tabla_ventas = ttk.Treeview(self.contenedor_tabla_ventas, height=20,
                                  columns=("#1", "#2", "#3", "#4", "#5"))
        self.tabla_ventas.place(relx=0, rely=0)

        self.tabla_ventas.column("#1", width=40, anchor=CENTER)
        self.tabla_ventas.column("#2", width=40, anchor=CENTER)
        self.tabla_ventas.column("#3", width=40, anchor=CENTER)
        self.tabla_ventas.column("#4", width=40, anchor=CENTER)
        self.tabla_ventas.column("#5", width=40, anchor=CENTER)

        self.tabla_ventas["show"] = "headings"
        self.tabla_ventas.heading("#1", text="VENTA", anchor=CENTER)
        self.tabla_ventas.heading("#2", text="DNI", anchor=CENTER)
        self.tabla_ventas.heading("#3", text="NOMBRE", anchor=CENTER)
        self.tabla_ventas.heading("#4", text="APELLIDO", anchor=CENTER)
        self.tabla_ventas.heading("#5", text="MONTO", anchor=CENTER)


    # Funcion para validar que no halla campos vacios en los entry antes de enviar
    def validacion_datos(self):
        return not self.producto_entry.get() or not self.marca_entry.get() or not self.seccion_entry.get() \
               or not self.precio_entry.get() or not self.stock_entry.get() or not self.descripcion_entry.get()

    # Funcion para enviar los datos de los entry a la base de datos
    def enviar_datos(self):
        if self.validacion_datos() == True:
            messagebox.showerror("AVISO", "Debe completar todos los campos")
        else:
            self.base_de_datos.insertar_datos_productos(self.producto_entry.get(),
                                                        self.marca_entry.get(),
                                                        self.seccion_entry.get(), self.precio_entry.get(),
                                                        self.stock_entry.get(), self.descripcion_entry.get())
            self.producto_entry.delete(0, END)
            self.marca_entry.delete(0, END)
            self.seccion_entry.delete(0, END)
            self.precio_entry.delete(0, END)
            self.stock_entry.delete(0, END)
            self.descripcion_entry.delete(0, END)

            messagebox.showinfo("AVISO", "Los datos se enviaron exitosamente")
    # Funcion para refrescar la pagina y actualizar los datos
    def refrescar(self):
        self.ventana.destroy()
        Administrador()




Administrador()
