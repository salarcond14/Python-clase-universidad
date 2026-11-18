import math

#Ejercicio 1

class Circulo:
    def __init__(self, radio,):
        self.radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.deleter
    def radio(self):
        del self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser mayor que cero.")
        self._radio = valor

    def calcular_area(self):
        """Calcula el área del círculo."""
        return math.pi * (self.radio ** 2)   

def main():
    """Función principal para probar el funcionamiento de la clase Circulo."""
    try:
        # 1. Prueba con un valor válido
        circulo1 = Circulo(5)
        print(f"Radio inicial: {circulo1.radio}")
        print(f"Área del círculo: {circulo1.calcular_area():.2f}")

        # 2. Modificación válida usando el setter
        circulo1.radio = 10
        print(f"\nNuevo radio: {circulo1.radio}")
        print(f"Nueva área: {circulo1.calcular_area():.2f}")

        # 3. Prueba de validación (debe lanzar la excepción)
        print("\nIntentando asignar un radio negativo...")
        circulo1.radio = -3

    except ValueError as error:
        print(f"Error capturado correctamente: {error}")


if __name__ == "__main__":
    main()

#Ejercicio 2
class CuentaBancaria:
    """Clase que representa una cuenta bancaria con control de saldo e interés anual."""

    def __init__(self, titular: str, saldo_inicial: float):
       
        self.titular = titular
        # Se asigna a self.saldo para ejecutar la validación del setter desde el inicio
        self.saldo = saldo_inicial

    @property
    def saldo(self):
        
        return self.__saldo

    @saldo.setter
    def saldo(self, valor: float):
        
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self.__saldo = valor

    @property
    def interesAnual(self):
        
        return self.__saldo * 0.05


def main():
    """Función principal que solicita los datos al usuario y muestra el resumen de la cuenta."""
    try:
        titular = input("Titular de la cuenta: ")
        saldo_inicial = float(input("Saldo inicial: "))

        cuenta = CuentaBancaria(titular, saldo_inicial)

        print(f"Titular: {cuenta.titular}")
        print(f"Saldo: ${cuenta.saldo:.2f}")
        print(f"Interés anual: ${cuenta.interesAnual:.2f}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()

    