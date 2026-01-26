# Programa para calcular el promedio de temperatura semanal
# Usando Programación Orientada a Objetos (POO)

class Semana: #Definición de la clase
    def __init__(self): #Definición del constructor
        self.temperaturas = [] #Definición de atributo tipo lista para almacenar las temperaturas

    def ingresar_temperaturas(self): #Definición del metodo para ingresar
        for i in range(1, 8): #Define el número de veces a repetir
            temp = float(input(f"Ingrese la temperatura del día {i}: ")) #Varaible que almacena la temperatura ingresada por día
            self.temperaturas.append(temp) #Agrega la temp al atributo temperatura

    def calcular_promedio(self): #Definición del metodo calcular promedio
        suma = sum(self.temperaturas) #Suma de las temperaturas ingresadad en el atributo temperaturas
        promedio = suma / len(self.temperaturas) #Calcula el promedio de la sumatoria para el tamaño del atributo
        return promedio #Retorna el valor del promedio


# Programa principal
semana = Semana() #Creación del objeto de la clase Semana
semana.ingresar_temperaturas() #Ejecutar el metodo ingresar_temperatura
resultado = semana.calcular_promedio() #Ejecutar el metodo calcular.promedio y almacenar el valor que retorna

print("El promedio de temperatura de la semana es:", resultado) #Impresión del resultado