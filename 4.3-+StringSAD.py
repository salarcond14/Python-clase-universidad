#Ejercicio 1
palabra = input("Digite una palabra: ")
resultado = ",".join(palabra)

print(resultado)

#Ejercicio 2
texto = "Contratar expertos en PYTHON es lo de HOY"
texto_minusculas = texto.lower()
texto_separado = texto_minusculas.split(" ")
texto_mayusculas = [palabra.capitalize() for palabra in texto_separado]
resultado = " ".join(texto_mayusculas)
print(resultado)

#Ejercicio 3
# Lista inicial
lista = [1, 2, 3, 4, 5]

# En una lista de 5 elementos, la mitad (5 // 2) da el índice 2 (que es el número 3)
posicion_central = len(lista) // 2

# Guardamos la lista previa en texto para mostrarla bonita con .join
lista_anterior = [str(1), str(2), str(3), str(4), str(5)]
print("Lista anterior:", ", ".join(lista_anterior))

nuevo_numero = int(input("Ingresa un número entero para el centro: "))
lista[posicion_central] = nuevo_numero # Reemplazamos el elemento en la posición central con el nuevo número

print("Lista actualizada:", lista)

lista.pop()
print("Lista sin el último elemento:", lista)

nuevo_elemento = int(input("Ingresa un nuevo número para la lista: "))
lista.append(nuevo_elemento) # Agregamos el nuevo elemento al final de la lista
print("Lista final:", lista)

longitud = len(lista)
print("La longitud de la lista es:", longitud)

buscar = int(input("Ingresa un número para buscar: "))

if buscar in lista:
    print("El número se encontró en la lista.")
else:
    print("El número NO se encontró en la lista.")
