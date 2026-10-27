#Ejericio 1
listaFrutas = ["manzana", "pera", "uva","mango", "plátano", "fresa"]
resultadoImpar = listaFrutas[1::2]
ultimPalabra = listaFrutas[-1]
for i, fruta in enumerate(listaFrutas, start = 1):
    print(f"{i}. {fruta}")

print("\n")

for i, fruta in enumerate(resultadoImpar, start = 1):   
    print(f"{i}. {fruta}")

print("\n")

#Imprimir Ultima palabra de la lista y su posición en la lista
for i, fruta in enumerate(listaFrutas, start = 1):
    if fruta == ultimPalabra:
        print(f"{i}. {fruta} (última palabra)")
    else:
        print(f"{i}. {fruta}")

#Ejercicio 2 
import os
import random
import sys


class Estudiante:
  def __init__(self, nombre, carrera, matricula=None):
    # Atributos privados (usando doble guion bajo)
    self.__matricula = (
        matricula
        if matricula
        else f"A{random.randint(10000, 99999)}"  # Prefijo A + 5 dígitos aleatorios
    )
    self.__nombre = nombre
    self.__carrera = carrera

  # Métodos públicos para acceder a los atributos privados (Getters)
  @property
  def matricula(self):
    return self.__matricula

  @property
  def nombre(self):
    return self.__nombre

  @property
  def carrera(self):
    return self.__carrera

  def __str__(self):
    return f"Matrícula: {self.__matricula} | Nombre: {self.__nombre} | Carrera: {self.__carrera}"

  def to_file_format(self):
    return f"{self.__matricula},{self.__nombre},{self.__carrera}\n"


def obtener_ruta_archivo():

  directorio_actual = os.path.dirname(os.path.abspath(__file__))
  return os.path.join(directorio_actual, "alumnos.txt")


def agregar_estudiante():
  print("\n--- Agregar Estudiante ---")
  nombre = input("Ingrese el nombre del estudiante: ").strip()
  carrera = input("Ingrese la carrera del estudiante: ").strip()

  estudiante = Estudiante(nombre, carrera)
  ruta = obtener_ruta_archivo()

  try:
    # El archivo se crea automáticamente si no existe al abrirlo en modo 'a' o 'w[span_5](start_span)'[span_5](end_span)
    with open(ruta, "a", encoding="utf-8") as archivo:
      archivo.write(estudiante.to_file_format())
    print(
        f"¡Estudiante agregado con éxito! Matrícula asignada:"
        f" {estudiante.matricula}"
    )
  except Exception as e:
    sys.stderr.write(f"Error al escribir en el archivo: {e}\n")


def mostrar_estudiantes():
  print("\n--- Mostrar todos los estudiantes ---")
  ruta = obtener_ruta_archivo()

  try:
    if not os.path.exists(ruta):
      raise FileNotFoundError("El archivo alumnos.txt no existe.")

    with open(ruta, "r", encoding="utf-8") as archivo:
      lineas = archivo.readlines()
      if not lineas:
        print("No hay estudiantes registrados en el archivo.")
        return

      # Uso de enumerate requerido por el ejercicio[span_7](start_span)[span_7](end_span)
      for indice, linea in enumerate(lineas, start=1):
        datos = linea.strip().split(",")
        if len(datos) == 3:
          mat, nom, car = datos
          print(
              f"{indice}. Matrícula: {mat} | Nombre: {nom} | Carrera: {car}"
          )

  except FileNotFoundError as e:
    sys.stderr.write(f"Error: {e}\n")
  except Exception as e:
    sys.stderr.write(f"Error al leer el archivo: {e}\n")


def buscar_estudiante():
  print("\n--- Buscar estudiante por matrícula ---")
  ruta = obtener_ruta_archivo()

  try:
    if not os.path.exists(ruta):
      raise FileNotFoundError("El archivo alumnos.txt no existe.")

    entrada = input(
        "Ingrese los 5 dígitos numéricos de la matrícula (ej. 12345): "
    ).strip()

    # Manejo de error: Entrada no numérica o longitud incorrecta
    if not entrada.isdigit() or len(entrada) != 5:
      raise ValueError(
          "Entrada no numérica o inválida. Debe ingresar exactamente 5 dígitos."
      )

    matricula_buscada = f"A{entrada}"
    encontrado = False

    with open(ruta, "r", encoding="utf-8") as archivo:
      for linea in archivo:
        datos = linea.strip().split(",")
        if len(datos) == 3:
          mat, nom, car = datos
          if mat == matricula_buscada:
            print(
                f"\n¡Estudiante encontrado!\nMatrícula: {mat}\nNombre:"
                f" {nom}\nCarrera: {car}"
            )
            encontrado = True
            break

    # Manejo de error: Matrícula no encontrada
    if not encontrado:
      raise ValueError(f"Matrícula no encontrada: {matricula_buscada}")

  except FileNotFoundError as e:
    sys.stderr.write(f"Error: {e}\n")
  except ValueError as e:
    sys.stderr.write(f"Error: {e}\n")
  except Exception as e:
    sys.stderr.write(f"Error inesperado: {e}\n")


def main():
  while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Buscar estudiante por matricula")
    print("4. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
      agregar_estudiante()
    elif opcion == "2":
      mostrar_estudiantes()
    elif opcion == "3":
      buscar_estudiante()
    elif opcion == "4":
      print("Saliendo del programa...")
      break
    else:
      sys.stderr.write(
          "Opción inválida. Por favor, elija una opción del 1 al 4.\n"
      )


if __name__ == "__main__":
  main()
