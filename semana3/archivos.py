import os

# Productos precargados por defecto
default_products = [
    {"nombre": "Manzanas", "precio": 1.5, "cantidad": 50},
    {"nombre": "Leche", "precio": 2.0, "cantidad": 20},
    {"nombre": "Huevos", "precio": 3.2, "cantidad": 30}
]

def guardar_txt(inventory):
    if not inventory:
        print("El inventario está vacío. No se puede guardar.")
        return

    folder = os.path.join(os.path.dirname(__file__), "inventario.txt")
    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, "inventario.")

    with open(filepath, "w", encoding="utf-8-sig", newline="\r\n") as file:
        file.write("nombre,precio,cantidad\n")
        for product in inventory:
            file.write(f"{product['nombre']},{product['precio']},{product['cantidad']}\n")

    print(f"Inventario guardado en: {filepath}")


def cargar_txt():
    folder = os.path.join(os.path.dirname(__file__), "inventario")
    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, "inventario.txt")

    # Si no existe, crear archivo con productos por defecto
    if not os.path.exists(filepath):
        guardar_txt(default_products)
        return default_products.copy()

    inventory = []
    with open(filepath, "r", encoding="utf-8-sig") as file:
        lines = file.readlines()

    if not lines or lines[0].strip() != "nombre,precio,cantidad":
        print("Encabezado inválido, cargando productos por defecto.")
        guardar_txt(default_products)
        return default_products.copy()

    for line in lines[1:]:
        parts = line.strip().split(",")
        if len(parts) != 3:
            continue
        try:
            inventory.append({
                "nombre": parts[0],
                "precio": float(parts[1]),
                "cantidad": int(parts[2])
            })
        except:
            continue

    # Ordenar por nombre
    inventory = sorted(inventory, key=lambda p: p["nombre"].lower())
    return inventory
