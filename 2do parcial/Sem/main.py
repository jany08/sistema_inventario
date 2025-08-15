from sem.producto import Producto
from sem.inventario import Inventario

def menu():
    inventario = Inventario()

    while True:
        print("\n📋 --- Menú de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                id_p = int(input("ID del producto: "))
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_p, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("⚠️ Error: Datos inválidos.")

        elif opcion == "2":
            try:
                id_p = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id_p)
            except ValueError:
                print("⚠️ Error: ID inválido.")

        elif opcion == "3":
            try:
                id_p = int(input("ID del producto a actualizar: "))
                cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
                precio = input("Nuevo precio (dejar vacío si no cambia): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_p, cantidad, precio)
            except ValueError:
                print("⚠️ Error: Datos inválidos.")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for r in resultados:
                    print(r)
            else:
                print("❌ No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción no válida.")

if __name__ == "__main__":
    menu()
