# Ejercicio 1
libro = {
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "anio": 1967,
    "precio": 350.00
}
# 1. get()
print("1. get():", libro.get("titulo"))

# 2. keys()
print("\n2. keys():", libro.keys())

# 3. values()
print("\n3. values():", libro.values())

# 4. items()
print("\n4. items():", libro.items())

# 5. update()
libro.update({"editorial": "Sudamericana"})
print("\n5. update():", libro)

# 6. pop()
precio = libro.pop("precio")
print("\n6. pop():", precio, "| Estado actual del libro:", libro)

# 7. setdefault()
paginas = libro.setdefault("paginas", 471)
print("\n7. setdefault():", paginas, "| Estado actual del libro:", libro)

# 8. copy()
copia_libro = libro.copy()
print("\n8. copy():", copia_libro)

# 9. sum()
suma_numerica = sum([libro["anio"], libro["paginas"]])
print("\n9. sum():", suma_numerica)

# 10. clear()
libro.clear()
print("\n10. clear():", libro)


#Ejercicio 2 

print("\n=== Librería Online A ===")

class Tienda:
    def __init__(self):
        self.catalogo = {
            1: {"titulo": "Pedro Páramo", "precio": 220.0},
            2: {"titulo": "El principito", "precio": 180.0},
            3: {"titulo": "Cien años de soledad", "precio": 350.0},
            4: {"titulo": "Don Quijote", "precio": 400.0},
            5: {"titulo": "Hábitos Atómicos", "precio": 299.0}
        }

    def agregar(self, titulo, precio):
        # TODO:
        # 1. Obtener el siguiente ID disponible.
        idLibro = max(self.catalogo.keys()) + 1
        # 2. Agregar el libro al catálogo.
        self.catalogo[idLibro] = {"titulo": titulo, "precio": precio}

    def buscarLibro(self, id_libro):
        # TODO:
        # Verificar si el ID existe en el catálogo.
        if id_libro in self.catalogo:
        # Si existe, mostrar el título y precio.
            print(f"ID: {id_libro}, Título: {self.catalogo[id_libro]['titulo']}, Precio: ${self.catalogo[id_libro]['precio']}")
        # Si no existe, mostrar un mensaje de error.
        else:
            print("Libro no encontrado.")

    def mostrar(self):
        # TODO:
        # Recorrer el diccionario e imprimir
        # ID, título y precio de cada libro.
        for id_libro, info_libro in self.catalogo.items():
            print(f"ID: {id_libro}, Título: {info_libro['titulo']}, Precio: ${info_libro['precio']}")

    def totalInventario(self):
        # TODO:
        # Crear una variable acumuladora.
        # Recorrer el catálogo.
        # Sumar cada precio.
        # Regresar el total.
        total = sum(info['precio'] for info in self.catalogo.values())
        return total

    # Reto opcional
    def eliminar(self, id_libro):
        # TODO:
        # Eliminar un libro utilizando pop().
        self.catalogo.pop(id_libro, None)


# Programa principal

t = Tienda()

print("\n--- Catálogo Inicial ---")
t.mostrar()

# Buscar un libro
id_libro = int(input("\nDa el ID del libro a buscar: "))
t.buscarLibro(id_libro)

# Mostrar total del inventario
print("\nTotal del inventario: $", t.totalInventario())

# Agregar un libro
print("\n--- Agregar Libro ---")

titulo = input("Ingrese el título del libro: ")
precio = float(input("Ingrese el precio del libro: "))

t.agregar(titulo, precio)

print("\n--- Catálogo Actualizado ---")
t.mostrar()

print("\nTotal del inventario: $", t.totalInventario())

# Reto opcional
# id_eliminar = int(input("\nDa el ID del libro a eliminar: "))

# t.eliminar(id_eliminar)

# t.mostrar()