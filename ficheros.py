from ventana_usuarios_registrados import UsuariosRegistrados
from base_de_datos import BaseDatos
import sqlite3
class Ficheros:

    def consulta_compras_clientes(self):
        self.usuarios = UsuariosRegistrados()
        # Obtencion de datos:
        dni = self.usuarios.valor2
        apellido = self.usuarios.valor3
        nombre = self.usuarios.valor4
        # Consultar fichero
        self.fichero = open(f"./historial_ventas_usuarios/{dni}_{apellido}_{nombre}","r")
        self.consulta = self.fichero.read()
        self.fichero.close()

    def escrituras_ficheros_ventas(self,dni,apellido,nombre):
        self.base = BaseDatos()
        self.conexion = sqlite3.connect("./base_datos/ventas.db")
        self.cursor = self.conexion.cursor()
        datos = self.cursor.execute(f"SELECT * FROM COMICS WHERE DNI = {dni}")
        self.fichero_nuevo = open(f"./historial_ventas_usuarios/{dni}_{apellido}_{nombre}","a")
        self.fichero_nuevo.write(f"""FECHA: \n
            
                                                    
                                                    
                                                    
                                                    
                                                    """)

        self.conexion.commit()
        self.conexion.close()

# ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                 DNI INTEGER,
#                 NOMBRE TEXT,
#                 APELLIDO TEXT,
#                 MONTO REAL