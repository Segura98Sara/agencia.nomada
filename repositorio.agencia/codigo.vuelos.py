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
        '5': 'Salir'
    }
    print("¿Qué te interesa? Selecciona una opción:")
    for key, value in opciones.items():
        print(f"{key}. {value}")
    
    eleccion = input("\nIngresa el número de la opción deseada: ")
    
    if eleccion == '1':
        reservar_vuelo()
    elif eleccion == '2':
        print("\nModulo de Alojamiento próximamente disponible.\n")
        menu_principal()
    elif eleccion == '3':
        print("\nModulo de Traslados próximamente disponible.\n")
        menu_principal()
    elif eleccion == '4':
        print("\nModulo de Paquetes próximamente disponible.\n")
        menu_principal()
    elif eleccion == '5':
        print("\n¡Gracias por visitar Mochila Nómada! ¡Hasta pronto!\n")
    else:
        print("\nOpción no válida. Por favor, intenta de nuevo.\n")
        menu_principal()

def reservar_vuelo():
    print("\n*** Reserva tu Vuelo ***\n")
    origen = input("Ciudad de origen: ")
    destino = input("Ciudad de destino: ")
    fecha_salida = input("Fecha de salida (DD/MM/AAAA): ")
    fecha_regreso = input("Fecha de regreso (DD/MM/AAAA): ")
    pasajeros = input("Número de pasajeros: ")
    
    detalles_vuelo = {
        'Origen': origen.title(),
        'Destino': destino.title(),
        'Fecha de Salida': fecha_salida,
        'Fecha de Regreso': fecha_regreso,
        'Pasajeros': pasajeros
    }
    
    print("\nVerificando disponibilidad de vuelos...\n")
    
    # Simulación de búsqueda de vuelos disponibles
    vuelos_disponibles = [
        {'Aerolínea': 'AirWays', 'Precio': 500000},
        {'Aerolínea': 'SkyFlight', 'Precio': 450000},
        {'Aerolínea': 'FlyHigh', 'Precio': 480000}
    ]
    
    print("Vuelos disponibles:")
    for idx, vuelo in enumerate(vuelos_disponibles, 1):
        print(f"{idx}. {vuelo['Aerolínea']} - ${vuelo['Precio']}  COP")
    
    seleccion = input("\nSelecciona el número del vuelo que deseas reservar: ")
    
    if seleccion.isdigit() and 1 <= int(seleccion) <= len(vuelos_disponibles):
        vuelo_elegido = vuelos_disponibles[int(seleccion)-1]
        detalles_vuelo.update(vuelo_elegido)
        confirmar_reserva(detalles_vuelo)
    else:
        print("\nSelección no válida. Por favor, intenta de nuevo.\n")
        reservar_vuelo()

def confirmar_reserva(detalles):
    print("\n*** Detalles de tu Reserva ***")
    for key, value in detalles.items():
        print(f"{key}: {value}")
    
    confirmacion = input("\n¿Deseas confirmar tu reserva? (si/no): ")
    
    if confirmacion.lower() == 's':
        print("\n¡Tu reserva ha sido confirmada exitosamente! Gracias por confiar en Mochila Nómada.\n")
    elif confirmacion.lower() == 'n':
        print("\nReserva cancelada. Regresando al menú principal...\n")
        menu_principal()
    else:
        print("\nOpción no válida. Por favor, intenta de nuevo.\n")
        confirmar_reserva(detalles)

if __name__ == "__main__":
    saludo_bienvenida()

