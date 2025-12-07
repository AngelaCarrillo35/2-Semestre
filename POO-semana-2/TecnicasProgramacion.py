
#     Clase base: Auto
# ABSTRACCIÓN
class Auto:
    def __init__(self, marca=None, modelo=None, placa=None, combustible=None, color=None):

        self._marca = marca
        self._modelo = modelo
        self._placa = placa
        self._combustible = combustible
        self._color =color

    # MÉTODO DE ABSTRACCIÓN
    def mostrar_info(self):
        return f"Maca:{self._marca} Modelo:{self._modelo} Placa:{self._placa} Combustible:{self._combustible} Color:{self._color}"

    # -------- MÉTODOS DE ENCAPSULAMIENTO --------
    def get_marca(self):
        return self._marca

    def set_marca(self, nueva_marca):
        if len(nueva_marca) > 1:
            self._marca = nueva_marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, nuevo_modelo):
        if nuevo_modelo > 0:
            self._modelo = nuevo_modelo

    def get_placa(self):
        return self._placa

    def set_placa(self, nueva_placa):
        if len(nueva_placa) > 1:
            self._placa = nueva_placa

    def get_combustible(self):
        return self._combustible

    def set_combustible(self, nuevo_combustible):
        if len(nuevo_combustible) > 1:
            self._combustible = nuevo_combustible

    def get_color(self):
        return self._color

    def set_color(self, nuevo_color):
        if len(nuevo_color) > 1:
            self._color = nuevo_color

#     HERENCIA: Auto y Volqueta

class Volqueta(Auto):
    def __init__(self, marca=None, modelo=None, placa=None, combustible=None, color=None, tonelaje=None, ejes=None, cia=None):
        # Llama al constructor de Auto
        super().__init__(marca, modelo, placa, combustible, color)
        self._tonelaje = tonelaje
        self._ejes = ejes
        self._cia = cia

    def mostrar_info(self):
        return (f"Volqueta: {self._marca} {self._modelo} {self._placa} {self._combustible} {self._color} "
                f"{self._tonelaje} {self._ejes} {self._cia}")

    def get_tonelaje(self):
        return self._tonelaje

    def set_tonelaje(self, nuevo_tonelaje):
        if len(nuevo_tonelaje) > 1:
            self._tonelaje = nuevo_tonelaje

    def get_ejes(self):
        return self._ejes

    def set_ejes(self, nuevos_ejes):
        if nuevos_ejes > 0:
            self._ejes= nuevos_ejes

    def get_cia(self):
        return self._cia

    def set_cia(self, nueva_cia):
        if len(nueva_cia) > 1:
            self._cia = nueva_cia

class Taxi(Auto):
    def __init__(self, marca=None, modelo=None, placa=None, combustible=None, color=None, pasajeros=None, parada=None, ciudad=None):
        # Llama al constructor de Auto
        super().__init__(marca, modelo, placa, combustible, color)
        self._pasajeros = pasajeros
        self._parada = parada
        self._ciudad = ciudad

    def mostrar_info(self):
        return (f"Taxi: {self._marca} {self._modelo} {self._placa} {self._combustible} {self._color} "
                f"{self._pasajeros} {self._parada} {self._ciudad}")

    def get_pasajeros(self):
        return self._pasajeros

    def set_pasajeros(self, nuevos_pasajeros):
        if nuevos_pasajeros > 0:
            self._pasajeros = nuevos_pasajeros

    def get_parada(self):
        return self._parada

    def set_parada(self, nueva_parada):
        if len(nueva_parada) > 1:
            self._parada= nueva_parada

    def get_ciudad(self):
        return self._ciudad

    def set_ciudad(self, nueva_ciudad):
        if len(nueva_ciudad) > 1:
            self._ciudad = nueva_ciudad
# ============================================
#     PROGRAMA PRINCIPAL (uso de las clases)
# ============================================

Auto1 = Auto ("Chevrolet",2015, "ABC-123", "Gasolina", "Rojo")
Auto2 = Auto ()

Auto2.set_marca("KIA")
Auto2.set_modelo(2020)
Auto2.set_placa("TEA-1245")
Auto2.set_combustible("Diesel")
Auto2.set_color("Blanco")

#e1 = Estudiante("María", "Pérez", "F", 20, "Ingeniería")
#d1 = Docente("Ana", "Ramírez", "F", 40, "Programación")

print(Auto1.mostrar_info())
print(Auto2.mostrar_info())


Volq1 = Volqueta("Hino", 2025, "PER-1234", "Diesel", "Amarilla", "20T", 4, "metrotrans")
print(Volq1.mostrar_info())

Volq2 = Volqueta ()
Volq2.set_marca("Eskania")
Volq2.set_modelo(2012)
Volq2.set_combustible("Diesel")
Volq2.set_color("Amarillo")
Volq2.set_tonelaje("30T")
Volq2.set_ejes(4)
Volq2.set_cia("Rutas")
print(Volq2.mostrar_info())

Tax1 = Taxi("Hino", 2025, "PER-1234", "Diesel", "Amarilla", 5, "Aloag", "quito")
print(Tax1.mostrar_info())

Tax3 = Taxi ()
Tax3.set_marca("Toyota")
Tax3.set_modelo(2012)
Tax3.set_combustible("Diesel")
Tax3.set_color("amarillos")
Tax3.set_pasajeros(5)
Tax3.set_parada("Aloasi")
Tax3.set_ciudad("Ambato")
print(Tax3.mostrar_info())

#print(e1.mostrar_info())  # ejemplo de polimorfismo
#print(d1.mostrar_info())  # ejemplo de polimorfismo

# Usando encapsulación (modificando datos de forma controlada)
#p1.set_nombre("Luis Alberto")
#p1.set_edad(31)
#print(p1.mostrar_info())