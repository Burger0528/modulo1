import sys
sys.dont_write_bytecode = True  # Evita __pycache__

from servicios import *
from archivos import guardar_txt, cargar_txt

# Cargar inventario desde archivo o inicializar productos por defecto
inventory = cargar_txt()

def menu():
    while True:
        print("""
--- Menú Principal ---
1. Agregar producto
2. Mostrar inventario
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Estadísticas
7. Guardar TXT
8. Salir
""")
        option = input("Selecciona una opción: ")

        if not option.isdigit():
            print("Ingresa un número válido.")
            continue

        option = int(option)

        # 1. Agregar
        if option == 1:
            name = input("Nombre del producto: ").strip()  # Quita espacios al inicio y fin
            if not name:  # Verifica si está vacío
                print("El nombre del producto no puede estar vacío.")
                continue

            try:
                price = float(input("Precio: "))
                quantity = int(input("Cantidad: "))
                if price < 0 or quantity < 0:
                    print("Los valores no pueden ser negativos.")
                    continue
            except:
                print("Debes ingresar valores numéricos válidos.")
                continue

            agregar_producto(inventory, name, price, quantity)

            

        # 2. Mostrar
        elif option == 2:
            mostrar_inventario(inventory)

        # 3. Buscar
        elif option == 3:
            name = input("Nombre del producto: ")
            product = buscar_producto(inventory, name)
            if product:
                print(f"Producto encontrado: {product}")
            else:
                print("Producto no encontrado.")

        # 4. Actualizar
        elif option == 4:
            name = input("Nombre del producto a actualizar: ").strip()  # Quita espacios
            if not name:  # Validación de nombre vacío
                print("El nombre del producto no puede estar vacío.")
                continue

            try:
                new_price = input("Nuevo precio (enter para no cambiar): ")
                new_quantity = input("Nueva cantidad (enter para no cambiar): ")

                new_price = float(new_price) if new_price else None
                new_quantity = int(new_quantity) if new_quantity else None

                if new_price is not None and new_price < 0:
                    print("Precio inválido.")
                    continue

                if new_quantity is not None and new_quantity < 0:
                    print("Cantidad inválida.")
                    continue
            except:
                print("Valores inválidos.")
                continue

            actualizar_producto(inventory, name, new_price, new_quantity)


        # 5. Eliminar
        elif option == 5:
            name = input("Nombre del producto a eliminar: ")
            eliminar_producto(inventory, name)

        # 6. Estadísticas
        elif option == 6:
            calcular_estadisticas(inventory)

        # 7. Guardar TXT
        elif option == 7:
            guardar_txt(inventory)

        # 8. Salir
        elif option == 8:
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")

menu()
