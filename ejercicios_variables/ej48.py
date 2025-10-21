
estudiantes = {
    "Ana": [18, ["Matemáticas", "Historia", "Biología"]],
    "Luis": [20, ["Programación", "Física", "Inglés"]],
    "María": [19, ["Química", "Arte", "Literatura"]],
    "Carlos": [21, ["Economía", "Estadística", "Informática"]]
}

estudiantes["Alex"]=[20, ["Fisica", "Matematicas", "Ingles"]]
estudiantes["Ana"]=[18, ["Matemáticas", "Historia", "Programacion"]]
del estudiantes["Carlos"]


print(estudiantes)
print(estudiantes["Ana"])
print(estudiantes.get("Carlos")) #No existe con lo cual nos devuelve None
print(list(estudiantes.keys()))
print(list(estudiantes.values()))
for i in estudiantes:
    print(f"{i}: {estudiantes[i]}")

