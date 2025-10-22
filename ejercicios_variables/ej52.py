reservas= {}

def agregar_reservas(nombre_cliente, num_coches, tipo_habitacion):
    try:
        reservas[nombre_cliente]=[num_coches, tipo_habitacion]
    except ValueError:
        print ("Entrada no valida. Introduzca un numero en el numero de coches")

    return reservas

def cancelar_reservas(nombre_cliente):
    if nombre_cliente in reservas.keys():
          del reservas[nombre_cliente]
        
def calcular_costo():
    for num_coches, tipo_habitacion in reservas.values():
        match tipo_habitacion.lower():
            case "individual":
                habitacion_costo = 50
            case "doble":
                habitacion_costo = 80
            case "suite":
                habitacion_costo = 150
            case "familiar":
                habitacion_costo = 200
            case _:
                raise ValueError("Tipo de habitacion no valida")
        coches_costo = num_coches * 10
        costo_total = coches_costo + habitacion_costo
    return costo_total

def mostrar_resumen_reservas():
    for nombre_cliente in reservas.keys():
        for numero_coches, tipo_habitacion in reservas.values():
            print(f"Nombre cliente: {nombre_cliente}\nNumero de coches {numero_coches}\nTipo de tipo_habitacion: {tipo_habitacion}\n {( '-' * 40)}")


agregar_reservas("Alex", 8, "Comfort")
agregar_reservas("Pedro", 10, "Comfort")
agregar_reservas("Ruben", 3, "Premium")
print(reservas)
cancelar_reservas("Ruben")
print(reservas)
mostrar_resumen_reservas()