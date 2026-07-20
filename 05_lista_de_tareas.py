cantidad = int(input("¿Cuantas tareas quieres agregar?: "))
tareas = []
for i in range(cantidad):
    tarea = input("Escribe una tarea: ")
    tareas.append(tarea)
contador = 1
for tarea in tareas:
    print(contador, ".", tarea)
    contador = contador + 1