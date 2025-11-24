# Historia de usuario - Semana 2
# Control de flujo y manejo de listas en el inventario

# En este sistema el usuario puede:
# - Registrar nuevos productos
# - Consultar el inventario
# - Actualizar productos
# - Eliminar productos
# - Buscar productos por código

# el codigo gira en un diccionario y listas dentro del diccionario, entonces inicializamos uno vacio
productos={}
#en cada def creamos una funcion, es un bloque de codigo que podria usar en otras partes
# En este mostramos un menu con todas sus opciones
def mostrar_menu():
    print("======menu principal=======")
    print("1. ver productos ")
    print("2. registrar productos")
    print("3. actualizar producto")
    print("4. eliminar un producto")
    print("5. buscar un producto")
    print("0. salir ")

# funcion para ver productos
def mostrar_productos():
    #esta condicion es contraria, significa que si el diccionario esta vacio o iguala 0 entonces muestre
    if not productos:
        print("============================")
        print("no hay productos para mostra")
        print("============================")
        #si si hay elementos muestrelos
    else:
        print("=====Inventario=====")
        #recorremos los datos para mostrar el inventario
        for codigo,(nombre,precio,cantidad) in productos.items():
            print(F" codigo  -  nombre  -  precio  -  cantidad")
            print(F"{codigo} - {nombre} - {precio} - {cantidad}")

#registrar productos
def registrar_productos():
    #usamos el try que es un manejo de errore, para poder capturarlos si es el caso
    try:
        codigo=int(input("Ingrese el codigo del producto: "))
        if codigo in productos:
            print("======================")
            print("El producto ya existe ")
            print("======================")
            return      
          #salimos si el producto existe
          # si no existe ingresamos los valores del nuevo producto
        nombre=input("Ingrese el nombre del producto: ")
        precio=input("Ingrese el precio del producto: ")
        cantidad=input("Ingrese la cantidad del producto: ")
        #agregamos
        productos[codigo]=(nombre, precio, cantidad)
        print(f"{nombre} registrado con exito")
        #capturamos el error
    except ValueError:
        print("ingrese un numero valido, intente nuevamente")
# funcion eliminar producto
def eliminar_producto():
    #try para capturar errores
    try: 
        #le pedimos codigo del producto al usuario
        codigo = int(input("ingrese el codigo del producto a eliminar"))
        if codigo in productos:
            #usamos el .pop para eliminar un producto en especifico
            eliminado = productos.pop(codigo)
            print("el producto fue eliminado del inventario")
        else:
            print("el producto no existe")
    # capturamos el error
    except ValueError:
        print("ingrese un numero codigo valido")
#definimos la funcion actualizar producto
def actualizar_producto():
    try:
        codigo = int(input("ingrese el codigo del producto a actualizar"))
        if codigo in productos:
            nombre=input("Ingrese el nombre del producto: ")
            precio=input("Ingrese el precio del producto: ")
            cantidad=input("Ingrese la cantidad del producto: ")
            #recorremos y renombramos donde encuentra al la clave codigo
            productos[codigo]=(nombre, precio, cantidad)
            print(f"{nombre} actualizado con exito")

        else:
            print("")
    # capturamos el error
    except ValueError:
        print("ingrese un numero valido")
#Definimos la funcion buscar productos
def buscar_producto():
    try:
        # pedimos datos al usuario, busacmos y mostramos
        codigo=int(input("Ingrese el codigo del producto que deseas buscar"))
        if codigo in productos:
            nombre, precio, cantidad = productos[codigo]
            print("producto encontrado")
            print(f"el produco con codigo {codigo}, nombre: {nombre}, precio: {precio}, cantidad: {cantidad}")

        else:
            print("el producto no existe")

    except ValueError:
        print("ingrese un numero valido")
    


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            registrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente nuevamente")

# Ejecutar el programa
if __name__ == "__main__":
    main()
