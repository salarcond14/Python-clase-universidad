import sqlite3
from pathlib import Path


class BaseDatos:
    """Clase para gestionar la base de datos de alumnos y libros mediante SQLite."""

    def __init__(self, rutaBD):
        """Crea la conexión, las tablas y realiza la carga de datos iniciales."""
        self.conexion = sqlite3.connect(rutaBD)
        self.cursor = self.conexion.cursor()
        self.crearTablas()
        self.cargarRegistros()

    def crearTablas(self):
        """Crea las tablas 'alumnos' y 'libros' si no existen en la base de datos."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS alumnos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                carrera TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                autor TEXT
            )
        """)
        self.conexion.commit()

    def cargarRegistros(self):
        """Inserta 2 registros por catálogo solo si las tablas están vacías."""
        # Carga inicial para la tabla alumnos
        self.cursor.execute("SELECT COUNT(*) FROM alumnos")
        if self.cursor.fetchone()[0] == 0:
            self.agregarAlumno("Ana Torres", "Ciencia de Datos")
            self.agregarAlumno("Luis Pérez", "Programación")

        # Carga inicial para la tabla libros
        self.cursor.execute("SELECT COUNT(*) FROM libros")
        if self.cursor.fetchone()[0] == 0:
            self.agregarLibro("Cien Años de Soledad", "Gabriel García Márquez")
            self.agregarLibro("Don Quijote de la Mancha", "Miguel de Cervantes")

    # --- MÉTODOS PARA ALUMNOS ---

    def agregarAlumno(self, nombre, carrera):
        """Agrega un alumno nuevo al catálogo."""
        self.cursor.execute(
            "INSERT INTO alumnos (nombre, carrera) VALUES (?, ?)", (nombre, carrera)
        )
        self.conexion.commit()

    def mostrarAlumnos(self):
        """Muestra todos los alumnos almacenados."""
        self.cursor.execute("SELECT * FROM alumnos")
        filas = self.cursor.fetchall()
        print("\n--- CATÁLOGO DE ALUMNOS ---")
        if not filas:
            print("No hay alumnos registrados.")
        else:
            for id_alumno, nombre, carrera in filas:
                print(f"ID: {id_alumno} | Nombre: {nombre} | Carrera: {carrera}")

    def actualizarAlumno(self, id_alumno, nombre, carrera):
        """Actualiza el nombre y carrera del alumno con el ID especificado."""
        self.cursor.execute(
            "UPDATE alumnos SET nombre = ?, carrera = ? WHERE id = ?",
            (nombre, carrera, id_alumno),
        )
        self.conexion.commit()
        return self.cursor.rowcount > 0

    def eliminarAlumno(self, id_alumno):
        """Elimina el alumno según su ID."""
        self.cursor.execute("DELETE FROM alumnos WHERE id = ?", (id_alumno,))
        self.conexion.commit()
        return self.cursor.rowcount > 0

    def buscarAlumnosPorCarrera(self, carrera):
        """Consulta extra: muestra ID y Nombre de los alumnos pertenecientes a una carrera dada."""
        self.cursor.execute(
            "SELECT id, nombre FROM alumnos WHERE carrera LIKE ?", (f"%{carrera}%",)
        )
        filas = self.cursor.fetchall()
        print(f"\n--- ALUMNOS DE LA CARRERA: {carrera} ---")
        if not filas:
            print("No se encontraron alumnos registrados en esa carrera.")
        else:
            for id_alumno, nombre in filas:
                print(f"ID: {id_alumno} | Nombre: {nombre}")

    # --- MÉTODOS PARA LIBROS ---

    def agregarLibro(self, titulo, autor):
        """Agrega un libro nuevo al catálogo."""
        self.cursor.execute(
            "INSERT INTO libros (titulo, autor) VALUES (?, ?)", (titulo, autor)
        )
        self.conexion.commit()

    def mostrarLibros(self):
        """Muestra todos los libros almacenados."""
        self.cursor.execute("SELECT * FROM libros")
        filas = self.cursor.fetchall()
        print("\n--- CATÁLOGO DE LIBROS ---")
        if not filas:
            print("No hay libros registrados.")
        else:
            for id_libro, titulo, autor in filas:
                print(f"ID: {id_libro} | Título: {titulo} | Autor: {autor}")

    def actualizarLibro(self, id_libro, titulo, autor):
        """Actualiza el título y autor del libro especificado."""
        self.cursor.execute(
            "UPDATE libros SET titulo = ?, autor = ? WHERE id = ?",
            (titulo, autor, id_libro),
        )
        self.conexion.commit()
        return self.cursor.rowcount > 0

    def eliminarLibro(self, id_libro):
        """Elimina el libro según su ID."""
        self.cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
        self.conexion.commit()
        return self.cursor.rowcount > 0

    def cerrar(self):
        """Cierra la conexión con la base de datos."""
        self.conexion.close()


