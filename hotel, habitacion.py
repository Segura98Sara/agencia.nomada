class Hotel:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.habitaciones = []

    def añadir_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
        print(f"Habitación {habitacion.numero} añadida al hotel {self.nombre}.")

    def eliminar_habitacion(self, habitacion):
        self.habitaciones.remove(habitacion)
        print(f"Habitación {habitacion.numero} eliminada del hotel {self.nombre}.")

    def buscar_habitacion(self, tipo=None, precio_max=None):
        resultados = []
        for habitacion in self.habitaciones:
            if (tipo is None or habitacion.tipo == tipo) and (precio_max is None or habitacion.precio <= precio_max):
                resultados.append(habitacion)
        return resultados
    
    def mostrar_info(self):
        return f"Hotel {self.nombre}, ubicado en {self.ubicacion}"

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible
        estado = "disponible" if disponible else "no disponible"
        print(f"Habitación {self.numero} ahora está {estado}")

    def mostrar_info(self):
        return f"Habitación {self.numero} Tipo: {self.tipo}, Precio: ${self.precio} por noche, Estado: {'Disponible' if self.disponible else 'No disponible'}"
    
class Reserva:
    def __init__(self, id_reserva, habitacion, cliente, fecha_entrada, fecha_salida):
       self.id_reserva = id_reserva
       self.habitacion = habitacion
       self.cliente = cliente
       self.fecha_entrada = fecha_entrada
       self.fecha_salida = fecha_salida
       self.estado = "pendiente"

    def modificar_reserva(self, nueva_fecha_entrada, nueva_fecha_salida):
        self.fecha_entrada = nueva_fecha_entrada
        self.fecha_salida = nueva_fecha_salida
        print(f"Reserva {self.id_reserva} modificada para el periodo {self.fecha_entrada} a {self.fecha_salida}")

    def cancelar_reserva(self):
        self.estado = "cancelada"
        self.habitacion.actualizar_disponibilidad(True)
        print(f"Reserva {self.id_reserva} cancelada.")

    def mostrar_info(self):
        return f"Reserva {self.id_reserva}: Hotel {self.habitacion.hotel.nombre}, Habitación {self.habitacion.numero}, Fechas: {self.fecha_entrada} a {self.fecha_salida}, Estado: {self.estado}"

class Cliente:
    def __init__(self, id_cliente, nombre, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.reservas = []

    def realizar_reserva(self, reserva):
        self.reservas.append(reserva)
        reserva.estado = "confirmada"
        reserva.habitacion.actualizar_disponibilidad(False)
        print(f"Reserva {reserva.id_reserva} realizada por {self.nombre} para la habitación {reserva.habitacion.numero}.")

    def cancelar_reserva(self, reserva):
        if reserva in self.reservas:
            self.reservas.remove(reserva)
            reserva.cancelar_reserva()

    def mostrar_info(self):
        info = f"Cliente: {self.nombre}, Email: {self.email}\nReservas:"
        if not self.reservas:
            info += " No hay reservas activas."
        else:
            for reserva in self.reservas:
                info += f"\n  {reserva.mostrar_info()}"
        return info

class SistemaReservas:
    def __init__(self):
        self.hoteles = []
        self.clientes = []

    def registrar_hotel(self, hotel):
        self.hoteles.append(hotel)
        print(f"Hotel {hotel.nombre} registrado en el sistema.")

    def eliminar_hotel(self, hotel):
        self.hoteles.remove(hotel)
        print(f"Hotel {hotel.nombre} eliminado del sistema.")

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nombre} registrado en el sistema.")

    def eliminar_cliente(self, cliente):
        self.clientes.remove(cliente)
        print(f"Cliente {cliente.nombre} eliminado del sistema.")

    def buscar_hoteles(self, ubicacion=None, nombre=None):
        resultados = []
        for hotel in self.hoteles:
            if (ubicacion is None or hotel.ubicacion == ubicacion) and (nombre is None or hotel.nombre == nombre):
                resultados.append(hotel)
        return resultados
    
    def listar_reservas(self):
        for cliente in self.clientes:
            for reserva in cliente.reservas:
                print(reserva.mostrar_info())

    def obtener_info_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente.mostrar_info()
        return "Cliente no encontrado."

# Ejemplo de uso
if __name__ == "__main__":
    sistema = SistemaReservas()

    # Crear y registrar hoteles
    hotel1 = Hotel("Hotel Playa", "Costa del Sol")
    hotel2 = Hotel("Hotel Montaña", "Sierra Nevada")
    sistema.registrar_hotel(hotel1)
    sistema.registrar_hotel(hotel2)

    # Añadir habitaciones a los hoteles
    hab1 = Habitacion(101, "Individual", 50)
    hab2 = Habitacion(102, "Doble", 80)
    hab3 = Habitacion(201, "Suite", 150)
    hab1.hotel = hotel1  # Añadimos referencia al hotel
    hab2.hotel = hotel1
    hab3.hotel = hotel2
    hotel1.añadir_habitacion(hab1)
    hotel1.añadir_habitacion(hab2)
    hotel2.añadir_habitacion(hab3)

    # Registrar clientes
    cliente1 = Cliente(1, "Juan Pérez", "juan@email.com")
    cliente2 = Cliente(2, "María López", "maria@email.com")
    sistema.registrar_cliente(cliente1)
    sistema.registrar_cliente(cliente2)

    # Realizar reservas
    reserva1 = Reserva(1, hab1, cliente1, "2023-07-01", "2023-07-05")
    reserva2 = Reserva(2, hab3, cliente2, "2023-08-15", "2023-08-20")
    cliente1.realizar_reserva(reserva1)
    cliente2.realizar_reserva(reserva2)

    # Obtener información de un cliente específico
    print("\nInformación del cliente Juan Pérez:")
    print(sistema.obtener_info_cliente(1))

    # Obtener información de otro cliente
    print("\nInformación del cliente María López:")
    print(sistema.obtener_info_cliente(2))

    # Cancelar una reserva
    print("\nCancelando una reserva de Juan Pérez:")
    cliente1.cancelar_reserva(reserva1)

    # Mostrar información actualizada del cliente
    print("\nInformación actualizada de Juan Pérez:")
    print(sistema.obtener_info_cliente(1))

    # Intentar obtener información de un cliente que no existe
    print("\nIntentando obtener información de un cliente inexistente:")
    print(sistema.obtener_info_cliente(3))
