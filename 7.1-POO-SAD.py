import random


class Estudiante:

    def __init__(self, nombre, calificacion):
        # Atributos: nombre es público; id y calificación son privados
        self.nombre = nombre
        self.__id = random.randint(100000, 999999)
        self.__calificacion = float(calificacion)

    # Getter para la calificación
    def getCalificacion(self):
        return self.__calificacion

    # Setter con validación entre 0 y 10
    def setCalificacion(self, nueva_calificacion):
        if 0 <= nueva_calificacion <= 10:
            self.__calificacion = nueva_calificacion
            print("Calificación actualizada correctamente.")
        else:
            print("La calificación no es válida.")

    # Muestra los datos del estudiante
    def mostrar_informacion(self):
        print("\n----- INFORMACIÓN DEL ESTUDIANTE -----")
        print(f"Nombre: {self.nombre}")
        print(f"Matrícula: {self.__id}")
        print(f"Calificación: {self.__calificacion}\n")

    # Verifica si cumple el requisito para la beca (>= 9.7)
    def verificarBeca(self):
        if self.__calificacion >= 9.7:
            print("Puede obtener una beca de excelencia.")
        else:
            faltante = round(9.7 - self.__calificacion, 1)
            print("No alcanza la calificación para la beca de excelencia.")
            print(f"Le faltan {faltante} puntos para alcanzar 9.7.")


#Registro inicial
nombre_input = input("Ingresa el nombre del estudiante: ")
calif_input = float(input("Ingresa la calificación inicial: "))

estudiante1 = Estudiante(nombre_input, calif_input)

#Mostramos datos y validación inicial de beca
estudiante1.mostrar_informacion()
estudiante1.verificarBeca()

#Actualización de calificación mediante el Setter
nueva_calif = float(
    input("\nIngresa la nueva calificación para actualizar: ")
)
estudiante1.setCalificacion(nueva_calif)

#Mostrar calificación actualizada usando el Getter y nueva verificación
print(f"Calificación actual: {estudiante1.getCalificacion()}")
estudiante1.verificarBeca()