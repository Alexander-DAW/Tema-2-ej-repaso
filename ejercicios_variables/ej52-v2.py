class ReservaExistenteError(Exception):
    """Excepcion lanzada cuando se intenta hacer uan reserva para un cliente ya existente"""
    def __init__(self, nombre_cliente):
        super().__init__(F"El cliente {nombre_cliente} tiene una reserva ya creada")

class Reserva:
    def __init__(self, nombre_cliente, num_coches, tipo_habitacion):
        self.__nombre_cliente = nombre_cliente
        self.num_coches = num_coches
        self.tipo_habitacion = tipo_habitacion

    @property
    def nombre_cliente(self):
        return self.__nombre_cliente
    
    @nombre_cliente.setter
    def nombre_cliente(self):
        self.__nombre_cliente = self.nombre_cliente
    
    def __str__(self):
        return f"Reserva a nombre de {self.nombre_cliente}\nNumero de coches: {self.num_coches}\nTipo de habitacion: {self.tipo_habitacion}"

class Hotel:
    reservas = {}

    def __init__(self):
        pass

    def agregar_reserva(self, reserva):
        reserva.append(reserva.__nombre)

        


             

