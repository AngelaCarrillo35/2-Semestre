from producto import Producto
import os

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # CARGAR PRODUCTOS DESDE ARCHIVO
    
    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                # Si el archivo no existe, lo crea
                open(self.archivo, "w").close()
                return

            with open(self.archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        producto = Producto(
                            datos[0],
                            datos[1],
                            int(datos[2]),
                            float(datos[3])
                        )
                        self.productos.append(producto)

        except FileNotFoundError:
            print("Error: Archivo no encontrado.")
        except PermissionError:
            print("Error: No tiene permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar archivo: {e}")

    # ===============================
    # GUARDAR PRODUCTOS EN ARCHIVO
    # ===============================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos:
                    f.write(str(producto) + "\n")

        except PermissionError:
            print("Error: No tiene permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar archivo: {e}")

    # ===============================
    # MÉTODOS DE INVENTARIO
    # ===============================
    def añadir_producto(self, producto):
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado correctamente y guardado en archivo.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print("Producto eliminado correctamente.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad, nuevo_precio):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                producto.cantidad = nueva_cantidad
                producto.precio = nuevo_precio
                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                print(producto)
                return
        print("Producto no encontrado.")

    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos:
                print(producto)