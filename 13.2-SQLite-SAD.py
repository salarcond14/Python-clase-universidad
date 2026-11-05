import sqlite3

def main():
    try:
        # 1. Crear la base de datos (se genera el archivo empresa.db)[span_2](start_span)[span_2](end_span)
        conexion = sqlite3.connect("empresa.db")
        cursor = conexion.cursor()
        print("Base de datos 'empresa.db' creada y conectada exitosamente.")

        # 2. Crear la tabla 'empleados[span_3](start_span)'[span_3](end_span)
        # id_que es el campo llave (Primary Key), seguido de nombre, puesto y salario
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id_que INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                puesto TEXT NOT NULL,
                salario REAL NOT NULL
            )
        """)
        conexion.commit()
        print("Tabla 'empleados' creada correctamente.")

        # 3. Insertar datos en la tabla empleados[span_4](start_span)[span_4](end_span)
        # 3.1 Inserción desde el código fuente (al menos 5 empleados: los 3 pedidos + 2 adicionales)[span_5](start_span)[span_5](end_span)
        empleados_iniciales = [
            (1, "Juan Pérez", "Gerente", 35000),
            (2, "Ana Gómez", "Secretaria", 20000),
            (3, "Carlos López", "Programador", 30000),
            (4, "Sofía Ramírez", "Diseñadora", 32000),  # Empleado adicional 1
            (5, "Luis Torres", "Contador", 28000)       # Empleado adicional 2
        ]
        
        # Usamos executemany para insertar múltiples registros de golpe
        cursor.executemany("""
            INSERT OR IGNORE INTO empleados (id_que, nombre, puesto, salario)
            VALUES (?, ?, ?, ?)
        """, empleados_iniciales)
        conexion.commit()
        print("Se insertaron los 5 empleados iniciales desde el código fuente.")

        # 3.2 Inserción de 1 empleado desde el teclado[span_6](start_span)[span_6](end_span)
        print("\n--- Registro de un nuevo empleado por teclado ---")
        nuevo_id = int(input("Ingresa el ID del empleado: "))
        nuevo_nombre = input("Ingresa el nombre del empleado: ")
        nuevo_puesto = input("Ingresa el puesto del empleado: ")
        nuevo_salario = float(input("Ingresa el salario del empleado: "))

        cursor.execute("""
            INSERT INTO empleados (id_que, nombre, puesto, salario)
            VALUES (?, ?, ?, ?)
        """, (nuevo_id, nuevo_nombre, nuevo_puesto, nuevo_salario))
        conexion.commit()
        print("Empleado registrado exitosamente desde el teclado.")

        # 4. Mostrar todos los registros utilizando fetchall()[span_7](start_span)[span_7](end_span)
        print("\n--- Lista completa de empleados (fetchall) ---")
        cursor.execute("SELECT * FROM empleados")
        todos_empleados = cursor.fetchall()
        
        for emp in todos_empleados:
            print(f"ID: {emp[0]} | Nombre: {emp[1]} | Puesto: {emp[2]} | Salario: ${emp[3]:,.2f}")

        # 5. Mostrar registros con una condición[span_8](start_span)[span_8](end_span)
        # Adicional: Filtrar empleados con salario mayor a $30,000 y usar fetchone() para el primero[span_9](start_span)[span_9](end_span)
        print("\n--- Primer empleado con salario mayor a $30,000 (fetchone) ---")
        cursor.execute("SELECT * FROM empleados WHERE salario > 30000")
        primer_filtrado = cursor.fetchone()
        
        if primer_filtrado:
            print(f"ID: {primer_filtrado[0]} | Nombre: {primer_filtrado[1]} | Puesto: {primer_filtrado[2]} | Salario: ${primer_filtrado[3]:,.2f}")
        else:
            print("No se encontraron empleados con un salario mayor a $30,000.")

    except sqlite3.Error as e:
        print(f"Se produjo un error en la base de datos: {e}")
    except ValueError:
        print("Error: Ingresaste un valor numérico inválido por el teclado.")
    finally:
        # Cerrar la conexión para liberar recursos
        if 'conexion' in locals():
            conexion.close()
            print("\nConexión a la base de datos cerrada.")

if __name__ == "__main__":
    main()
