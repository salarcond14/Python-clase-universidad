# Ejercicio 1

# Definimos el texto que simula el nombre de un archivo
texto = "reporte_final_v2.pdf"

# Utilizamos rfind() para buscar la posición de la última aparición del punto (".")
posicion_punto = texto.rfind(".")

# Verificamos si se encontró el punto en la cadena
if posicion_punto != -1:
    # Sumamos 1 a la posición del punto para no incluirlo en el resultado.
    extension = texto[posicion_punto + 1:]
    print("Es un ", extension)
else:
    # Caso contrario, informamos que no hay extensión (no hay punto)
    print("No se encontro ninguna extensión")

print("\n")

# Ejercicio 2

texto = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

# Utilizamos rindex() para encontrar el índice donde comienza la última aparición de la palabra "práctica" dentro de la cadena de texto.
ultima_posicion = texto.rindex("práctica")

# Imprimimos el resultado
print("La ultima posición de la palabra práctica es: ", ultima_posicion)

print("\n")

# Ejercicio 3
frase = str(input("Teclea una frase: "))

# Convertimos toda la frase a minúsculas para ignorar diferencias entre mayúsculas y minúsculas
frase_minusculas = frase.lower()

# Reemplazamos los espacios en blanco por cadenas vacías para eliminarlos
frase_sin_espacios = frase_minusculas.replace(" ", "")

# Mostramos la frase procesada (sin espacios y en minúsculas)
print(frase_sin_espacios)
# Mostramos la frase invertida
print(frase_sin_espacios[::-1])

# Comparamos la frase sin espacios y con todo en minúsculas con su versión invertida
if frase_sin_espacios == frase_sin_espacios[::-1]:
    print("Es un palindromo")
else:
    print("No es un palindromo")

"""
count
Ejemplo nuevo: "mississippi".count("ss")
Resultado: 2

partition
Ejemplo nuevo: "usuario@ejemplo.com".partition("@")
Resultado: ('usuario', '@', 'ejemplo.com')

rpartition
Ejemplo nuevo: "2026-12-31".rpartition("-")
Resultado: ('2026-12', '-', '31')

strip
Ejemplo nuevo: "   Python 3   ".strip()
Resultado: "Python 3"

lstrip
Ejemplo nuevo: "   Python 3   ".lstrip()
Resultado: "Python 3   "

rstrip
Ejemplo nuevo: "   Python 3   ".rstrip()
Resultado: "   Python 3"

isdigit 
Ejemplo nuevo: "2²".isdigit()
Resultado: True

isnumeric 
Ejemplo nuevo: "¾".isnumeric()
Resultado: True

isdecimal 
Ejemplo nuevo: "9876".isdecimal()
Resultado: True

isalnum
Ejemplo nuevo: "Usuario2026".isalnum()
Resultado: True

isspace
Ejemplo nuevo: " \n\t ".isspace()
Resultado: True
"""
