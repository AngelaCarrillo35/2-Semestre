# Clase Habitacion: representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True  # Indica si la habitación está disponible

    def reservar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True


# Clase Cliente: representa a una persona que reserva una habitación
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre


# Clase Hotel: gestiona las habitaciones y reservas
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    # Agregar habitaciones al hotel
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    # Reservar una habitación disponible
    def reservar_habitacion(self, cliente, tipo):
        for habitacion in self.habitaciones:
            if habitacion.tipo == tipo and habitacion.disponible:
                habitacion.reservar()
                print(f"{cliente.nombre} reservó la habitación {habitacion.numero}")
                return
        print("No hay habitaciones disponibles de ese tipo")

    # Mostrar estado de las habitaciones
    def mostrar_habitaciones(self):
        for habitacion in self.habitaciones:
            estado = "Disponible" if habitacion.disponible else "Ocupada"
            print(f"Habitación {habitacion.numero} - {habitacion.tipo} - {estado}")


# Crear hotel
hotel = Hotel("Hotel Palmas")

# Crear habitaciones
hab1 = Habitacion(101, "Simple", 50)
hab2 = Habitacion(102, "Doble", 80)

# Agregar habitaciones al hotel
hotel.agregar_habitacion(hab1)
hotel.agregar_habitacion(hab2)

# Crear cliente
cliente1 = Cliente("Juan Pérez")

# Reservar habitación
hotel.reservar_habitacion(cliente1, "Simple")

# Mostrar estado del hotel
hotel.mostrar_habitaciones()