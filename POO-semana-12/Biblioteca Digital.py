# Sistema de Gestión de Biblioteca Digital

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para datos que no cambiarán
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def mostrar_info(self):
        titulo, autor = self.info
        return f"Título: {titulo}, Autor: {autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para libros prestados
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros(self):
        if not self.libros_prestados:
            print("No tiene libros prestados.")
        else:
            for libro in self.libros_prestados:
                print(libro.mostrar_info())

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        # Diccionario para libros
        self.libros = {}
        # Diccionario para usuarios
        self.usuarios = {}
        # Conjunto para IDs únicos
        self.ids_usuarios = set()

    # Añadir libro
    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        print("Libro añadido correctamente.")

    # Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado.")
        else:
            print("El ID de usuario ya existe.")

    # Dar de baja usuario
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # Prestar libro
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            del self.libros[isbn]
            print("Libro prestado correctamente.")
        else:
            print("Usuario o libro no encontrado.")

    # Devolver libro
    def devolver_libro(self, id_usuario, libro):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            usuario.devolver_libro(libro)
            self.libros[libro.isbn] = libro
            print("Libro devuelto correctamente.")
        else:
            print("Usuario no encontrado.")

    # Buscar libro
    def buscar_libro(self, texto):
        encontrados = []
        for libro in self.libros.values():
            titulo, autor = libro.info
            if texto.lower() in titulo.lower() or texto.lower() in autor.lower() or texto.lower() in libro.categoria.lower():
                encontrados.append(libro)

        if encontrados:
            for libro in encontrados:
                print(libro.mostrar_info())
        else:
            print("No se encontraron libros.")

# ------------------- PRUEBA DEL SISTEMA -------------------

# Crear biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "111")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Ficción", "222")

# Añadir libros
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Crear usuario
usuario1 = Usuario("Juan", "U001")

# Registrar usuario
biblioteca.registrar_usuario(usuario1)

# Prestar libro
biblioteca.prestar_libro("U001", "111")

# Ver libros prestados
usuario1.listar_libros()

# Buscar libro
biblioteca.buscar_libro("Principito")