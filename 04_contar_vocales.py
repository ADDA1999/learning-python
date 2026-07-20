palabra = input("Escribe una palabra para contar sus vocales: ")
contador = 0
vocales = "aeiou"
for letra in palabra:
    if letra in vocales:
        contador = contador + 1
print("tiene", contador, "vocales")

