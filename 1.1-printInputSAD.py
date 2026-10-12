#Santiago Alarcón Díaz 

#******Ejercicio 1******
# Convierte la entrada a entero y calcula su cuadrado.
#anything = (input("ingresa un número: "))
# something = anything ** 2.0 
#print(anything, "all cuadro es", something)

anything = int(input("ingresa un número: ")) #Agregamos un int al input para que pueda lleer el valor como un número y no como un string
something = anything ** 2.0 #La variable se eleva a  2.0
print(anything, "all cuadro es", something) #Lo imprime

#******Ejercicio 2******
# Comprueba si el número es mayor o igual que 100.
"""Usando uno de los operadores de comparación en
Python, escribe un programa simple de dos líneas que tome el parámetro n como entrada, que es un entero, 
 e imprime False si n es menor que 100, y True if n es mayor o igual que 100.
> No debes crear ningún bloque if (hablaremos de ellos muy pronto). Prueba tu código usando los datos que te proporcionamos
"""
n = int(input("ingresa un número: "))
print(n>=100)

#******Ejercicio 3******
# Une dos respuestas del usuario en una sola frase.
"""
3.Pide al usuario que responda dos preguntas que requieran una sola palabra cada una 
y que luego le muestre en pantalla esas palabras concatenadas, agregando texto extra 
que complete las respuesta que el usuario te dio.
"""
# Se solicitan dos palabras al usuario
print("¿Cuál es tu letra favorita?")
letra = input()  # lee la letra en la variable
print("¿Cuál es tu inicial?")
inicial = input()  # lee la inicial en la variable
# Concatena las dos palabras
letra_inicial = letra + " " + inicial
# Suma las letras
print("Tu letra favorita es", letra, "y tu inicial es", inicial, "juntas hacen: ", letra_inicial)

#******Ejercicio 4******
# Calcula la comisión del vendedor, que corresponde al 13% de sus ventas.
"""Tú trabajas en una empresa donde los vendedores reciben comisiones del 13% por sus ventas totales, 
y tu jefe quiere que ayudes a los vendedores a calcular sus comisiones creando un programa 
que les pregunte su nombre y cuánto han vendido en este mes.
• Tu programa le va a responder con una frase que incluya su nombre, el monto de sus ventas 
y el monto que le corresponde por las comisiones."""

# Pide el nombre del vendedor
nombre = input("¿Cuál es tu nombre?: ")
# Pide el monto de ventas y convierte a número decimal
ventas = float(input("¿Cuánto has vendido este mes?: "))
# Calcula la comisión
comision = ventas * 0.13
# Muestra el nombre, las ventas y la comisión calculada
print("Hola", nombre, "este mes has vendido un total de", ventas, " tu comisión es de", comision)

#******Ejercicio 5******
# Calcula el área de un triángulo usando su base y su altura.
"""Ahora calcula el área de un triángulo, el usuario debe poder capturar base y altura. 
Se deberán mostrar los tres valores, área, base y altura. Escribe a que corresponde cada valor
que estés mostrando.
"""

# Pide la base del triángulo y convierte a número decimal
base = float(input("Ingresa la base de tu triángulo: "))
# Pide la altura del triángulo y convierte a número decimal
altura = float(input("Ahora ingresa la altura del triángulo: "))
# Calcula el área
area = (base * altura) / 2
# Muestra los tres valores con etiquetas claras
print("La base es:", base)
print("La altura es:", altura)
print("Entonce el área de tu triángulo es:", area)