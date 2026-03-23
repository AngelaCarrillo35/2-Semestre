import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry  # necesitas instalar: pip install tkcalendar

# Lista para almacenar eventos
eventos = []

# Función para agregar evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        evento = f"{fecha} - {hora} - {descripcion}"
        eventos.append(evento)
        lista_eventos.insert(tk.END, evento)

        # Limpiar campos
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios")

# Función para eliminar evento
def eliminar_evento():
    seleccion = lista_eventos.curselection()
    if seleccion:
        confirmar = messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?")
        if confirmar:
            index = seleccion[0]
            lista_eventos.delete(index)
            eventos.pop(index)
    else:
        messagebox.showwarning("Error", "Seleccione un evento")

# Función para salir
def salir():
    ventana.quit()

# Ventana principal
ventana = tk.Tk()
ventana.title("Agenda de Eventos")
ventana.geometry("500x400")


# FRAME LISTA DE EVENTOS
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

tk.Label(frame_lista, text="Lista de Eventos").pack()

lista_eventos = tk.Listbox(frame_lista, width=60, height=10)
lista_eventos.pack()

# FRAME ENTRADA DE DATOS
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Fecha
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
entry_fecha = DateEntry(frame_entrada, width=12)
entry_fecha.grid(row=0, column=1)

# Hora
tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1)

# Descripción
tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
entry_descripcion = tk.Entry(frame_entrada, width=30)
entry_descripcion.grid(row=2, column=1)


# FRAME BOTONES

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=5)

# Ejecutar aplicación
ventana.mainloop()