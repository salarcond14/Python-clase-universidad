import tkinter as tk
from tkinter import ttk, messagebox  # Se importa messagebox

# Variable global para almacenar el historial de registros
registros = []

# 1. Función para abrir ventana de resumen
def abrirVentanaResumen():
    ventanaResumen = tk.Toplevel()
    ventanaResumen.title("Resumen de registros")
    ventanaResumen.geometry("600x450")
    ventanaResumen.configure(bg="#E8F6F3")
    
    frameDatos = tk.Frame(ventanaResumen, bg="#E8F6F3")
    frameDatos.pack(pady=20)
    
    # Encabezados de la tabla
    tk.Label(frameDatos, text="Nombre", font=("Arial", 12, "bold"), bg="#E8F6F3").grid(row=0, column=0, padx=15)
    tk.Label(frameDatos, text="Matrícula", font=("Arial", 12, "bold"), bg="#E8F6F3").grid(row=0, column=1, padx=15)
    tk.Label(frameDatos, text="Carrera", font=("Arial", 12, "bold"), bg="#E8F6F3").grid(row=0, column=2, padx=15)
    
    # Mostrar todos los registros almacenados
    for fila, alumno in enumerate(registros, start=1):
        tk.Label(frameDatos, text=alumno[0], font=("Arial", 11), bg="#E8F6F3").grid(row=fila, column=0, padx=10, pady=5)
        tk.Label(frameDatos, text=alumno[1], font=("Arial", 11), bg="#E8F6F3").grid(row=fila, column=1, padx=10, pady=5)
        tk.Label(frameDatos, text=alumno[2], font=("Arial", 11), bg="#E8F6F3").grid(row=fila, column=2, padx=10, pady=5)
        
    # Botón para cerrar la ventana secundaria
    botonCerrarResumen = tk.Button(ventanaResumen, text="Cerrar", command=ventanaResumen.destroy)
    botonCerrarResumen.pack(pady=10)

# 2. Función para limpiar las cajas de texto y el combobox
def limpiarCampos():
    entradaNom.delete(0, "end")
    entradaID.delete(0, "end")
    comboCarrera.set("Seleccione su carrera")

# 3. Función para guardar la información y validar con messagebox
def guardar_informacion():
    nombre = entradaNom.get().strip()
    id_usuario = entradaID.get().strip()

    if nombre == "" or id_usuario == "":
        messagebox.showerror("Error de captura", "Debes escribir el nombre y la matrícula/ID.")
        return
    elif comboCarrera.current() == -1 or comboCarrera.get() == "Seleccione su carrera":
        messagebox.showwarning("Advertencia", "Por favor, seleccione una carrera válida.")
        return
    
    carrera = comboCarrera.get()
    
    # Agregar a la lista de registros
    registros.append([nombre, id_usuario, carrera])
    
    # Confirmar registro exitoso
    messagebox.showinfo("Registro exitoso", "Los datos fueron capturados correctamente.")
    
    # Limpiar formulario
    limpiarCampos()
    
    # Mostrar la ventana secundaria con el resumen acumulado
    abrirVentanaResumen()

# 4. Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Registro de alumnos")
ventana.geometry("420x520")
ventana.resizable(False, False)
ventana.configure(bg="#F6F4EE")

# 5. Creación de controles

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

# Contenedor/Frame para los botones Guardar y Cerrar
frameBotones = tk.Frame(ventana, bg="#F6F4EE")
frameBotones.pack(pady=30)

botonGuardar = tk.Button(
    frameBotones, 
    text="Guardar", 
    bg="#117A76", 
    fg="white", 
    font=("Arial", 11, "bold"), 
    width=12,
    command=guardar_informacion
)
botonGuardar.pack(side="left", padx=10)

botonCerrar = tk.Button(
    frameBotones, 
    text="Cerrar", 
    bg="#C0392B", 
    fg="white", 
    font=("Arial", 11, "bold"), 
    width=12,
    command=ventana.destroy
)
botonCerrar.pack(side="left", padx=10)

ventana.mainloop()