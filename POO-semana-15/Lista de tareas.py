# Aplicación GUI de Lista de Tareas usando Tkinter
# Autor: Angela Carrillo
# Descripción: Permite añadir, marcar como completadas y eliminar tareas.

import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x450")

# Lista interna para guardar tareas
tareas = []

# Función para actualizar la lista visual
def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    for tarea in tareas:
        lista_tareas.insert(tk.END, tarea)

# Función para añadir tarea
def agregar_tarea(event=None):  # event permite usar Enter
    tarea = entrada_tarea.get().strip()
    if tarea != "":
        tareas.append(tarea)
        entrada_tarea.delete(0, tk.END)
        actualizar_lista()
    else:
        messagebox.showwarning("Advertencia", "Debes escribir una tarea")

# Función para marcar como completada
def marcar_completada():
    try:
        indice = lista_tareas.curselection()[0]
        tarea = tareas[indice]

        # Cambiar visualmente la tarea
        if not tarea.startswith("✔ "):
            tareas[indice] = "✔ " + tarea
        else:
            tareas[indice] = tarea.replace("✔ ", "")

        actualizar_lista()
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea")

# Función para eliminar tarea
def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        tareas.pop(indice)
        actualizar_lista()
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea")

# Evento opcional: doble clic para completar tarea
def doble_click(event):
    marcar_completada()

# Campo de entrada
entrada_tarea = tk.Entry(ventana, width=30)
entrada_tarea.pack(pady=10)

# Permitir agregar con Enter
entrada_tarea.bind("<Return>", agregar_tarea)

# Botones
btn_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=40, height=15)
lista_tareas.pack(pady=10)

# Evento de doble clic
lista_tareas.bind("<Double-Button-1>", doble_click)

# Ejecutar aplicación
ventana.mainloop()