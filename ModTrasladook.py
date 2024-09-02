import unicodedata

# Eliminar tildes y convertir a minúsculas
def normalizar_texto(texto):
    texto = texto.lower() 
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8') 
    return texto

# Calcular la tarifa base según el destino
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

# Aplicar el descuento del 10%
def aplicar_descuento(tarifa, descuento=0.10):
    return tarifa * (1 - descuento)

# Función principal para el cálculo del traslado
def calcular_traslado():
    # Preguntas al usuario
    destino = input("¿A dónde va? (centro, norte, sur, area metropolitana, hotel a aeropuerto, aeropuerto hotel): ").strip()
    tipo_traslado = input("Elija el tipo de traslado (auto privado, van, bus): ").strip()
    solo_ida = input("¿Es solo ida? (sí/no): ").strip().lower() == 'si'
    tiene_descuento = input("¿Tiene descuento? (sí/no): ").strip().lower() == 'si'

    # Normalizar las entradas
    destino_normalizado = normalizar_texto(destino)
    tipo_traslado_normalizado = normalizar_texto(tipo_traslado)

    # Cálculo de la tarifa base según el destino
    tarifa_base = calcular_tarifa(destino_normalizado)

    # Verifica si la tarifa base es válida
    if tarifa_base == 0:
        print("Destino no válido. Por favor, revise la entrada.")
        return

    # Ajuste según el tipo de traslado
    if tipo_traslado_normalizado == 'auto privado':
        tarifa_ajustada = tarifa_base
    elif tipo_traslado_normalizado == 'van':
        tarifa_ajustada = tarifa_base * 0.5  # 50% de descuento
    elif tipo_traslado_normalizado == 'bus':
        tarifa_ajustada = 20000  # Tarifa fija para bus
    else:
        print("Tipo de traslado no válido. Por favor, revise la entrada.")
        return

    # Si es ida y vuelta, duplicar la tarifa
    if not solo_ida:
        tarifa_ajustada *= 2

    # Aplicar descuento si el usuario tiene uno
    if tiene_descuento:
        tarifa_final = aplicar_descuento(tarifa_ajustada)
    else:
        tarifa_final = tarifa_ajustada

    print(f"El costo total del traslado es: ${tarifa_final:.2f} COP")

# Ejecutar la función
calcular_traslado()
