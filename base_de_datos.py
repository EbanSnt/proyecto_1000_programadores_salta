import sqlite3

class BaseDatos:

    # CREACION DE BASES DE DATOS
    def crear_base_productos(self):  # Aqui se alamacenaran el stock del producto
        self.conexion = sqlite3.connect("./base_datos/productos.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS PRODUCTOS (
        CODIGO INTEGER,
        PRODUCTO TEXT,
        MARCA TEXT,
        SECCION TEXT,
        PRECIO REAL,
        STOCK INTEGER,
        DESCRIPCION TEXT)""")
        self.conexion.commit()
        self.conexion.close()

    def crear_base_clientes(self):  # Aqui se veran los clientes registrados
        self.conexion = sqlite3.connect("./base_datos/clientes.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS CLIENTES (
        DNI INTEGER,
        NOMBRE TEXT,
        APELLIDO TEXT,
        PASSWORDS TEXT)""")
        self.conexion.commit()
        self.conexion.close()

    def crear_base_ventas(self):  # Aqui se vera a todos las ventas realizadas, juntos con sus usuarios
        self.conexion = sqlite3.connect("./base_datos/ventas.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS VENTAS (
        VENTAS INTEGER PRIMARY KEY AUTOINCREMENT,
        DNI INTEGER,
        NOMBRE TEXT,
        APELLIDO TEXT,
        MONTO REAL)""")
        self.conexion.commit()
        self.conexion.close()

    def crear_base_compras(self):  # Sirve como historial de compras, para cada usuario registrado. Se creara una base por cada uno
        self.conexion = sqlite3.connect("./base_datos/compras.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS COMPRAS (
        COMPRAS INTEGER PRIMARY KEY AUTOINCREMENT,
        DNI INTEGER,
        NOMBRE TEXT,
        APELLIDO TEXT
        )""")
        self.conexion.commit()
        self.conexion.close()


    # FUNCIONES PARA INSERTAR LOS DATOS

    def insertar_datos_productos(self,codigo,producto,marca,seccion,precio,stock,descripcion):
        self.conexion = sqlite3.connect("./base_datos/productos.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute(f"INSERT INTO PRODUCTOS VALUES ({codigo},'{producto}','{marca}','{seccion}'"
                            f",{precio},{stock},'{descripcion}')")
        self.conexion.commit()
        self.conexion.close()

    def insertar_datos_clientes(self,dni,nombre,apellido,passwords):
        self.conexion = sqlite3.connect("./base_datos/clientes.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute(f"INSERT INTO CLIENTES VALUES ({dni},'{nombre}','{apellido}'"
                            f",'{passwords}')")
        self.conexion.commit()
        self.conexion.close()

    def insertar_datos_ventas(self,dni,nombre,apellido,monto):
        self.conexion = sqlite3.connect("./base_datos/ventas.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute(f"INSERT INTO VENTAS VALUES (NULL,{dni},'{nombre}','{apellido}'"
                            f",{monto})")
        self.conexion.commit()
        self.conexion.close()

    def insertar_datos_compras(self,dni,nombre,apellido,monto):
        self.conexion = sqlite3.connect("./base_datos/compras.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute(f"INSERT INTO VENTAS VALUES (NULL,{dni},'{nombre}','{apellido}'"
                            f",{monto})")
        self.conexion.commit()
        self.conexion.close()



    # FUNCIONES PARA ACTUALIZAR LOS DATOS

    def actualizar_datos_productos(self,codigo,producto,marca,seccion,precio,stock,descripcion):
        self.conexion = sqlite3.connect("./base_datos/productos.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM PRODUCTOS")
        self.cursor.execute(f"UPDATE PRODUCTOS"
                            f"SET NOMBRE = {codigo}, SET PRODUCTO = '{producto}', SET MARCA = '{marca}',"
                            f"SET SECCION = '{seccion}', SET PRECIO = {precio}, SET STOCK = {stock}, SET DESCRIPCION = '{descripcion}';")
        self.conexion.commit()
        self.conexion.close()


    def actualizar_datos_clientes(self,dni,nombre,apellido,passwords):
        self.conexion = sqlite3.connect("./base_datos/clientes.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM CLIENTES")
        self.cursor.execute(f"UPDATE CLIENTES"
                            f"SET DNI = {dni}, SET NOMBRE = '{nombre}', SET APELLIDO = '{apellido}',"
                            f"SET SECCION = '{passwords}';")
        self.conexion.commit()
        self.conexion.close()

    def actualizar_datos_compras(self,dni,nombre,apellido):
        self.conexion = sqlite3.connect("./base_datos/compras.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM COMPRAS")
        self.cursor.execute(f"UPDATE COMPRAS"
                            f"SET DNI = {dni}, SET NOMBRE = '{nombre}', SET APELLIDO = '{apellido}';"
                            )
        self.conexion.commit()
        self.conexion.close()

    def actualizar_datos_ventas(self, dni, nombre, apellido,monto):
        self.conexion = sqlite3.connect("./base_datos/ventas.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM VENTAS")
        self.cursor.execute(f"UPDATE VENTAS"
                            f"SET DNI = {dni}, SET NOMBRE = '{nombre}', SET APELLIDO = '{apellido}', SET MONTO = {monto};")
        self.conexion.commit()
        self.conexion.close()




