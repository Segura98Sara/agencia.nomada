class hotel:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.habitacion = []

    def añadir_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
        print(f"habitacion {habitacion.numero} añadida al hotel {self.nombre}.")

    def eliminar_habitacion(self, habitacion):
        self.habitaciones.remove(habitacion)
        print(f"habitacion {habitacion.numero} eliminada del hotel {self.nombre}.")

    def buscar_habitacion(self, tipo=None, precio_max=None):
        resultaddos = []
        for habitacion in self.habitaciones:
            if (tipo is None or habitacion.tipo ==tipo) and (precio_max is None or habitacion.precio <= precio_max):
                resultaddos.append(habitacion)
        return resultaddos
    
    def mostrar_info(self):
        return f"hotel {self.nombre}, ubicado en {self.ubicacion}"

class habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible
        estado = "disponible" if disponible else "no disponible"
        print(f"habitacion {self.numero} ahora está {estado}")

    def mostrar_info(self):
        return f"Habitacion {self.numero} Tipo: {self.tipo}, Precio: {self.precio} por noche"
    
class reserva:
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
        print(f"""reserva {self.id_reserva} modificada para el periodo {self.fecha_entrada} a {self.fecha_salida}""")

    def cancelar_reserva(self):
        self.estado = "cancelada"
        print(f"reserva {self.id_reserva} cancelada.")

class clientes:
    def __init__(self, id_cliente, nombre, email):
        self.ed_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.reservas = []

    def realizar_reserva(self, rserva):
        self.reservas.append(reserva)
        reserva.estado = "confirmada"
        print(f"""reserva {reserva.id_reserva} realizada por {self.nombre} para la habitacion {reserva.habitacion.numero}.""")

    def cancelar_reserva(self, reserva):
        if reserva in self.reservas:
            self.reservas.remove(reserva)

class SistemaReservas:
    def __init__(self):
        self.hoteles = []
        self.clientes = []

    def registrar_hotel(self, hotel):
        self.hoteles.append(hotel)
        print(f"totel {hotel.nombre} registrado en el sistema.")

    def eliinar_hotel(self, hotel):
        self.hoteles.remove(hotel)
        print(f"totel {hotel.nombre} eliminado del sistema.")

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"cliente {cliente.nombre} registrado en el sistema.")

    def eliminar_cliente(self, cliente):
        self.clientes.remove(cliente)
        print(f"cliente {cliente.nombre} eliminado del sistema.")

    def buscar_hoteles(self, ubicacion=None, nombre=None):
        resultados = []
        for hotel  in self.hoteles:
            if (ubicacion is None or hotel.ubicacion == ubicacion) and (nombre is None or hotel.nombre == nombre):
                resultados.append(hotel)
        return resultados
    
    def lista_reservas(self):
        for cliente in self.clientes:
         for reserva in cliente.reservas:
            print(f"Reserva {reserva.id_reserva} para el cliente: {cliente.nombre}, para las fechas desde: {reserva.fecha_entrada} hasta: {reserva.fecha_salida}. Estado: {reserva.estado}.")

    
