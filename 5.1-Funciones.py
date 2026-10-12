#Ejercicio 1
def calcular_area(base, altura):
    area = base * altura
    return area

# Pedimos los valores al usuario fuera de la función
b = float(input("Ingresa la base: "))
h = float(input("Ingresa la altura: "))

# Llamamos a la función y guardamos el resultado
resultado = calcular_area(b, h)
print("El área es:", resultado)

#Ejercicio 2

# Corrección de errores:
# 1. En la segunda llamada original "mostrarProducto(precio=8000, "Tablet")" existe un SyntaxError
#    porque los argumentos posicionales no pueden ir después de un argumento con clave
# 2. Definimos la función 'mostrarProducto' para aceptar ambos parámetros correctamente.

def mostrarProducto(producto, precio):
    print("Producto:", producto, "Precio:", precio)

# Código corregido:
mostrarProducto("Laptop", 15000)
mostrarProducto("Tablet", 8000) # Corregimos el orden de los argumentos

#Ejercicio 3
def calcularPromedio(c1, c2, c3):
    prom = (c1 + c2 + c3) / 3
    return prom

# Pedimos las calificaciones juntas
datos = input("Ingresa las tres calificaciones separadas por un espacio: ")
lista = datos.split() # Separamos el texto por espacios

n1 = float(lista[0])
n2 = float(lista[1])
n3 = float(lista[2])

# Calculamos e imprimimos el promedio usando la función
promedio = calcularPromedio(n1, n2, n3)
print("Promedio:", promedio)

if promedio >= 7:
    print("Aprobado")
else:
    print("Reprobado")


# Ventaja de utilizar return:
# Devolver el valor mediante 'return' permite guardar el resultado en una variable,
# realizar operaciones posteriores (evaluar si aprobó/reprobó o formatear el texto) o consumirlo desde otras
# partes del programa, mientras que imprimirlo ('print') dentro de la función limita su uso únicamente a la pantalla sin almacenar el dato.

#Ejercicio 4
# Variable GLOBAL: Se crea fuera y vale 100 en todo el programa
bonus = 100

def calcularPuntos(puntos):
    # Variable LOCAL: Se crea adentro de la función y solo existe aquí.
    # Esta 'bonus' opaca a la global mientras estemos dentro de la función.
    bonus = 50
    total = puntos + bonus

    print("Dentro de la función:")
    print("Total:", total) # Suma 200 + 50 = 250
    print("Bonus:", bonus) # Muestra 50

calcularPuntos(200)

print("Fuera de la función:")
# Al salir de la función, la variable local desaparece y volvemos a ver la global.
print("Bonus:", bonus) # Muestra 100