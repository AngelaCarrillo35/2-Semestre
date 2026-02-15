import threading
import time

# Función que ejecutará cada hilo
def tarea_hilo(identificador, delay):
    for i in range(5):
        print(f'Hilo {identificador}: ejecutando tarea {i}')
        time.sleep(delay)

# Creación de los hilos
hilo1 = threading.Thread(target=tarea_hilo, args=(1, 1))
hilo2 = threading.Thread(target=tarea_hilo, args=(2, 0.8))
hilo3 = threading.Thread(target=tarea_hilo, args=(3, 1.2))

# Inicio de los hilos
hilo1.start()
hilo2.start()
hilo3.start()

# Esperar a que los hilos terminen
hilo1.join()
hilo2.join()
hilo3.join()

print("Programa principal: todas las tareas han finalizado")