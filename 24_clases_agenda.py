class Contacto:
    def __init__(self, nombre, numero, email):
        self.nombre = nombre
        self.numero = numero
        self.email = email

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Numero:", self.numero)
        print("Email:", self.email)

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
        return None

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                self.contactos.remove(contacto)
                return True
        return False

    def mostrar_todos(self):
        for contacto in self.contactos:
            contacto.mostrar_info()

    def guardar_en_archivo(self, nombre):
        archivo = open(nombre, "w")
        for contacto in self.contactos:
            archivo.write(contacto.nombre + "," + contacto.numero + "," + contacto.email + "\n")
        archivo.close()

    def cargar_desde_archivo(self, nombre):
        archivo = open(nombre, "r")
        lineas = archivo.readlines()
        archivo.close()
        lista_vacia = []
        for linea in lineas:
                partes = linea.strip().split(",")
                contacto_reconstruido = Contacto(partes[0], partes[1], partes[2])
                lista_vacia.append(contacto_reconstruido)
        return lista_vacia


mi_agenda = Agenda()
try:
    mi_agenda.contactos = mi_agenda.cargar_desde_archivo("contactos_clases.txt")
except:
    pass


while True:
    print ("=== AGENDA DE CONTACTOS ===")
    print ("1. Agregar contacto")
    print ("2. Buscar contacto")
    print ("3. Ver todos los contactos")
    print ("4. Eliminar contacto")
    print ("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Por favor digita el nombre de tu contacto: ")
        numero = input("Por favor digita el numero de tu contacto: ")
        email = input("Por favor digita el email de tu contacto: ")
        nuevo = Contacto(nombre, numero, email)
        mi_agenda.agregar_contacto(nuevo)
    elif opcion == "2":
        nombre = input("Por favor digita el nombre del contacto que quieres buscar: ")
        resultado = mi_agenda.buscar_contacto(nombre)
        resultado.mostrar_info()
    elif opcion == "3":
        mi_agenda.mostrar_todos()
    elif opcion == "4":
        nombre = input("Por favor digita el nombre de tu contacto: ")
        resultado = mi_agenda.eliminar_contacto(nombre)
        if resultado:
            print("El contacto se eliminó correctamente")
        else:
            print("Contacto no encontrado")
    elif opcion == "5":
        break
mi_agenda.guardar_en_archivo("contactos_clases.txt")
        
