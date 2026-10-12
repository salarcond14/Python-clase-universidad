class Empleado:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = 0
        self.set_edad(edad)  # Validamos la edad mediante el setter
        
    def get_nombre(self):
        return self.__nombre
        
    def get_edad(self):
        return self.__edad
        
    def set_edad(self, edad):
        # Valida que la edad sea un número positivo lógico y mayor o igual a 18
        if edad < 0:
            raise ValueError("La edad no puede ser un número negativo.")
        if edad >= 18:
            self.__edad = edad
            self.es_mayor_de_edad = True
        else:
            raise ValueError("Edad no válida: El empleado debe ser mayor de edad (>= 18).")



class EmpleadoFijo(Empleado):
    def __init__(self, nombre, edad, sueldoMensual, bono):
        # Valida que los valores económicos no sean negativos antes de instanciar
        if sueldoMensual < 0 or bono < 0:
            raise ValueError("El sueldo y el bono no pueden ser valores negativos.")
            
        super().__init__(nombre, edad)  # Hereda los atributos de Empleado
        self.__sueldoMensual = sueldoMensual
        self.__bono = bono
        
    def get_sueldoMensual(self):
        return self.__sueldoMensual
        
    def get_bono(self):
        return self.__bono
        
    def calcularPago(self):
        # Lógica de negocio: si el sueldo supera 20,000, se le suman 1,000 extra al bono
        bono_actual = self.__bono
        if self.__sueldoMensual > 20000:
            bono_actual += 1000
            print("-> [Info] Recibe un bono adicional de 1,000 por sueldo alto.")
        else:
            print("-> [Info] Recibe el bono establecido.")
            
        pago = self.__sueldoMensual + bono_actual
        return pago



class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, edad, horasTrabajadas, pagoPorHora):
        # Validar que las horas y la tarifa no sean negativas
        if horasTrabajadas < 0 or pagoPorHora < 0:
            raise ValueError("Las horas trabajadas y la tarifa no pueden ser negativas.")
            
        super().__init__(nombre, edad)
        self.__horasTrabajadas = horasTrabajadas
        self.__pagoPorHora = pagoPorHora
        
    def get_horasTrabajadas(self):
        return self.__horasTrabajadas
        
    def get_pagoPorHora(self):
        return self.__pagoPorHora
        
    def calcularPago(self):
        # Lógica de horas extras: hasta 40 horas normal, pasadas de 40 se pagan al doble
        if self.__horasTrabajadas <= 40:
            pago = self.__horasTrabajadas * self.__pagoPorHora
        else:
            horas_normales = 40
            horas_extras = self.__horasTrabajadas - 40
            pago = (horas_normales * self.__pagoPorHora) + (horas_extras * self.__pagoPorHora * 2)
            print("-> [Info] Se le pagará el doble por las horas extras trabajadas.")
        return pago



def ejecutar_sistema():
    lista_empleados = []  # Almacena los objetos creados exitosamente
    
    while True:
        print("\n==============================")
        print("   SISTEMA DE EMPLEADOS       ")
        print("==============================")
        print("1. Registrar Empleado Fijo")
        print("2. Registrar Empleado por Hora")
        print("3. Mostrar todos los empleados")
        print("4. Salir")
        
        opcion = input("\nElige una opción (1-4): ")
        
        if opcion == "1":
            print("\n--- Registro de Empleado Fijo ---")
            try:
                # Captura de datos y conversión a tipos numéricos
                nombre = input("Ingresa el nombre: ")
                edad = int(input("Ingresa la edad: "))
                sueldo = float(input("Ingresa el sueldo mensual: "))
                bono = float(input("Ingresa el bono: "))
                
                # Si algún dato es inválido o negativo, lanzará una excepción aquí
                emp_fijo = EmpleadoFijo(nombre, edad, sueldo, bono)
                
                # Solo si todo es correcto, se añade a la lista
                lista_empleados.append(emp_fijo)
                print(f"¡Éxito! Empleado registrado. Pago total: ${emp_fijo.calcularPago()}")
                
            except ValueError as e:
                # Captura tanto errores de tipo (letras en vez de números) como valores negativos/edades inválidas
                print(f"\n[ERROR DE VALIDACIÓN]: {e}")
                print("El registro ha sido cancelado. Intente nuevamente.")
            
        elif opcion == "2":
            print("\n--- Registro de Empleado por Hora ---")
            try:
                nombre = input("Ingresa el nombre: ")
                edad = int(input("Ingresa la edad: "))
                horas = int(input("Ingresa las horas trabajadas: "))
                tarifa = float(input("Ingresa la tarifa por hora: "))
                
                emp_hora = EmpleadoPorHora(nombre, edad, horas, tarifa)
                
                lista_empleados.append(emp_hora)
                print(f"¡Éxito! Empleado registrado. Pago total: ${emp_hora.calcularPago()}")
                
            except ValueError as e:
                print(f"\n[ERROR DE VALIDACIÓN]: {e}")
                print("El registro ha sido cancelado. Intente nuevamente.")
            
        elif opcion == "3":
            print("\n--- Lista de Empleados Registrados ---")
            if not lista_empleados:
                print("No hay empleados registrados todavía.")
            else:
                for i, emp in enumerate(lista_empleados, 1):
                    tipo = "Empleado Fijo" if isinstance(emp, EmpleadoFijo) else "Empleado por Hora"
                    print(f"{i}. Nombre: {emp.get_nombre()} | Tipo: {tipo} | Pago Total: ${emp.calcularPago()}")
                    
        elif opcion == "4":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("\n[Error] Opción no válida. Por favor, elige un número del 1 al 4.")

# Punto de entrada principal del programa
if __name__ == "__main__":
    ejecutar_sistema()
