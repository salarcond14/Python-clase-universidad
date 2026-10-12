#Ejercicio 1:

def factorial(n):
    if n == 1: #the base case (termination condition)
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4)) # output: 24

valor = float(input("Ingrese un número para calcular su factorial: "))
if valor < 0:
    print("El factorial no está definido para números negativos.")
else:
    print("El factorial de", int(valor), "es:", factorial(int(valor)))

#Ejercicio 2:
def cuenta_atras(num):
    num = 1
    if num <= 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooom!")
    return # No imprime el siguiente print, ya que la función termina aquí
    print("Fin de la función", num)


#Ejercicio 3:
import random

def evaluar_jugada(dado1, dado2):
    suma = dado1 + dado2
    if suma <= 6:
        return f"La suma de tus dados es {suma}. Lamentable"
    elif 6 < suma < 10:
        return f"La suma de tus dados es {suma}. Tienes buenas chances"
    else:  # suma >= 10
        return f"La suma de tus dados es {suma}. Parece una jugada ganadora"

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    mensaje = evaluar_jugada(dado1, dado2) # Llama a la función evaluar_jugada con los valores de los dados
    return mensaje

# Prueba de la función
print(lanzar_dados())

#Ejercicio 4:
import random

def buscarPremio(intentos=1):
    premios = ["🍎", "🍌", "🍇", "🎁", "🍉", "🍓"]
    
    # Caso límite de 10 intentos
    if intentos > 10:
        print("Se alcanzó el límite de intentos.")
        return "No se encontró el premio"
    
    # Seleccionar un elemento al azar
    eleccion = random.choice(premios)
    
    if eleccion == "🎁":
        print(f"Intento {intentos}: {eleccion}")
        print("¡Premio encontrado!")
        return intentos
    else:
        print(f"Intento {intentos}: {eleccion}")
        # Llamada recursiva aumentando el contador de intentos
        return buscarPremio(intentos + 1)

# Ejecución de la función
resultado = buscarPremio()
print("Resultado:", resultado)