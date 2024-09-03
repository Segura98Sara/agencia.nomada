import unicodedata
from datetime import datetime

# Funciones de bienvenida y menú principal
def saludo_bienvenida():
    nombre = input("¡Si nos visitaste es porque quieres viajar! Por favor, ingresa tu nombre: ")
    print(f"\n¡Hola {nombre.capitalize()}! Bienvenidx a Mochila Nómada.\n")
    quienes_somos()

def quienes_somos():
    descripcion = """
    Mochila Nómada es una agencia dedicada a ofrecer experiencias únicas de viaje,
    somos tu compañero de viajes ideal. Ofrecemos las mejores opciones en vuelos,
    alojamiento, traslados y paquetes turísticos para que tu experiencia sea inolvidable.
    """
    print(descripcion)
    menu_principal()

def menu_principal():
    opciones = {
        '1': 'Vuelos',
        '2': 'Alojamiento',
        '3': 'Traslados',
        '4': 'Paquetes',
        '5': 'Clientes',
        '6': 'Salir'
    }
    print("¿Qué te interesa? Selecciona una opción:")
    for key, value in opciones.items():
        print(f"{key}. {value}")
    
    eleccion = input("\nIngresa el número de la opción deseada: ")
    
    if eleccion == '1':
        reservar_vuelo()
    elif eleccion == '2':
        reservar_alojamiento()
    elif eleccion == '3':
        calcular_traslado()
    elif eleccion == '4':
        seleccionar_paquete()
    elif eleccion == '5':
        gestionar_clientes()
    elif eleccion == '6':
        print("\n¡Gracias por visitar Mochila Nómada! ¡Hasta pronto!\n")
    else:
        print("\nOpción no válida. Por favor, intenta de nuevo.\n")
        menu_principal()

# Funciones de reservas de vuelos
def formato_fecha(fecha):
    """Función que recibe una fecha en formato DDMMAAAA y la formatea como DD/MM/AAAA"""
    if len(fecha) == 8 and fecha.isdigit():
        return f"{fecha[:2]}/{fecha[2:4]}/{fecha[4:]}"
    else:
        print("Formato de fecha incorrecto. Por favor, ingresa la fecha en el formato DDMMAAAA.")
        return None

def reservar_vuelo():
    print("\n** Reserva tu Vuelo **\n")
    origen = input("Ciudad de origen: ")
    destino = input("Ciudad de destino: ")
    
    fecha_salida = None
    while not fecha_salida:
        fecha_salida_input = input("Fecha de salida (DDMMAAAA): ")
        fecha_salida = formato_fecha(fecha_salida_input)
    
    fecha_regreso = None
    while not fecha_regreso:
        fecha_regreso_input = input("Fecha de regreso (DDMMAAAA): ")
        fecha_regreso = formato_fecha(fecha_regreso_input)
        
    pasajeros = None
    while not pasajeros:
        pasajeros_input = input("Número de pasajeros: ")
        if pasajeros_input.isdigit() and int(pasajeros_input) > 0:
            pasajeros = int(pasajeros_input)
        else:
            print("Por favor, ingresa un número válido de pasajeros.")
    
    detalles_vuelo = {
        'Origen': origen.title(),
        'Destino': destino.title(),
        'Fecha de Salida': fecha_salida,
        'Fecha de Regreso': fecha_regreso,
        'Pasajeros': pasajeros
    }
    
    print("\nVerificando disponibilidad de vuelos...\n")
    
    # Simulación de búsqueda de vuelos disponibles en pesos colombianos
    vuelos_disponibles = [
        {'Aerolínea': 'AirWays', 'Precio': 500000},
        {'Aerolínea': 'SkyFlight', 'Precio': 450000},
        {'Aerolínea': 'FlyHigh', 'Precio': 480000}
    ]
    
    print("Vuelos disponibles:")
    for idx, vuelo in enumerate(vuelos_disponibles, 1):
        print(f"{idx}. {vuelo['Aerolínea']} - ${vuelo['Precio']} COP")
    
    seleccion = input("\nSelecciona el número del vuelo que deseas reservar: ")
    
    if seleccion.isdigit() and 1 <= int(seleccion) <= len(vuelos_disponibles):
        vuelo_elegido = vuelos_disponibles[int(seleccion) - 1]
        detalles_vuelo.update(vuelo_elegido)
        confirmar_reserva(detalles_vuelo)
    else:
        print("\nSelección no válida. Por favor, intenta de nuevo.\n")
        reservar_vuelo()

def confirmar_reserva(detalles):
    print("\n** Detalles de tu Reserva **")
    for key, value in detalles.items():
        print(f"{key}: {value}")
    
    confirmacion = input("\n¿Deseas confirmar tu reserva? (si/no): ")
    
    if confirmacion.lower() == 'si':
        print("\n¡Tu reserva ha sido confirmada exitosamente! Gracias por confiar en Mochila Nómada.\n")
    elif confirmacion.lower() == 'no':
        print("\nReserva cancelada. Regresando al menú principal...\n")
        menu_principal()
    else:
        print("\nOpción no válida. Por favor, intenta de nuevo.\n")
        confirmar_reserva(detalles)

