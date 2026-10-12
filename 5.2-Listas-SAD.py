#Ejercico 1
my_list = [1, None, True, "Soy una cadena", 256,0]

#Ejercicio 2
print(my_list[3])
print(my_list[-1])

my_list[1] = '?'
print(my_list)

my_list.insert(0,"primero")
my_list.append("ultimo")
print(my_list) # output: ['primero', 1, '?', True, 'Soy una cadena', 256, 0, 'ultimo']

#Ejercicio 3
my_list = [1, 'a', ["lista",64,[0,1],False]]

#Ejercicio 4
my_list=[1,2,3,4]
del my_list[2]
print(my_list) # output: [1, 2, 4]

del my_list
print (my_list) # output: NameError: name 'my_list' is not defined

#Ejercicio 5
my_list = ["blanco","purpura","azul","amarillo","verde"]
for color in my_list:
    print(color)

#Ejercicio 6
#Encontrar el valor mayor en la lista [17,3,11,5,1,9,7,15,13]
my_list = [17,3,11,5,1,9,7,15,13]
numeroMayor = my_list[0]
for num in my_list:
    if num > numeroMayor:
        numeroMayor = num
print(numeroMayor) # output: 17

#Ejercicio 7
#Encontrar la ubicación del elemento 5 dentro de una lista [17,3,11,5,1,9,7,15,13]
my_list = [17,3,11,5,1,9,7,15,13]
ubi = -1
for i in range(len(my_list)):
    if my_list[i] == 5:
        ubi = i
        break
print(ubi) # output: 3

#Ejercicio 8
# Definimos los números sorteados (ganadores)
ganadores = [5, 11, 9, 42, 3, 49]

# Lista para guardar los números que ingrese el usuario
apuesta = []

print("Ingrese 6 números entre 1 y 49:")

# Capturamos 6 números del usuario
for i in range(6):
    num = int(input(f"Número {i+1}: "))
    apuesta.append(num)

# Contamos los aciertos
aciertos = 0

for num_apuesta in apuesta:
    for num_ganador in ganadores:
        if num_apuesta == num_ganador:
            aciertos += 1
            break  # Salimos para no contar duplicados si el usuario repite un número acertado

# Mostramos los resultados
print("Números sorteados:", ganadores)
print("Tu apuesta:", apuesta)
print("Aciertos:", aciertos)