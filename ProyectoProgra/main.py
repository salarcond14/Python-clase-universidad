from modelos import Cliente, Tecnico, Computadora, OrdenServicio
from persistencia import GestorArchivos, registrarError
from pathlib import Path

def main():
    print("=== INICIANDO SISTEMA DE REPARACIONES ===\n")
    
    # 1. Creación de objetos de todas las clases (incluidas hijas)
    print("1. Creando objetos del sistema...")
    cliente1 = Cliente("Santiago Alarcón", "4421112233", "Centro Histórico")
    tecnico1 = Tecnico("Luis Alvaréz", "4429998877", "Microelectrónica")
    pc1 = Computadora("Dell", "XPS 13", "Pantalla rota", 16)
    
    orden1 = OrdenServicio("ORD-100", cliente1, tecnico1, pc1)
    
    # 2. Uso de métodos propios del negocio (validación y __str__)
    print("\n2. Usando métodos del negocio...")
    orden1.costoTotal = 2500.00
    print(orden1) # Imprime usando el método __str__
    
    # 3. Guardado de la información en archivo
    print("\n3. Guardando datos en archivo de texto...")
    listaParaGuardar = [orden1.toDict()]
    GestorArchivos.guardarOrdenes(listaParaGuardar)
    print("Datos guardados con éxito en 'ordenes_datos.txt'.")
    
    # 4. Carga desde archivo y comprobación (Reconstrucción de objetos)
    print("\n4. Cargando y reconstruyendo objetos...")
    datosCrudos = GestorArchivos.cargarDatosPreconstruidos()
    
    ordenesReconstruidas = []
    if datosCrudos:
        for dato in datosCrudos:
            # Reconstruimos las instancias originales desde los datos leídos
            c = Cliente(dato["cliente"]["nombre"], dato["cliente"]["telefono"], dato["cliente"]["direccion"])
            t = Tecnico(dato["tecnico"]["nombre"], dato["tecnico"]["telefono"], dato["tecnico"]["especialidad"])
            d = Computadora(dato["dispositivo"]["marca"], dato["dispositivo"]["modelo"], dato["dispositivo"]["falla"], dato["dispositivo"]["ram"])
            
            orden_rec = OrdenServicio(dato["folio"], c, t, d)
            orden_rec.costoTotal = dato["costoTotal"]
            ordenesReconstruidas.append(orden_rec)
            
        print("Objeto reconstruido exitosamente. Coincidencia verificada:")
        print(f"Folio recuperado: {ordenesReconstruidas[0]._folio} | Costo recuperado: ${ordenesReconstruidas[0].costoTotal}")

    # 5. Generación de 3 errores provocados a propósito para el Log
    print("\n5. Provocando errores para bitácora (log_errores.txt)...")
    
    # Error A: Archivo inexistente (FileNotFoundError)
    try:
        rutaFalsa = Path(__file__).resolve().parent / "archivo_borrado.txt"
        with open(rutaFalsa, "r") as f:
            f.read()
    except FileNotFoundError as e:
        registrarError(f"FileNotFoundError: {e}")
        print(" -> FileNotFoundError capturado correctamente.")

    # Error B: Dato inválido (ValueError por precio negativo en el setter)
    try:
        orden1.costoTotal = -50.0 
    except ValueError as e:
        registrarError(f"ValueError: {e}")
        print(" -> ValueError capturado correctamente.")

    # Error C: Búsqueda inexistente (IndexError al consultar registro)
    try:
        listaVacia = []
        consultaMala = listaVacia[10]
    except IndexError as e:
        registrarError(f"IndexError: Intento de acceder a registro inexistente. {e}")
        print(" -> IndexError capturado correctamente.")

    print("\n=== EJECUCIÓN FINALIZADA ===")
    print("Revisa la carpeta actual, se debieron crear 'ordenes_datos.txt' y 'log_errores.txt'.")

if __name__ == "__main__":
    main()