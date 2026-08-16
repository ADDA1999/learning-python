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
c1 = Contacto("Allan", "8888-0000", "allan@gmail.com")
c2 = Contacto("Maria", "8444-6336", "maria@gmail.com")
mi_agenda.agregar_contacto(c1)
mi_agenda.agregar_contacto(c2)

mi_agenda.guardar_en_archivo("contactos_clases.txt")

nueva_agenda = Agenda()
nueva_agenda.contactos = nueva_agenda.cargar_desde_archivo("contactos_clases.txt")
nueva_agenda.mostrar_todos()
        
