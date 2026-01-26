#Cálculo del área de un rectángulo
#El ancho y el alto de un rectángulo, calcula su área y muestra el resultado en pantalla.


def calcular_area_rectangulo(ancho, alto): # Función que calcula el área de un rectángulo
    """
    Calcula el área de un rectángulo.
    :param ancho: ancho del rectángulo (float)
    :param alto: alto del rectángulo (float)
    :return: área del rectángulo (float)
    """
    area = ancho * alto
    return area

mensaje_bienvenida = "Cálculo del área de un rectángulo" # Mensaje de bienvenida (string)
print(mensaje_bienvenida)

ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: ")) # Entrada de datos (float)
alto_rectangulo = float(input("Ingrese el alto del rectángulo: "))

area_rectangulo = calcular_area_rectangulo(ancho_rectangulo, alto_rectangulo) # Cálculo del área

area_valida = area_rectangulo > 0 # Variable booleana para verificar si el área es válida

if area_valida: # Uso de una estructura condicional

    print("El área del rectángulo es:", area_rectangulo) # Salida de datos
else:
    print("Los valores ingresados no son válidos.")