# Funciones de alojamiento
def formato_fecha_alojamiento(fecha):
    """Función que recibe una fecha en formato DD/MM/AAAA y la convierte a un objeto datetime"""
    try:
        return datetime.strptime(fecha, "%d/%m/%Y")
    except ValueError:
        print("Formato de fecha incorrecto. Por favor, ingresa la fecha en el formato DD/MM/AAAA.")
        return None

def reservar_alojamiento():
    print("\n** Reserva de Alojamiento **\n")
    destino = input("¿Dónde deseas alojarte? (Cartagena, Medellín, Bogotá, Cali, Santa Marta): ").capitalize()
    
    entrada = None
    while not entrada:
        entrada_input = input("Ingrese la fecha de entrada (DD/MM/AAAA): ")
        entrada = formato_fecha_alojamiento(entrada_input)
    
    salida = None
    while not salida:
        salida_input = input("Ingrese la fecha de salida (DD/MM/AAAA): ")
        salida = formato_fecha_alojamiento(salida_input)
    
    if salida <= entrada:
        print("La fecha de salida debe ser después de la fecha de entrada.")
        return
    
    dias = (salida - entrada).days
    
    if dias <= 0:
        print("La fecha de salida debe ser después de la fecha de entrada.")
        return
    
    precio_por_dia = 100000
    costo_total = precio_por_dia * dias
    
    print(f"\nEl costo total de alojamiento en {destino} para {dias} días es: ${costo_total:,} pesos colombianos")
    
    confirmar_reserva_alojamiento(destino, entrada.strftime("%d/%m/%Y"), salida.strftime("%d/%m/%Y"), costo_total)

def confirmar_reserva_alojamiento(destino, entrada, salida, costo_total):
    print(f"\n** Detalles de tu Reserva de Alojamiento **")
    print(f"Destino: {destino}")
    print(f"Fecha de Entrada: {entrada}")
    print(f"Fecha de Salida: {salida}")
    print(f"Costo Total: ${costo_total:,} pesos colombianos")
    
    confirmacion = input("\n¿Deseas confirmar tu reserva de alojamiento? (si/no): ")
    
    if confirmacion.lower() == 'si':
        print("\n¡Tu reserva de alojamiento ha sido confirmada exitosamente! Gracias por confiar en Mochila Nómada.\n")
        menu_principal()
    elif confirmacion.lower() == 'no':
        print("\nReserva cancelada. Regresando al menú de alojamiento...\n")
        reservar_alojamiento()  # Regresa a la función de reserva
    else:
        print("\nOpción no válida. Por favor, intenta de nuevo.\n")
        confirmar_reserva_alojamiento(destino, entrada, salida, costo_total)

# Funciones de traslados
def normalizar_texto(texto):
    """Eliminar tildes y convertir a minúsculas"""
    texto = texto.lower() 
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8') 
    return texto

def calcular_tarifa(destino):
    tarifas = {
        'centro': 25000,
        'norte': 35000,
        'sur': 35000,
        'area metropolitana': 35000,
        'hotel a aeropuerto': 50000,
        'aeropuerto hotel': 50000
    }
    return tarifas.get(destino, 0)  # Regresa 0 si el destino no está en la lista

def aplicar_descuento(tarifa, descuento=0.10):
    return tarifa * (1 - descuento)

def calcular_traslado():
    # Preguntas al usuario
    destino = normalizar_texto(input("\nIngresa el destino del traslado (Centro, Norte, Sur, Área Metropolitana, Hotel a Aeropuerto, Aeropuerto a Hotel): "))
    tipo_traslado = normalizar_texto(input("¿Deseas un traslado en (van, autobús, auto privado)? "))
    ida_regreso = normalizar_texto(input("¿Deseas traslado de (solo ida, ida y vuelta)? "))
    descuento = input("¿Deseas aplicar un descuento del 10%? (si/no): ")
    
    tarifa_base = calcular_tarifa(destino)
    
    if tipo_traslado == 'van' or tipo_traslado == 'autobús':
        tarifa = tarifa_base * 0.50
    else:
        tarifa = tarifa_base
    
    if ida_regreso == 'ida y vuelta':
        tarifa *= 2
    
    if descuento == 'si':
        tarifa = aplicar_descuento(tarifa)
    
    print(f"\nEl costo del traslado es: ${tarifa:,.2f} pesos colombianos.")
    menu_principal()  # Regresa al menú principal

# Funciones de paquetes y clientes
def seleccionar_paquete():
    # Función para manejar la selección de paquetes
    print("\n** Selección de Paquetes Turísticos **")
    # Aquí agregarías lógica para mostrar paquetes y permitir reserva
    menu_principal()

def gestionar_clientes():
    # Función para manejar clientes
    print("\n** Gestión de Clientes **")
    # Aquí agregarías lógica para gestionar clientes
    menu_principal()

# Ejecución inicial
saludo_bienvenida()
