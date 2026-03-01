import json
from producto import Producto
# Clase Inventario
def guardar_archivo(self):
    with open("inventario.txt", "w", encoding="utf-8") as archivo:
        json.dump(
            {id: p.to_dict() for id, p in self.productos.items()},
            archivo,
            indent=4
        )
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario {id: Producto}

    # Añadir producto
    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("⚠️ El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("✅ Producto añadido correctamente.")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑 Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("🔄 Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    # Buscar por nombre
    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron productos.")

    # Mostrar todos
    def mostrar_todos(self):
        if not self.productos:
            print("📦 Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    # Guardar en archivo
    def guardar_archivo(self, nombre_archivo="inventario.txt"):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(
                {id: p.to_dict() for id, p in self.productos.items()},
                archivo,
                indent=4
            )
        print("💾 Inventario guardado correctamente.")

    # Cargar desde archivo
    def cargar_archivo(self, nombre_archivo="inventario.txt"):
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read().strip()

                if not contenido:
                    print("📂 Archivo vacío. No hay datos para cargar.")
                    return

                datos = json.loads(contenido)

                for id, info in datos.items():
                    producto = Producto(
                        info["id"],
                        info["nombre"],
                        info["cantidad"],
                        info["precio"]
                    )
                    self.productos[id] = producto

            print("📂 Inventario cargado correctamente.")

        except FileNotFoundError:
            print("⚠ No existe archivo previo. Se creará uno al guardar.")