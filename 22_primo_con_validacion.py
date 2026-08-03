def es_un_primo(numero):
    es_primo = True
    if numero < 2:
        es_primo = False
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
    return es_primo

numero_valido = False
while not numero_valido:
    try:
        numero = int(input("Escribe un número: "))
        numero_valido = True
        print("Escribiste:", numero)
    except:
        print("El número escrito no es valido")
if es_un_primo(numero):
    print("Es primo")
else:
    print("No es primo")