def menu():
    """Despliega las opciones del menú principal en pantalla."""
    print("\n" + "=" * 30)
    print("         MENÚ PRINCIPAL         ")
    print("=" * 30)
    print("1. Agregar alumno")
    print("2. Agregar libro")
    print("3. Mostrar alumnos")
    print("4. Mostrar libros")
    print("5. Actualizar alumno")
    print("6. Actualizar libro")
    print("7. Eliminar alumno")
    print("8. Eliminar libro")
    print("9. Buscar alumnos por carrera (Consulta extra)")
    print("0. Salir")
    return input("Elige una opción: ").strip()


def main():
    """Ejecuta el flujo interactivo controlando las excepciones y el cierre de BD."""
    ruta_bd = Path(__file__).parent / "catalogos.db"
    
    try:
        bd = BaseDatos(ruta_bd)

        while True:
            opcion = menu()

            if opcion == "1":
                nombre = input("Ingrese el nombre del alumno: ")
                carrera = input("Ingrese la carrera del alumno: ")
                bd.agregarAlumno(nombre, carrera)
                print("¡Alumno agregado exitosamente!")

            elif opcion == "2":
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                bd.agregarLibro(titulo, autor)
                print("¡Libro agregado exitosamente!")

            elif opcion == "3":
                bd.mostrarAlumnos()

            elif opcion == "4":
                bd.mostrarLibros()

            elif opcion == "5":
                try:
                    id_alumno = int(input("Ingrese el ID del alumno a actualizar: "))
                    nombre = input("Ingrese el nuevo nombre: ")
                    carrera = input("Ingrese la nueva carrera: ")
                    if bd.actualizarAlumno(id_alumno, nombre, carrera):
                        print("¡Alumno actualizado exitosamente!")
                    else:
                        print("No se encontró un alumno con ese ID.")
                except ValueError:
                    print("Error: El ID debe ser un número entero.")

            elif opcion == "6":
                try:
                    id_libro = int(input("Ingrese el ID del libro a actualizar: "))
                    titulo = input("Ingrese el nuevo título: ")
                    autor = input("Ingrese el nuevo autor: ")
                    if bd.actualizarLibro(id_libro, titulo, autor):
                        print("¡Libro actualizado exitosamente!")
                    else:
                        print("No se encontró un libro con ese ID.")
                except ValueError:
                    print("Error: El ID debe ser un número entero.")

            elif opcion == "7":
                try:
                    id_alumno = int(input("Ingrese el ID del alumno a eliminar: "))
                    if bd.eliminarAlumno(id_alumno):
                        print("¡Alumno eliminado exitosamente!")
                    else:
                        print("No se encontró un alumno con ese ID.")
                except ValueError:
                    print("Error: El ID debe ser un número entero.")

            elif opcion == "8":
                try:
                    id_libro = int(input("Ingrese el ID del libro a eliminar: "))
                    if bd.eliminarLibro(id_libro):
                        print("¡Libro eliminado exitosamente!")
                    else:
                        print("No se encontró un libro con ese ID.")
                except ValueError:
                    print("Error: El ID debe ser un número entero.")

            elif opcion == "9":
                carrera = input("Ingrese la carrera que desea buscar: ")
                bd.buscarAlumnosPorCarrera(carrera)

            elif opcion == "0":
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

    except sqlite3.Error as err:
        print(f"Error en la base de datos: {err}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        if 'bd' in locals():
            bd.cerrar()
            print("Conexión a la base de datos cerrada de manera segura.")


if __name__ == "__main__":
    main()
