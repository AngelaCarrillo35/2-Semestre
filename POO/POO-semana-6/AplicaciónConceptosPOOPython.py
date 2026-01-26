
# CLASE BASE

class Persona:#Definición de la clase persona.
    """Clase base que representa a una persona. Aplica encapsulación y define métodos generales."""

    def __init__(self, nombre, edad):#Constructor de la clase, se ejecuta cuando se crea un objeto perona.
        # Atributos encapsulados
        self._nombre = nombre
        self._edad = edad

    # Métodos getters (encapsulación)
    def get_nombre(self):#Metodo acceder al atributo nombre.
        return self._nombre #Devuelve el nombre de la persona.

    def get_edad(self):#Metodo para acceder al atributo edad.
        return self._edad #Devuelve la edad de la persona

    # Método que será sobrescrito (polimorfismo)
    def presentarse(self):#Metodo que describe a la persona, muestra polimorfismo.
        return f"Hola, soy {self._nombre} y tengo {self._edad} años." #Retorna mensaje utilizando los atributos encapsulados

# CLASE DERIVADA (HERENCIA)
class Estudiante(Persona): #Deinición clase estudiante que hereda de persona.
    """Clase derivada que hereda de Persona. Aplica herencia y polimorfismo."""

    def __init__(self, nombre, edad, carrera): #Constructor de la clase estudiante
        # Llamada al constructor de la clase base
        super().__init__(nombre, edad)
        self.carrera = carrera #Atributo propio de la clase estudiante

    # Método sobrescrito (polimorfismo)
    def presentarse(self):
        return (
            f"Hola, soy {self.get_nombre()}, tengo {self.get_edad()} años "
            f"y estudio la carrera de {self.carrera}." #Mensaje especifico para el estudiante
        )

# PROGRAMA PRINCIPAL

# Creación de objetos (instancias)
persona1 = Persona("Anggie", 24)#Se crea un objeto de la clase persona
estudiante1 = Estudiante("Abigail", 20, "Ingeniería en Sistemas") #Se crea el objeto de la clase estudiante

# Uso de métodos
print(persona1.presentarse()) #Llama al metodo presentarse del objeto persona
print(estudiante1.presentarse()) #Llama al metodo presentarse del objeto persona