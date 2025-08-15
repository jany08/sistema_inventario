class Producto:
    """
    Clase que representa un producto en el inventario.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def set_id(self, nuevo_id):
        self.id_producto = nuevo_id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"
