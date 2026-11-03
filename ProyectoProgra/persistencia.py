import json
from datetime import datetime
from pathlib import Path

# Rutas absolutas para evitar problemas de ubicación
carpeta = Path(__file__).resolve().parent
rutaLog = carpeta / "log_errores.txt"
rutaDatos = carpeta / "ordenes_datos.txt"

def registrarError(mensaje):
    """Método reutilizable que registra cada error en el log con fecha y hora."""
    fechaHora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"{fechaHora} | ERROR | {mensaje}\n"
    with open(rutaLog, "a", encoding="utf-8") as archivo:
        archivo.write(linea)

class GestorArchivos:
    """Concentra toda la lectura y escritura del sistema."""
    
    @staticmethod
    def guardarOrdenes(listaDiccionarios):
        """Guarda la colección de objetos (convertidos a diccionarios) en un archivo de texto."""
        try:
            with open(rutaDatos, "w", encoding="utf-8") as f:
                json.dump(listaDiccionarios, f, indent=4, ensure_ascii=False)
        except PermissionError as e:
            registrarError(f"PermissionError: No se tienen permisos de escritura. {e}")
        except Exception as e:
            registrarError(f"Exception: Error al guardar. {e}")

    @staticmethod
    def cargarDatosPreconstruidos():
        """Carga el texto y devuelve la lista de diccionarios crudos para reconstruir objetos."""
        try:
            with open(rutaDatos, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError as e:
            registrarError(f"FileNotFoundError: Archivo de datos no encontrado. {e}")
            return []