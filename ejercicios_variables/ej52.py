reservas= {}

def agregar_reservas(nombre_cliente, num_coches, tipo_habitacion):
    reservas[nombre_cliente]=[num_coches, tipo_habitacion]
    return reservas

def cancelar_reservas(nombre_cliente):
    if nombre_cliente in reservas.keys():
          del reservas[nombre_cliente]
        
def calcular_costo():
     for num_coches, tipo_habitacion in reservas.values():
          costo=num_coches
          

agregar_reservas("Alex", 8, "Comfort")
agregar_reservas("Pedro", 10, "Comfort")
agregar_reservas("Ruben", 3, "Premium")
print(reservas)
cancelar_reservas("Ruben")
print(reservas)