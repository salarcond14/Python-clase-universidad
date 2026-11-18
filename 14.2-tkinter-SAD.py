import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk       # Librerías para agregar logo
from pathlib import Path             # Para encontrar la ruta del archivo

# Variable global para almacenar el historial de registros
registros = []

# 1. Función para abrir ventana de resumen
def abrirVentanaResumen():
    ventanaResumen = tk.Toplevel()
    ventanaResumen.title("Resumen del registro")
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
        
    # Botón para cerrar la ventana secundaria y limpiar controles con lambda
    botonCerrarResumen = tk.Button(
        ventanaResumen, 
        text="Cerrar", 
        command=lambda: [limpiarCampos(), ventanaResumen.destroy()]
    )
    botonCerrarResumen.pack(pady=10)

# 2. Función para limpiar las cajas de texto y el combobox
def limpiarCampos():
    entradaNom.delete(0, "end")
    entradaMat.delete(0, "end")
    comboCarrera.set("Selecciona una carrera")

# 3. Función para guardar la información y validar con messagebox
def guardar_informacion():
    nombre = entradaNom.get().strip()
    matricula = entradaMat.get().strip()

    # Validación corregida según la presentación
    if nombre == "" or matricula == "":
        messagebox.showerror("Error de captura", "Debes escribir el nombre y la matrícula.")
        return
    elif comboCarrera.current() == -1 or comboCarrera.get() == "Selecciona una carrera":
        messagebox.showwarning("Advertencia", "Por favor, seleccione una carrera válida.")
        return
    
    carrera = comboCarrera.get()
    
    # Agregar a la lista de registros
    registros.append([nombre, matricula, carrera])
    
    # Confirmar registro exitoso
    messagebox.showinfo("Registro exitoso", "Los datos fueron capturados correctamente.")
    
    # Mostrar la ventana secundaria con el resumen acumulado
    abrirVentanaResumen()

# 4. Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Registro de alumnos")
ventana.geometry("420x520")
ventana.resizable(False, False)
ventana.configure(bg="#F3E6E8")

# Agregando el logo según código de la presentación
try:
    # Obtiene la carpeta donde está el archivo.py
    rutaBase = Path(__file__).parent
    # Construye la ruta del logo
    rutaLogo = rutaBase / "logo.png"
    print("Ruta logo:", rutaLogo)
    print("Existe:", rutaLogo.exists())
    
    # Abre la imagen
    imagen = Image.open(rutaLogo)
    # Ajusta tamaño
    imagen = imagen.resize((280, 110))
    # Convierte para Tkinter
    imagenTk = ImageTk.PhotoImage(imagen)
    # Muestra el logo
    etiquetaLogo = tk.Label(ventana, image=imagenTk, bg="#F3E6E8")
    # Mantener referencia a la imagen
    etiquetaLogo.image = imagenTk
    etiquetaLogo.pack(pady=10)
except Exception as error:
    print("Error al cargar el logo:")
    print(error)
    etiquetaErrorLogo = tk.Label(ventana, text="No se pudo cargar el logo.", bg="#F3E6E8", fg="red")
    etiquetaErrorLogo.pack(pady=10)

# 5. Creación de controles

# Campo: Nombre
etiquetaNom = tk.Label(ventana, text="Nombre:", fg="#955AED", bg="#F3E6E8", font=("Arial", 11, "bold"))
etiquetaNom.pack(anchor="w", padx=20, pady=(15, 2))
entradaNom = tk.Entry(ventana, font=("Arial", 11))
entradaNom.pack(fill="x", padx=20)

# Campo: Matrícula
etiquetaMat = tk.Label(ventana, text="Matrícula:", fg="#5A9AED", bg="#F3E6E8", font=("Arial", 11, "bold"))
etiquetaMat.pack(anchor="w", padx=20, pady=(10, 2))
entradaMat = tk.Entry(ventana, font=("Arial", 11))
entradaMat.pack(fill="x", padx=20)

# Campo: Carrera (Combobox)
etiquetaCarrera = tk.Label(ventana, text="Carrera:", fg="#D75AED", bg="#F3E6E8", font=("Arial", 11, "bold"))
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
comboCarrera.set("Selecciona una carrera")
comboCarrera.pack(fill="x", padx=20)

# Contenedor/Frame para los botones Guardar y Cerrar
frameBotones = tk.Frame(ventana, bg="#F3E6E8")
frameBotones.pack(pady=(130, 10))  # Modificado para empujar los botones hacia abajo

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
