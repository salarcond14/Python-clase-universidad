# Solicita una contraseña y comprueba sus condiciones básicas.
contra=input("Ingrese la contraseña, debe tener al menos 8 caracteres y no contener espacios> ")

if(len(contra)<8 or " "in contra):
    print("Tu contraseña debe tener por lo menos 8 caracteres y no contener espacios")
elif(contra=="anahuac999"):
    print("Invalida!")
else:
    print("Valida!")

# Ejercicio 2: comprueba si la persona cumple los requisitos del puesto.

edad=int(input("Ingrese su edad: "))
experiencia=int(input("Ingrese su experiencia laboral en años: "))
if(edad>=38 or (edad>=28 and experiencia>=2)):
    print("Cumple con los requisitos para el puesto")
else:
    print("No cumple con los requisitos para el puesto")

# Ejercicio 3: calcula el costo de envío según sus características.
peso=float(input("Ingrese su peso en kg: ")) #Un float por si el peso no es entero
distancia=float(input("Ingrese la distancia en km: ")) #Float por que se cuentan los decimales
fragilidad=input("Ingrese si el paquete es frágil (si/no): ") #String por que se ingresa una opción
costo=0
if(peso<=5):
    costo+=50 #Se suma 50 al costo si el peso es menor o igual a 5 kg y así con las demás condiciones
else:
    costo+=200

if(distancia<=50):
    costo+=30
else:
    costo+=70

if(fragilidad=="si"):
    costo+=100
else: 
    costo+=50

# Calcula y suma el IVA del 16% al costo del envío.
Iva=float(costo*0.16) #Al costo se le suma el 16% de iva
subtotal=float(costo+Iva) #Se suma el costo con el iva para obtener el subtotal
print ("El costo total del envío es: ", subtotal ,"con iva incluido") #Se imprime el costo total del envío con iva incluido