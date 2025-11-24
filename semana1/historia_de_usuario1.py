#Registrar productos con su nombre, precio y cantidad en un programa simple.
#Calcular operaciones básicas como total de unidades y costo aproximado.
#Aplicar fundamentos de programación: entrada de datos, variables, operaciones matemáticas y salidas en consola.



#inicializo variables vacias si son textos o en cero si son numericas

nombre_producto = ""
cantidad = 0
precio= 0.0
costo_total= 0.0
#con este imput para pedirle al usuario que ingrese el nombre
nombre_producto= input("ingresa el nombre del producto ")
#usamos ciclo while que la cantidad sea un numero
while True:
    try:
        cantidad_str=input("Ingrese la cantidad de unidades en numeros ")
        cantidad = int(cantidad_str)
        break
# capturamos el error
    except ValueError:
        print("la cantidad debe ser un numero entero")
# este ciclo es para que el precio pueda ser un valor float
while True:
    try:
        precio_str=input("ingrese el precio del producto, en valor numerico ")
        precio=float(precio_str)
        break
    except ValueError:
        print("El precio debe ser un numero ")
# la operacion matematica que nos arrojara el resultado
costo_total=(cantidad*precio)

print("Producto ingresado correctamente")
print("--------------------------------")
print(f"Producto : {nombre_producto}")
print(f"Cantidad: {cantidad}")
print(f"Precio : {precio}")
print(f"Precio total del pedido: {costo_total}")
print("--------------------------------")
