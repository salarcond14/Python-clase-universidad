# Ejercicio 1: repite el intento hasta adivinar el número secreto.
# Guarda el número que se debe adivinar.
numeroSecreto=999
# Muestra las instrucciones del juego.
print(
    """
    +================================+
    | ¡Bienvenido a mi juego, muggle!|
    | Introduce un numero entero     |
    | y adivina que número he        |
    | elegido para ti.               |
    | ¿Cuál es el número secreto?    | 
    +================================+
    """)
# Pide el primer intento al usuario.
num=int(input("Ingresa tu valor: "))

# Continúa preguntando mientras el número sea incorrecto.
while(num!=numeroSecreto):
    print("¡Ja, ja! !Estás atrapado en un bucle!")
    num=int(input("Vuevle a intentarlo: "))
# Este mensaje aparece cuando el usuario acierta.
print("¡Bien hecho muggle! ¡Has adivinado mi número secreto!")

# Deja una línea en blanco entre ejercicios.
print("")

# Ejercicio 2: muestra un mensaje según la opción elegida.
# Guarda la opción escrita por el usuario.
opcion=input("Elige una opción (1, 2, o 3): ")

# Compara la opción y muestra el mensaje correspondiente.
match (opcion):
    case '1':
        print("Elegiste la opción 1")
    case '2':
        print("Elegiste la opción 2")
    case '3':
        print("Elegiste la opción 3")
    case _:
        print("La opción no válida")

# Deja una línea en blanco entre ejercicios.
print("")

# Ejercicio 3: captura varios números y suma los pares e impares por separado.
# Indica cuántos números se van a capturar.
num=int(input("¿Que números quieres capturar?: "))
# Inicializa el contador y las sumas.
cont=1
contpar=0
contimpar=0

# Repite el proceso hasta capturar la cantidad indicada.
while(cont<=num):
    ing=int(input(f"Captura el numero {cont}: "))
# Comprueba si el número es par o impar y lo suma.
    if (ing % 2 ==0):
        contpar+=ing
    else:
        contimpar+=ing
# Avanza al siguiente número.
    cont+=1
# Muestra las dos sumas obtenidas.
print(f"La suma de los numeros pares es: {contpar}")
print(f"La suma de los numeros impares es: {contimpar}")

# Ejercicio 4: permite intentar la contraseña hasta tres veces.
# Define la contraseña correcta y prepara el control de intentos.
contrasenia = "TodoRojo"
intentos = 0
acertado = False

# Permite como máximo tres intentos.
while intentos < 3:
# Pide una contraseña y cuenta el intento realizado.
    pass_input = input("Ingresa la contraseña: ")
    intentos += 1
    
# Comprueba si la contraseña introducida es correcta.
    match pass_input == contrasenia:
        case True:
            print(f"Contraseña correcta: {pass_input}")
            acertado = True
            break
        case False:
# Si todavía quedan intentos, informa al usuario.
            if intentos < 3:
                print("Incorrecto, intenta de nuevo.")

# Informa del bloqueo si no se acertó la contraseña.
if not acertado:
    print("Bloqueado. Has excedido el número de intentos permitidos.")

# Ejercicio 5: separa los dígitos de un número y calcula su suma.
# Pide el número y usa su valor absoluto para aceptar números negativos.
numero = int(input("Ingresa un número entero: "))
temp = abs(numero)
suma_digitos = 0

# Extrae el último dígito y lo suma hasta terminar el número.
while temp > 0:
    digito = temp % 10
    suma_digitos += digito
# Elimina el último dígito del número.
    temp //= 10

# Muestra la suma final de los dígitos.
print(f"La suma de los dígitos es {suma_digitos}")