# Gestión de Clientes en la consola usando Python

# Diccionario para almacenar perfiles de clientes
clientes = {}

def mostrar_menu():
    print("\n--- Gestión de Clientes ---")
    print("1. Crear perfil de cliente")
    print("2. Ver perfil de cliente")
    print("3. Actualizar perfil de cliente")
    print("4. Ver historial de reservas")
    print("5. crear reserva")
    print("6. ver preferencias y solicitudes especiales")
    print("7. Añadir preferencias y solicitudes especiales")
    print("8. Agregar puntos de fidelización")
    print("9. Ver programa de fidelización")
    print("10. Salir")

def crear_perfil():
    print("\n--- Crear Perfil de Cliente ---")
    nombre = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el correo electrónico del cliente: ")
    clientes[email] = {
        'nombre': nombre,
        'historial_reservas': [],
        'preferencias': [],
        'puntos_fidelizacion': 0
    }
    print(f"Perfil de {nombre} creado exitosamente.")

def ver_perfil():
    print("\n--- Ver Perfil de Cliente ---")
    email = input("Ingrese el correo electrónico del cliente: ")
    cliente = clientes.get(email)
    if cliente:
        print(f"Nombre: {cliente['nombre']}")
        print(f"Historial de Reservas: {cliente['historial_reservas']}")
        print(f"Preferencias: {cliente['preferencias']}")
        print(f"Puntos de Fidelización: {cliente['puntos_fidelizacion']}")
    else:
        print("Cliente no encontrado.")

def actualizar_perfil():
    print("\n--- Actualizar Perfil de Cliente ---")
    email = input("Ingrese el correo electrónico del cliente: ")
    cliente = clientes.get(email)
    if cliente:
        nuevo_nombre = input(f"Ingrese el nuevo nombre para {cliente['nombre']} (o presione Enter para dejarlo igual): ")
        if nuevo_nombre:
            cliente['nombre'] = nuevo_nombre
        print("Perfil actualizado exitosamente.")
    else:
        print("Cliente no encontrado.")

def ver_historial_reservas():
    print("\n--- Ver Historial de Reservas ---")
    email = input("Ingrese el correo electrónico del cliente: ")
    cliente = clientes.get(email)
    if cliente:
        print(f"Historial de Reservas para {cliente['nombre']}: {cliente['historial_reservas']}")
    else:
        print("Cliente no encontrado.")

def agregar_reservas():
    print("\n--- Añadir Reserva  ---")
    email = input("Ingrese el correo electrónico del cliente: ")
    cliente = clientes.get(email)
    if cliente:
        preferencia = input("Ingrese el nombre del sitio turistico: ")
        cliente['historial_reservas'].append(preferencia)
        print("Reserva añadida exitosamente.")
    else:
        print("Cliente no encontrado.") 

def ver_preferencias():
    print("\n--- Ver Preferencias y Solicitudes Especiales ---")
    email = input("Ingrese el correo electrónico del cliente: ")
    cliente = clientes.get(email)
    if cliente:
        print(f"Historial de Preferencias y Solicitudes Especiales para {cliente['nombre']}: {cliente['preferencias']}")
    else:
        print("Cliente no encontrado.")              

def agregar_preferencias():
    print("\n--- Añadir Preferencias y Solicitudes Especiales ---")
    email = input("Ingrese el correo electrónico del cliente: ")
    cliente = clientes.get(email)
    if cliente:
        preferencia = input("Ingrese la preferencia o solicitud especial: ")
        cliente['preferencias'].append(preferencia)
        print("Preferencia añadida exitosamente.")
    else:
        print("Cliente no encontrado.")


def agreagar_fidelizacion():
    print("\n--- Agregar puntos de fidelizacion del Cliente ---")
    email = input("Ingrese el correo electrónico del cliente: ")
    cliente = clientes.get(email)
    if cliente:
        puntos = input(f"Ingrese los puntos de fidelizacion : {cliente['nombre']} (o presione Enter para dejarlo igual): ")
        if puntos:
            cliente['puntos_fidelizacion'] = puntos
        print("Se agrego los puntos de fidelizacion exitosamente.")
    else:
        print("Cliente no encontrado.")        

def ver_programa_fidelizacion():
    print("\n--- Ver Programa de Fidelización ---")
    email = input("Ingrese el correo electrónico del cliente: ")
    cliente = clientes.get(email)
    if cliente:
        print(f"Puntos de Fidelización para {cliente['nombre']}: {cliente['puntos_fidelizacion']}")
    else:
        print("Cliente no encontrado.")

# Loop principal para el menú
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-10): ")

    if opcion == "1":
        crear_perfil()
    elif opcion == "2":
        ver_perfil()
    elif opcion == "3":
        actualizar_perfil()
    elif opcion == "4":
        ver_historial_reservas()
    elif opcion == "5":
        agregar_reservas()
    elif opcion == "6":
        ver_preferencias()
    elif opcion == "7":
        agregar_preferencias()
    elif opcion == "8":
        agreagar_fidelizacion()
    elif opcion == "9":
        ver_programa_fidelizacion()
    elif opcion == "10":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
