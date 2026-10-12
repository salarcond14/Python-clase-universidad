import datetime
import time

# Ejercicio 1
def ejecutar_ejercicio_1():
    cociente = 0
    try:
        numerador = float(input("Ingrese el numerador: "))
        denominador = float(input("Ingrese el denominador: "))
        cociente = numerador / denominador
    except ValueError:
        print("Error: Debe ingresar un número válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print(f"El cociente es: {cociente}")
    finally:
        print("Fin del programa.\n")



# Ejercicio 2 
def ejecutar_ejercicio_2():
    registrar_calificacion = input("Ingrese su calificación (0-10): ")
    try:
        calificacion = float(registrar_calificacion)
        if calificacion < 0 or calificacion > 10:
            raise ValueError("La calificación debe estar entre 0 y 10.")
    except ValueError as e:
        print(f"Error: {e}\n")
    else:
        print(f"La calificación es: {calificacion}\n")


# Ejercicio 3
class RelojDigital:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        self.obtener_hora()

    def obtener_hora(self):
        ahora = datetime.datetime.now()
        self.hora = ahora.hour
        self.minuto = ahora.minute
        self.segundo = ahora.second

    def mostrar_fecha(self):
        ahora = datetime.datetime.now()
        return ahora.strftime("%Y-%m-%d %H:%M:%S")

    def mostrar_saludo(self):
        ahora = datetime.datetime.now()
        if 5 <= ahora.hour < 12:
            return "Buenos días"
        elif 12 <= ahora.hour < 18:
            return "Buenas tardes"
        else:
            return "Buenas noches"

    def mostrar_hora(self):
        print("Presiona Ctrl+C para detener el reloj...")
        try:
            while True:
                self.obtener_hora()
                print(
                    f"\rHora actual: {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}",
                    end="",
                    flush=True,
                )
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nReloj detenido.\n")
if __name__ == "__main__":

    reloj = RelojDigital()
    print(f"Saludo: {reloj.mostrar_saludo()}")
    print(f"Fecha actual: {reloj.mostrar_fecha()}")
    print()
    reloj.mostrar_hora()

# Ejercicio 4
class Cuenta:
    def __init__(self, titular, saldo=5000.0):
        self.titular = titular
        self.saldo = float(saldo)

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError("Fondos insuficientes.")
        self.saldo -= cantidad
        print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")


def ejecutar_ejercicio_4():
    cuenta = Cuenta("Santiago Alarcón", 5000)
    try:
        cantidad_a_retirar = float(input("Ingrese la cantidad a retirar: "))
        cuenta.retirar(cantidad_a_retirar)
    except ValueError as e:
        print(f"Error: {e}\n")


if __name__ == "__main__":

    ejecutar_ejercicio_4()

