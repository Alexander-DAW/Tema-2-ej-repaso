class ReservaExistenteError(Exception):
    """Excepcion lanzada cuando se intenta hacer uan reserva para un cliente ya existente"""
    def __init__(self, nombre_cliente):
        super().__init__(F"El cliente {nombre_cliente} tiene una reserva ya creada")
class ReservaInxistenteError(Exception):
    def __init__(self, nombre_cliente):
        super().__init__(F"El cliente {nombre_cliente} no tiene ninguna reserva creada")
        

class Reserva:
    def __init__(self, nombre_cliente, num_coches, tipo_habitacion, num_noches):
        self.__nombre_cliente = nombre_cliente
        self.num_coches = num_coches
        self.tipo_habitacion = tipo_habitacion
        self.num_noches = num_noches

    @property
    def nombre_cliente(self):
        return self.__nombre_cliente
    
    @nombre_cliente.setter
    def nombre_cliente(self, nombre_cliente):
        self.__nombre_cliente = nombre_cliente
    
    def __str__(self):
        return f"Reserva a nombre de {self.nombre_cliente} durante {self.num_noches} noches\nNumero de coches: {self.num_coches}\nTipo de habitacion: {self.tipo_habitacion}"
    

class Hotel:

    def __init__(self, reservas):
        self.__reservas = reservas

    @property
    def reservas(self):
        return self.__reservas
    
    @reservas.setter
    def reservas(self, reservas):
        self.__reservas = reservas

    def agregar_reserva(self, reserva):
        if reserva.nombre_cliente in self.reservas:
            raise ReservaExistenteError(reserva.nombre_cliente)
        else:
            datos = {"Número de coches" : reserva.num_coches, "Tipo de habitación" :reserva.tipo_habitacion, "Noches" : reserva.num_noches, "Costo total" : self.calcular_costo(reserva)}
            if self.reservas == {}:
                self.reservas = {
                    reserva.nombre_cliente : datos
                }
                print("Reserva realizada correctamente")
            else:
                self.reservas[reserva.nombre_cliente] = datos
                print("Reserva realizada correctamente")
        
        
    def cancelar_reserva(self, reserva):
        if reserva.nombre_cliente in self.reservas.keys():
            del self.reservas[reserva.nombre_cliente]
            print("Reserva cancelada correctamente")
        else:
            raise ReservaInxistenteError(self.nombre_clientes)


    def calcular_costo(self, reserva):
        match reserva.tipo_habitacion.lower():
            case "individual":
                habitacion_costo = 50
            case "doble":
                habitacion_costo = 80
            case "suite":
                habitacion_costo = 150
            case "familiar":
                habitacion_costo = 200
            case _:
                raise ValueError("Tipo de habitación no valida")
        coches_costo = reserva.num_coches * 10
        costo_total = coches_costo + habitacion_costo * reserva.num_noches

        return costo_total
    
    def mostrar_resumen_reservas(self):
        contador_reservas = 1
        print(f"RESUMEN DE RESERVAS\n{'-' * 19}")
        for nombre, datos in self.reservas.items():
            print(f"Reserve número {contador_reservas}")
            print(f"Nombre del cliente: {nombre.capitalize()}")
            for nombre_dato, valor_dato in datos.items():
                print(f"{nombre_dato}: {valor_dato}")
            print(f"{'-' * 30}")  
    

reserva_1=Reserva("Alex", 3, "Familiar", 2)
reserva_2=Reserva("Manolo", 2, "Suite", 2)

hotel = Hotel({})

hotel.agregar_reserva(reserva_1)
hotel.agregar_reserva(reserva_2)
hotel.mostrar_resumen_reservas
hotel.mostrar_resumen_reservas()


        

    


            
            

        

    

        
            

