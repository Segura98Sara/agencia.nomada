# Funciones de alojamiento
import datetime


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
        menu_principal() # type: ignore
    elif confirmacion.lower() == 'no':
        print("\nReserva cancelada. Regresando al menú de alojamiento...\n")
        reservar_alojamiento()  # Regresa a la función de reserva
    else:
        print("\nOpción no válida. Por favor, intenta de nuevo.\n")
        confirmar_reserva_alojamiento(destino, entrada, salida, costo_total)
