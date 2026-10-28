from datetime import datetime
from pathlib import Path


def main():
  # 1. Definir la ruta del directorio actual del script
  current_dir = Path(__file__).resolve().parent

  # Archivo donde se guardarán los registros (log)
  log_file_path = current_dir / "registro_calificaciones.log"

  print("=== Registro de Calificaciones ===")
  print("Ingrese una calificación entre 0 y 10 (o escriba 'salir' para terminar).")

  while True:
    entrada = input("Ingrese calificación: ").strip()

    if entrada.lower() == "salir":
      break

    try:
      # 3. Validar que solo se capturen números (enteros)
      calificacion = int(entrada)

      # 2. Validar que las calificaciones estén en un rango de 0 al 10
      if calificacion < 0 or calificacion > 10:
        raise ValueError("La calificación debe estar entre 0 y 10")

      # Si es correcto, podrías guardarlo o continuar,
      # pero según el ejemplo de la imagen, el log registra principalmente los errores o intentos.
      print(f"Calificación registrada exitosamente: {calificacion}")

    except ValueError as e:
      # Capturamos tanto el error de int() como el ValueError lanzado manualmente
      # 4. Estructura de fecha y hora: dd-mm-yyyy h-m-s
      ahora = datetime.now()
      # Formato similar al ejemplo: 27-10-2026 22-21-32
      fecha_hora = ahora.strftime("%d-%m-%Y %H-%M-%S")

      # Mensaje de error a registrar
      mensaje_error = str(e)

      # Determinamos el siguiente número de índice (enumerate) leyendo cuántas líneas existen o escribiendo directamente.
      # Una forma limpia es contar las líneas actuales del archivo log para el índice.
      indice = 1
      if log_file_path.exists():
        with open(log_file_path, "r", encoding="utf-8") as f:
          indice = sum(1 for _ in f) + 1

      # 5. Guardar el registro incluyendo el índice, fecha-hora, tipo y mensaje de error
      registro_linea = (
          f"{indice} | {fecha_hora} | ERROR | {mensaje_error}\n"
      )

      with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(registro_linea)

      print(f"Error registrado en el log: {mensaje_error}")

  # 6. Muestre el archivo log al finalizar
  print("\n--- CONTENIDO DEL ARCHIVO LOG ---")
  if log_file_path.exists():
    with open(log_file_path, "r", encoding="utf-8") as f:
      print(f.read())
  else:
    print("El archivo log está vacío o no ha sido creado.")


if __name__ == "__main__":
  main()