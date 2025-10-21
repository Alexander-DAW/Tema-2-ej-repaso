nota = float(input("Introduce tu nota: "))

if 0 <= nota < 5:
    print("Suspenso")
elif 5 <= nota < 7:
    print("Aprobado")
elif 7 <= nota < 9:
    print("Notable")
elif 9 <= nota <= 10:
    print("Sobresaliente")
else:
    print("Respuesta invalida. Tiene que ser enrte 0 y 10")


