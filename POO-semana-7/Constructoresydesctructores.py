class Persona: #Creación de la clase

    def __init__(self, nombre, apellido): #Indica los atributos nombre y edad, se ejecuta cuando se crea el objeto
        self.nombre = nombre
        self.apellido = apellido
        print(f"Persona creada: {self.nombre} {self.apellido}")

    def saludar(self): #Metodo simple de la clase
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}.")

    def __del__(self): #Se ejecuta el mensaje
        print(f"Persona eliminada: {self.nombre}. Recursos liberados.")


persona1 = Persona("Anggie","Ayala") # Al crear el objeto se ejecuta el constructor (__init__)

persona1.saludar()

del persona1 # Al eliminar el objeto se ejecuta el destructor (__del__)
