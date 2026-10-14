from random import randint

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.set_edad(edad)

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no puede ser un número negativo.")
        if edad >= 18:
            self.__edad = edad
        else:
            raise ValueError("Edad no válida: El alumno debe ser mayor de edad (>= 18).")


class Contacto:
    def __init__(self, correo, telefono):
        self.set_correo(correo)
        self.set_telefono(telefono)

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        if not telefono.isdigit() or len(telefono) < 7:
            raise ValueError("El teléfono debe contener solo dígitos y tener al menos 7 caracteres.")
        self.__telefono = telefono

    def set_correo(self, correo):
        if "@" not in correo or "." not in correo:
            raise ValueError("El correo electrónico no tiene un formato válido.")
        self.__correo = correo


class Alumno(Persona, Contacto):
    def __init__(self, nombre, edad, correo, telefono):
        Persona.__init__(self, nombre, edad)
        Contacto.__init__(self, correo, telefono)
        self.__matricula = ""
        self.generar_matricula()

    def get_matricula(self):
        return self.__matricula
    
    def generar_matricula(self):
        # Punto 4: Formato 'A' seguido de 4 números aleatorios
        self.__matricula = f"A{randint(1000, 9999)}"

    # Punto 5: Método __str__
    def __str__(self):
        return (
            "--- DATOS DEL ALUMNO ---\n"
            f"Nombre: {self.get_nombre()}\n"
            f"Edad: {self.get_edad()}\n"
            f"Correo: {self.get_correo()}\n"
            f"Telefono: {self.get_telefono()}\n"
            f"Matricula: {self.get_matricula()}"
        )


# --- Punto 6: Ejemplo de uso con Try ... Except ---
if __name__ == "__main__":
    try:
        # Puedes cambiar estos valores para probar las validaciones
        nombre = "Santiago Alarcón"
        edad = 19
        correo = "santiago@correo.com"
        telefono = "9541529207"

        # Creación del objeto Alumno
        alumno1 = Alumno(nombre, edad, correo, telefono)
        
        # Al hacer print(alumno1) se ejecuta automáticamente el método __str__
        print(alumno1)

    except ValueError as e:
        print(f"Error de captura: {e}")
