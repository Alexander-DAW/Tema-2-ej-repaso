# Diccionario del inventario
inventario = {
    "Laptop": {
        "precio": 899.99,
        "cantidad": 5,
        "reseñas": [5, 4, 5, 4]
    },
    "Ratón": {
        "precio": 19.99,
        "cantidad": 20,
        "reseñas": [4, 5, 3, 4, 4]
    },
    "Teclado": {
        "precio": 49.99,
        "cantidad": 10,
        "reseñas": [5, 5, 4]
    }
}

inventario["Alfombrilla"]={
    "precio": 9.99,
    "cantidad": 15,
    "reseñas": [5, 3, 5]
}

inventario["Alfombrilla"].update({
    "precio": 11.99,
    "cantidad": 13,
})

print(inventario)

del inventario["Alfombrilla"]

print(inventario)
print(inventario.get("Alfombrilla"))#No existe con lo cual nos devuelve None
print(list(inventario.keys()))
print(list(inventario.values()))
for i in inventario:
    print(f"{i}: {inventario[i]}")

    