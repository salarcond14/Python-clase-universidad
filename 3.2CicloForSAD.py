#Ejercicio 1
nombre = "Gregory"

for letra in nombre:
    # Convertimos la letra a minúscula con lower() para compararla fácilmente
    # Si la letra NO es una vocal, entra al bloque
    if letra.lower() not in "aeiou":
        # Imprimimos la consonante en mayúscula usando upper()
        print(letra.upper())
        

#Ejercico 2
texto = "Dia Anahuac 26 de Agosto"

# Iteramos letra por letra en el texto
for caracter in texto:
    # Si el carácter es un número, rompemos el ciclo
    if caracter.isdigit():
        break
    
    # Imprimimos el carácter. end="" evita el salto de línea.
    print(caracter, end="")
    
print("\n")

#Ejercico 3
text = "pxyxtxhxoxn"

# Iteramos sobre el texto
for caracter in text:
    # Si el carácter es una 'x', saltamos a la siguiente iteración
    if caracter == 'x':
        continue
    
    # Si no es 'x', se imprime la letra sin saltos de línea
    print(caracter, end="")

print("\n")

#Ejercicio 4
digitos = "0165031806510" 

# Iteramos sobre cada número en la cadena de texto
for numero in digitos:
    # Si el número es un cero, imprimimos 'x'
    if numero == "0":
        print("x", end="")
    # De lo contrario, imprimimos el número normal
    else:
        print(numero, end="")

print("\n")