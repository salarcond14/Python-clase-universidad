#Santiago Alarcón Díaz

# Ejercicio 1: según la calificación, muestra la categoría
calificacion = float(input("Ingresa tu calificación: "))
if calificacion >= 9:
    print("Sobresaliente")      # 9 o más
elif calificacion >= 8:
    print("Notable")            # 8 a 8.99
elif calificacion >= 7:
    print("Bien")               # 7 a 7.99
elif calificacion >= 6:
    print("Suficiente")         # 6 a 6.99
elif calificacion >= 5:
    print("Insuficiente")       # 5 a 5.99
else:
    print("Reprobado")          # menos de 5

# Ejercicio 2: aprueba solo si la nota y la asistencia cumplen el requisito
calificacionFinal = float(input("Ingresa tu calificación final: "))
asistencia = float(input("Ingresa tu asistencia: "))
if calificacionFinal >= 6 and asistencia >= 80: # 6 o más y asistencia del 80% o más
    print("aprobado")
else:
    print("reprobado")

# Ejercicio 3: comprueba si la edad permite obtener una entrada gratis.
edad = int(input("Ingresa tu edad: ")) #si es menor de 6 años o mayor de 65, entra gratis
if edad < 6 or edad > 65:
    print("Cumple con la edad para una entrada gratis")
else:
    print("Pago requerido ya que no cumple con la edad para una entrada gratis")


alphabet = "abcdefghijklmnopqrstuvwxyz"

# Comprueba si diferentes caracteres o textos están dentro del alfabeto.
print("f" in alphabet)  # True
print("F" in alphabet)  # False
print("1" in alphabet)  # False
print("ghi" in alphabet)  # True
print("Xyz" in alphabet)  # False

texto = "Programación en Python"

# Comprueba que la palabra Java no aparezca en el texto.
if "Java" not in texto:
    print("La palabra Java no aparece")
