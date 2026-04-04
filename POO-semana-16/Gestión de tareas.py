import tkinter as tk
from tkinter import messagebox

# FUNCIONES
def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea != "":
        lista_tareas.insert(tk.END, "⬜ " + tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Escribe una tarea.")

def completar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        indice = seleccion[0]
        tarea = lista_tareas.get(indice)

        if tarea.startswith("⬜"):
            tarea_completada = tarea.replace("⬜", "✅", 1)
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, tarea_completada)
            lista_tareas.itemconfig(indice, {'fg': 'green'})
    else:
        messagebox.showwarning("Aviso", "Selecciona una tarea.")

def eliminar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion[0])
    else:
        messagebox.showwarning("Aviso", "Selecciona una tarea.")

def cerrar_app(event=None):
    ventana.destroy()

# -------------------------------
# VENTANA PRINCIPAL
# -------------------------------
ventana = tk.Tk()
ventana.title("Gestión de Tareas")
ventana.geometry("500x400")
ventana.config(bg="#f0f0f0")

# -------------------------------
# ENTRY
# -------------------------------
entrada_tarea = tk.Entry(ventana, font=("Arial", 14), width=30)
entrada_tarea.pack(pady=10)

# -------------------------------
# BOTONES
# -------------------------------
frame_botones = tk.Frame(ventana, bg="#f0f0f0")
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar", width=15, command=agregar_tarea)
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="Completar", width=15, command=completar_tarea)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar", width=15, command=eliminar_tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

# -------------------------------
# LISTBOX
# -------------------------------
lista_tareas = tk.Listbox(ventana, width=50, height=15, font=("Arial", 12))
lista_tareas.pack(pady=10)

# -------------------------------
# ATAJOS DE TECLADO
# -------------------------------
ventana.bind("<Return>", agregar_tarea)     # Enter
ventana.bind("<c>", completar_tarea)        # tecla C
ventana.bind("<Delete>", eliminar_tarea)    # Delete
ventana.bind("<d>", eliminar_tarea)         # tecla D
ventana.bind("<Escape>", cerrar_app)        # Escape

# -------------------------------
# EJECUTAR
# -------------------------------
ventana.mainloop()