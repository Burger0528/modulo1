""" aqui tenemos los servicios del inventario """

def agregar_producto(inventory, name, price, quantity):
    inventory.append({"nombre": name, "precio": price, "cantidad": quantity})

def mostrar_inventario(inventory):
    if not inventory:
        print("El inventario está vacío.")
        return
    sorted_inventory = sorted(inventory, key=lambda p: p["nombre"].lower())
    print("\n--- Inventario ---")
    for product in sorted_inventory:
        print(f"Producto: {product['nombre']} | Precio: {product['precio']} | Cantidad: {product['cantidad']}")
    print("-------------------\n")

def buscar_producto(inventory, name):
    for product in inventory:
        if product["nombre"].lower() == name.lower():
            return product
    return None

def actualizar_producto(inventory, name, new_price=None, new_quantity=None):
    product = buscar_producto(inventory, name)
    if product:
        if new_price is not None:
            product["precio"] = new_price
        if new_quantity is not None:
            product["cantidad"] = new_quantity
        print("Producto actualizado correctamente.")
    else:
        print("Producto no encontrado.")

def eliminar_producto(inventory, name):
    product = buscar_producto(inventory, name)
    if product:
        inventory.remove(product)
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

def calcular_estadisticas(inventory):
    if not inventory:
        print("El inventario está vacío, no hay estadísticas que mostrar.")
        return

    subtotal = lambda p: p["precio"] * p["cantidad"]
    unidades_totales = sum(p["cantidad"] for p in inventory)
    valor_total = sum(subtotal(p) for p in inventory)
    producto_mas_caro = max(inventory, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventory, key=lambda p: p["cantidad"])

    print("\n--- Estadísticas del Inventario ---")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: {valor_total}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} (Precio: {producto_mas_caro['precio']})")
    print(f"Producto con mayor stock: {producto_mayor_stock['nombre']} (Cantidad: {producto_mayor_stock['cantidad']})")
    print("------------------------------------\n")

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }
