# Ejemplos básicos de impresión, variables, tipos de datos y ciclos.
# Esta parte está dentro de una cadena multilínea y no se ejecuta.
"""
print("¡¡Hola Mundo!!")
print(2) 
print(3.1416) 
print(True>False)
print(True<False)

nombre="Jimmy"
edad=25
print("Me llamo", nombre, "y tengo", edad, "años.")
semanas=4
print("En", semanas, "semanas hay", 7 * semanas, "dias")

var=2
var=3
print(var)

a='1'
b="1"
print(a+b)

print('Dime tu nombre: ')
nombre = input()
print('Hello', nombre)

a=6
b=3
a/=2*b
print(a)

edad = input('dime tu edad: ')
print('Tu tienes', edad, 'años.')

x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

edad1 = input('dime tu edad: ')
print(type(edad1))
print(edad1 +1)

#Ejemplo de expresiones
3+5 
"Hola " + "mundo"

num1 =5.8
print(type(num1))
num2=int(num1)
print(type(num2))

int("El tipo de valor de la variable num 1 es " + str(num1) + " y el tipo de valor de la variable num2 es " + str(num2))
int("El tipo de valor de la variable num 1 es", num1, "y el tipo de valor de la variable num2 es", num2)
int(f"El tipo de valor de la variable num1 es {num1} y el de num2 es {num2}")

c = 0
while c <= 5:
    print("c vale", c)
    c += 1

par = 0
impar = 0
numero = int(input("Dime un número o 0 para salir: "))
while numero !=0:
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    numero = int(input("Dime un número o 0 para salir: "))
print("Has introducido", par, "números pares y", impar, "números impares.")


# Repite el ciclo y lo detiene cuando el contador llega a 4.
c=0
while c <= 5:
    c+=1 
    if(c==4):
        print("rompemos el ciclo cuando c vale", c)
        break
    print(c, "", end="")
else:
    print("El ciclo ha terminado")"""

