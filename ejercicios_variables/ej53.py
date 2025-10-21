temperaturas_celsius=[0, 10, 20, 30, 40]
temperaturas_fahrenheit=list(map(lambda C: round(9/5*C+32), temperaturas_celsius))
print(temperaturas_fahrenheit)

