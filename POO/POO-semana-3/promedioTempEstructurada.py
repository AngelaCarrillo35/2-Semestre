# Programa para calcular el promedio de temperatura semanal
# Programación estructurada

suma_temperaturas = 0 #Definición de la variable que almacena la sumatoria de las temperaturas de cada día
dias = 7 #Definir el número de días que se repetira en el ingreso

for i in range(1, dias + 1): #Se define el numero de veces que se repetira el bloque de instrucciones
    temperatura = float(input(f"Ingrese la temperatura del día {i}: ")) #Ingresar la temperatura para cada día
    suma_temperaturas += temperatura #Almacena la sumatoria de las temperaturas ingresadas

promedio = suma_temperaturas / dias #Variable que almacena el promedio1

print("El promedio de temperatura de la semana es:", promedio) #Imprime el valor del promedio calculado

