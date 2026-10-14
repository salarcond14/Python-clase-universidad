from random import *

# CLASE PADRE: Tarjeta
class Tarjeta:
    def __init__(self, titular):
        # Generar un número de tarjeta aleatorio (ej. 4 dígitos o de 16 dígitos)
        self.__numero = randint(1000, 9999)
        self.__titular = titular

    def getId(self):
        return self.__numero

    def getNumero(self):
        return self.__numero

    def getTitular(self):
        return self.__titular


# CLASE HIJA 1: TarjetaCredito
class TarjetaCredito(Tarjeta):
    def __init__(self, titular):
        super().__init__(titular)
        self.__limiteCredito = 50000

    def getLimiteCredito(self):
        return self.__limiteCredito

    def setAumentarLimite(self, opcionTC):
        # Utilizar match para validar si el usuario captura 's' o 'S'
        match opcionTC.strip().lower():
            case 's':
                self.__limiteCredito += 1000
                print("¡Límite de crédito aumentado exitosamente en $1,000!")
            case _:
                print("Se mantiene el límite de crédito actual.")


# CLASE HIJA 2: TarjetaDebito (Herencia simple)
class TarjetaDebito(Tarjeta):
    def __init__(self, titular):
        super().__init__(titular)
        self.__saldo = 15000.0

    def getSaldo(self):
        return self.__saldo

    def setDepositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso de ${cantidad:.2f}")
        else:
            raise ValueError("La cantidad a depositar debe ser mayor a cero.")

    def __str__(self):
        return (f"--- Tarjeta de Débito ---\n"
                f"Número de tarjeta: {self.getId()}\n"
                f"Titular: {self.getTitular()}\n"
                f"Saldo actual: ${self.getSaldo():.2f}")


# CLASE HIJA MULTINIVEL: TarjetaDescuento
class TarjetaDescuento(TarjetaCredito):
    def __init__(self, titular):
        super().__init__(titular)
        
        # Opciones disponibles de colores y descuentos
        colores_beneficios = [
            ("Azul", 0.05),
            ("Amarillo", 0.07),
            ("Naranja", 0.10)
        ]
        
        # Generar un índice aleatorio entre 0 y 2 usando randint
        indice = randint(0, len(colores_beneficios) - 1)
        
        # Asignar el color y el porcentaje según el índice aleatorio obtenido
        self.__color, self.__porcentaje = colores_beneficios[indice]

    def getPorcentajeDescuento(self):
        return self.__porcentaje

    def mostrarDescuento(self):
        beneficio_porcentaje = int(self.__porcentaje * 100)
        return f"Color asignado: {self.__color} | Beneficio: {beneficio_porcentaje}% de descuento"

    def calcularDescuento(self):
        return self.__porcentaje * 100

    def __str__(self):
        return "Tarjeta número: {}\nTitular: {}\n{}\nLímite de crédito: ${} descuento mensual {:.2f}%".format(
            self.getId(),
            self.getTitular(),
            self.mostrarDescuento(),
            self.getLimiteCredito(),
            self.calcularDescuento())


# PROGRAMA PRINCIPAL CON MENÚ INTERACTIVO
if __name__ == "__main__":
    opcion = 0
    while opcion != 3:
        print("\n================ MENU ================")
        print("1. Tarjeta Crédito con Descuento")
        print("2. Tarjeta Débito")
        print("3. Salir")
        print("======================================")
        try:
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    try:
                        titular = input("Ingrese el nombre del titular de la tarjeta de crédito: ")
                        # Crear objeto TarjetaDescuento (herencia multinivel)
                        tarjeta_desc = TarjetaDescuento(titular)
                        
                        # Mostrar información usando __str__()
                        print("\n--- Información de la Tarjeta ---")
                        print(tarjeta_desc)
                        
                        # Solicitar autorización para aumentar crédito
                        opcionTC = input("\n¿Desea aumentar el límite de crédito en $1,000? (s/n): ")
                        tarjeta_desc.setAumentarLimite(opcionTC)
                        
                        # Mostrar nuevo límite
                        print(f"Nuevo límite de crédito: ${tarjeta_desc.getLimiteCredito()}")
                    except ValueError as error:
                        print(f"Error en los datos ingresados: {error}")

                case 2:
                    try:
                        titular = input("Ingrese el nombre del titular de la tarjeta de débito: ")
                        cantidad = float(input("Ingrese la cantidad a depositar: "))
                        
                        # Crear objeto TarjetaDebito
                        tarjeta_deb = TarjetaDebito(titular)
                        
                        # Realizar depósito
                        tarjeta_deb.setDepositar(cantidad)
                        
                        # Mostrar saldo final e información
                        print("\n" + str(tarjeta_deb))
                    except ValueError as error:
                        print(f"Error: {error}")

                case 3:
                    print("\nSaliendo del sistema. ¡Hasta luego!")

                case _:
                    print("\nOpción no válida. Por favor, seleccione una opción del 1 al 3.")

        except ValueError:
            print("\nError: Debe ingresar un número entero válido para seleccionar una opción del menú.")
