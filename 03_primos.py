numero = int(input("Escribe un número: "))
es_primo = True
if numero < 2:
    es_primo = False
for i in range(2, numero):
    if numero % i == 0:
        es_primo = False 
if es_primo:
    print("Es primo")
else:
    print("No es primo")