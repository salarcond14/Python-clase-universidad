from enum import Enum, unique

# ==============================================================================
# 1. CATÁLOGO SEGURO CON ENUMS (Llaves constantes e inmutables)
# ==============================================================================
@unique
class TipoPersonaje(Enum):
    GUERRERO = 1
    MAGO = 2
    ARQUERO = 3

# ==============================================================================
# 2. BASE DE DATOS COMPLEMENTARIA (Diccionario de Atributos Auxiliares)
# ==============================================================================
atributosPersonajes = {
    TipoPersonaje.GUERRERO: {"vida": 150, "ataque": 35},
    TipoPersonaje.MAGO:     {"vida": 80,  "ataque": 60},
    TipoPersonaje.ARQUERO:  {"vida": 110, "ataque": 45}
}


# ==============================================================================
# 3. CLASE PRINCIPAL: Personaje (Modelo POO)
# ==============================================================================
class Personaje:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        
        if isinstance(rol, TipoPersonaje):
            self.rol = rol
            
            # Extrae el diccionario interno usando el rol como llave
            datosBase = atributosPersonajes[rol]
            
            # Asigna la vida y el ataque correspondientes
            self.vidaActual = datosBase["vida"]
            self.ataqueBase = datosBase["ataque"]
        else:
            raise ValueError("El rol proporcionado no es válido para un personaje.")

    def mostrarEstadisticas(self):
        print(f"🛡️ Héroe: {self.nombre} | Rol: {self.rol.name} | Vida: {self.vidaActual} HP | Daño: {self.ataqueBase} pts")

    def recibirDanio(self, puntos):
        print(f"💥 ¡{self.nombre} recibe un impacto de {puntos} puntos de daño!")
        
        # Resta los puntos a la salud actual
        self.vidaActual -= puntos
        
        # Valida si la vida cae por debajo o igual a cero
        if self.vidaActual <= 0:
            self.vidaActual = 0
            print(f"💀 {self.nombre} ha caído en combate.\n")
        else:
            print(f"❤️ Vida restante de {self.nombre}: {self.vidaActual} HP\n")


# ==============================================================================
# 4. FLUJO PRINCIPAL INTERACTIVO (Corrida de Consola Simulada)
# ==============================================================================

print("==================================================")
print("===      CATÁLOGO DE PERSONAJES DISPONIBLES    ===")
print("==================================================")

for rolActual in TipoPersonaje:
    datosRol = atributosPersonajes[rolActual]
    print(f"[{rolActual.value}] {rolActual.name:<10} | Vida: {datosRol['vida']} HP | Daño: {datosRol['ataque']} pts")
print("==================================================\n")

try:
    # --- PASO 2: Preguntar al usuario qué personaje quiere elegir ---
    seleccionUsuario = input("Digita el número de la clase que deseas elegir para tu héroe: ")
    
    # Convierte la entrada a entero y mapea al Enum
    numeroClase = int(seleccionUsuario)
    rolElegido = TipoPersonaje(numeroClase) 
    
    nombreHeroe = input("Escribe el nombre de tu personaje: ")
    print("\n--- ¡Personaje Creado con Éxito! ---")
    
    # Instancia el objeto Personaje
    heroeUsuario = Personaje(nombreHeroe, rolElegido)
    heroeUsuario.mostrarEstadisticas()
    
    # --- PASO 3: Generar el enemigo fijo (Un Mago) para el combate ---
    print("--- ¡Un enemigo ha aparecido! ---")
    enemigoMago = Personaje("Mago Oscuro", TipoPersonaje.MAGO)
    enemigoMago.mostrarEstadisticas()
    
    print("==================================================")
    print("===             FASE DE COMBATE                ===")
    print("==================================================")
    
    # --- PASO 4: Preguntar el impacto y validar ---
    entradaImpacto = input(f"Ingresa los puntos de daño que deseas causarle a {enemigoMago.nombre}: ")
    puntosImpacto = int(entradaImpacto)
    
    if puntosImpacto < 0:
        print("❌ Error: No se permiten impactos con valores negativos. El ataque ha fallado.")
    else:
        enemigoMago.recibirDanio(puntosImpacto)

except ValueError:
    print("\n❌ Entrada Inválida: Asegúrate de seleccionar una opción correcta del menú y usar números válidos para el daño.")

print("\n[Sistema]: Simulación interactiva finalizada.")
