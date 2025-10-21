lista1 = [2, 4, 6, 8, 10]
lista2 = [1, 3, 5, 7, 9]
lista_resultados=[]

for num1, num2 in zip(lista1, lista2):
    lista_resultados.append(num1*num2)

print(lista_resultados)

    


