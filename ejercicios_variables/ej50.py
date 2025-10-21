vinos = [
    "Cream Sherry",
    "Oloroso Sherry",
    "Fino",
    "Amontillado Sherry",
    "Cabernet Sauvignon",
    "Pedro Ximénez",
    "Dry Sherry"
]

def vinos_sherry(vinos):
    diccionario_sherry = {}
    for i in vinos:
        if "Sherry" in i:
            diccionario_sherry[i] = True
        else:
            diccionario_sherry[i] = False
    return diccionario_sherry

vinosherry=vinos_sherry(vinos)

lista_sherry = list(filter(lambda vino: vinosherry[vino], vinosherry))
            
    
print(lista_sherry)