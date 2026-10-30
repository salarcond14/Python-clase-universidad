import sqlite3
from pathlib import Path

carpeta = Path(__file__).resolve().parent
rutaBD = carpeta / "ejemplo.db"


try:
    conexion = sqlite3.connect(rutaBD)
    cursor = conexion.cursor()

    # Crear la tabla 'estudiantes' si no existe
    estudiantes = [("Juan", 20, "Ingeniería"),
               ("María", 22, "Medicina"),
               ("Pedro", 21, "Derecho")
               ]

    cursor.executemany('''
    INSERT INTO estudiantes (nombre, edad, carrera)
    VALUES (?, ?, ?)
    ''', estudiantes)

    # Crear la tabla 'estudiantes' si no existe
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER,
        carrera TEXT
    )
    ''')  

    # Guardar cambios y cerrar la conexión
    conexion.commit()
    print("Tabla 'estudiantes' creada exitosamente.")

    cursor.execute('''
    INSERT INTO estudiantes (nombre, edad, carrera) 
    VALUES (?, ?, ?)
    ''', ("Ana", 20, "Ingeniería")) # Aquí se pasan los valores a insertar en la tabla
    
    #Hacer consulta
    cursor.execute('SELECT * FROM estudiantes')
    registros = cursor.fetchall()
    for fila in registros:
        print(fila)

    #Consultar con condición
    print("\n Consulta con mayores a 23 años")
    cursor.execute('SELECT nombre, carrera FROM estudiantes WHERE edad > ?', (23,))
    for fila in cursor.fetchall():
        print(f"Nombre: {fila[0]}, Carrera: {fila[1]}")

    conexion.commit()
    print("Datos guardados correctamente")

    conexion.close()
    
except sqlite3.Error as e:
    print(f"Error al crear la tabla: {e}") 

finally:
    if 'conexion' in locals():
        conexion.close()
        print("Conexión cerrada correctamente.")
