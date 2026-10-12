# Inicializa el contador y lo incrementa hasta encontrar el valor 4.
#Ejercicio 1
c=0
#Mientras 'c' sea menor o igual a 5, el bucle continuará ejecutándose
while c <= 5:
    c+=1 

    # Verificamos si 'c' ha alcanzado el valor de 4
    if(c==4):
        print("rompemos el ciclo cuando c vale", c)
        break
    print(c, "", end="")
else: 
    print("El ciclo ha terminado")

#Ejercicio 2
c=0
# Mientras 'c' sea menor o igual a 5, el bucle continuará ejecutándose
while c <= 5:
    c+=1 

    # Verificamos si 'c' es igual a 3 o igual a 4
    if c==3 or c ==4 :
        continue
    print("c vale ",c)
else:
    print("Se ha completado el ciclo", c)

#Ejercicio 3
nombre = "Gregory"

for letra in nombre:
    # Convertimos la letra a minúscula con lower() para compararla fácilmente
    # Si la letra NO es una vocal, entra al bloque
    if letra.lower() not in "aeiou":
        # Imprimimos la consonante en mayúscula usando upper()
        print(letra.upper())
        

#Ejercico 4
texto = "Dia Anahuac 26 de Agosto"

# Iteramos letra por letra en el texto
for caracter in texto:
    # Si el carácter es un número, rompemos el ciclo
    if caracter.isdigit():
        break
    
    # Imprimimos el carácter. end="" evita el salto de línea.
    print(caracter, end="")
    
print("\n")

#Ejercico 5
text = "pxyxtxhxoxn"

# Iteramos sobre el texto
for caracter in text:
    # Si el carácter es una 'x', saltamos a la siguiente iteración
    if caracter == 'x':
        continue
    
    # Si no es 'x', se imprime la letra sin saltos de línea
    print(caracter, end="")

print("\n")

#Ejercicio 6
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