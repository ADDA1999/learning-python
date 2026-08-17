class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):
        return self.precio * self.cantidad

    def mostrar_info(self):
        print("Producto:", self.nombre)
        print("Precio:", self.precio)
        print("Cantidad:", self.cantidad)
        print("Valor total:",self.valor_total())

class ProductoOferta(Producto):
    def __init__(self, nombre, precio, cantidad, descuento):
        super().__init__(nombre, precio, cantidad)
        self.descuento = descuento

    def valor_total(self):
        precio_con_descuento = self.precio * (1 - self.descuento)
        return precio_con_descuento * self.cantidad

oferta1 = ProductoOferta("Mouse", 20000, 5, 0.20)
oferta1.mostrar_info()
