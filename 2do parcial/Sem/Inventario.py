import csv
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()  # Cargar productos al iniciar

    def añadir_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            print("❌ ID ya existe.")
            return
        self.productos.append(producto)
        self.guardar_en_archivo()  # Guardar cambios
        print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.id == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("✅ Producto eliminado.")
                return
        print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.id == id_producto:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                self.guardar_en_archivo()
                print("✅ Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        return resultados

    def mostrar_productos(self):
        if not self.productos:
            print("📦 Inventario vacío")
            return
        for p in self.productos:
            print(f"ID: {p.id} | Nombre: {p.nombre} | Cantidad: {p.cantidad} | Precio: ${p.precio:.2f}")

    # ----------------------------
    # Funciones de archivo CSV
    # ----------------------------
    def guardar_en_archivo(self):
        with open("inventario.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nombre", "Cantidad", "Precio"])
            for p in self.productos:
                writer.writerow([p.id, p.nombre, p.cantidad, p.precio])

    def cargar_desde_archivo(self):
        try:
            with open("inventario.csv", "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    producto = Producto(int(row["ID"]), row["Nombre"], int(row["Cantidad"]), float(row["Precio"]))
                    self.productos.append(producto)
        except FileNotFoundError:
            pass  # Si no existe el archivo, no pasa nada
