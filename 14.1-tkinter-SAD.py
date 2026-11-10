import tkinter as tk
from tkinter import ttk

# 1. Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Registro de alumnos")
ventana.geometry("420x450")
ventana.resizable(False, False)
ventana.configure(bg="#F6F4EE")

# 2. Definición de la función para el evento del botón
def guardar_informacion():
    nombre = entradaNom.get().strip()
    id_usuario = entradaID.get().strip()

    if nombre == "" or id_usuario == "":
        etiquetaError.config(text="Por favor, complete todos los campos.", fg="red")
    elif comboCarrera.current() == -1:
        etiquetaError.config(text="Por favor, seleccione una carrera.", fg="red")
    else:
        carrera = comboCarrera.get()
        etiquetaError.config(
            text=f"¡Hola {nombre}!\nID: {id_usuario}\nCarrera: {carrera}", 
            fg="orange"
        )

# 3. Creación y empaquetado de controles (usando pack de forma consistente)

# Campo: Nombre
etiquetaNom = tk.Label(ventana, text="Nombre:", fg="#955AED", bg="#F6F4EE", font=("Arial", 11, "bold"))
etiquetaNom.pack(anchor="w", padx=20, pady=(15, 2))
entradaNom = tk.Entry(ventana, font=("Arial", 11))
entradaNom.pack(fill="x", padx=20)

# Campo: ID / Matrícula
etiquetaID = tk.Label(ventana, text="ID / Matrícula:", fg="#5A9AED", bg="#F6F4EE", font=("Arial", 11, "bold"))
etiquetaID.pack(anchor="w", padx=20, pady=(10, 2))
entradaID = tk.Entry(ventana, font=("Arial", 11))
entradaID.pack(fill="x", padx=20)

# Campo: Carrera (Combobox)
etiquetaCarrera = tk.Label(ventana, text="Carrera:", fg="#D75AED", bg="#F6F4EE", font=("Arial", 11, "bold"))
etiquetaCarrera.pack(anchor="w", padx=20, pady=(10, 2))

carreras = [
    "Ingeniería en Sistemas Computacionales",
    "Ingeniería Industrial",
    "Ingeniería Mecánica",
    "Ingeniería Civil",
    "Ingeniería Electrónica",
    "Ingeniería Química",
    "Arquitectura",
    "Medicina",
    "Derecho",
    "Psicología",
    "Diseño Gráfico",
    "Diseño Multimedia",
]

comboCarrera = ttk.Combobox(ventana, values=carreras, state="readonly", font=("Arial", 10))
comboCarrera.set("Seleccione su carrera")
comboCarrera.pack(fill="x", padx=20)

# Botón Guardar (conectado a la función)
botonGuardar = tk.Button(ventana, text="Guardar", bg="#010101", fg="blue", font=("Arial", 11, "bold"), command=guardar_informacion)
botonGuardar.pack(fill="x", padx=20, pady=20)

# Etiqueta de resultado / error
etiquetaError = tk.Label(ventana, text="", bg="#F6F4EE", font=("Arial", 11, "bold"))
etiquetaError.pack(pady=10)

ventana.mainloop()
