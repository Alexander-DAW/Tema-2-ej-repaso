texto = input("Introduce una frase ").lower()
vocales = "aeiou"
contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1

print(f"Numero de vocales: {contador}")