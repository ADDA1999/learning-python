numeros = [8, 3, 15, 1, 9]
menor = numeros[0]
for numero in numeros:
    if numero < menor:
        menor = numero
print("El número menor es: ",  menor)
