# --- CLASES BASE E HIJAS (PERSONAS) ---
class Persona:
    """Clase base para usuarios del sistema."""
    def __init__(self, nombre, telefono):
        self._nombre = nombre
        self._telefono = telefono
        
    @property
    def nombre(self):
        return self._nombre

    def __str__(self):
        return f"{self._nombre} (Tel: {self._telefono})"

class Cliente(Persona):
    def __init__(self, nombre, telefono, direccion):
        super().__init__(nombre, telefono)
        self._direccion = direccion
        
    def __str__(self):
        return f"[Cliente] {super().__str__()} | Dir: {self._direccion}"

class Tecnico(Persona):
    def __init__(self, nombre, telefono, especialidad):
        super().__init__(nombre, telefono)
        self._especialidad = especialidad
        
    def __str__(self):
        return f"[Técnico] {super().__str__()} | Esp: {self._especialidad}"


# --- CLASES BASE E HIJAS (DISPOSITIVOS) ---
class Dispositivo:
    """Clase base para los equipos."""
    def __init__(self, marca, modelo, fallaReportada):
        self._marca = marca
        self._modelo = modelo
        self._fallaReportada = fallaReportada
        
    def __str__(self):
        return f"{self._marca} {self._modelo} - Falla: {self._fallaReportada}"

class Computadora(Dispositivo):
    def __init__(self, marca, modelo, fallaReportada, ram):
        super().__init__(marca, modelo, fallaReportada)
        self._ram = ram
        
    def __str__(self):
        return f"[PC] {super().__str__()} | RAM: {self._ram}GB"

class DispositivoMovil(Dispositivo):
    def __init__(self, marca, modelo, fallaReportada, imei):
        super().__init__(marca, modelo, fallaReportada)
        self._imei = imei
        
    def __str__(self):
        return f"[Móvil] {super().__str__()} | IMEI: {self._imei}"


# --- CLASE GESTORA ---
class OrdenServicio:
    """Clase que asocia cliente, técnico y dispositivo."""
    def __init__(self, folio, cliente, tecnico, dispositivo):
        self._folio = folio
        self._cliente = cliente
        self._tecnico = tecnico
        self._dispositivo = dispositivo
        self._costoTotal = 0.0
        
    @property
    def costoTotal(self):
        return self._costoTotal
        
    @costoTotal.setter
    def costoTotal(self, valor):
        if float(valor) < 0:
            raise ValueError("El costo total de la orden no puede ser negativo.")
        self._costoTotal = float(valor)

    def toDict(self):
        """Convierte el objeto a diccionario para guardarlo."""
        return {
            "folio": self._folio,
            "costoTotal": self._costoTotal,
            "cliente": {"nombre": self._cliente._nombre, "telefono": self._cliente._telefono, "direccion": self._cliente._direccion},
            "tecnico": {"nombre": self._tecnico._nombre, "telefono": self._tecnico._telefono, "especialidad": self._tecnico._especialidad},
            "dispositivo": {"marca": self._dispositivo._marca, "modelo": self._dispositivo._modelo, "falla": self._dispositivo._fallaReportada, "ram": getattr(self._dispositivo, '_ram', None)}
        }
        
    def __str__(self):
        return (f"--- ORDEN {self._folio} ---\n"
                f"1. {self._cliente}\n"
                f"2. {self._tecnico}\n"
                f"3. {self._dispositivo}\n"
                f"Total a pagar: ${self._costoTotal}")  