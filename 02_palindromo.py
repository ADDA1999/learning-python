palabra=input("Escribe una palabra ")
if palabra.lower() == palabra.lower()[::-1]:
    print ("Es un palíndromo!")
else:
    print ("No es un palíndromo")