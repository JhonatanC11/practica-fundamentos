# ejercicio23.py - Inventario simple
import os
inventario = {
    "manzanas": 50,
    "naranjas": 30,
    "peras": 20
}

def agregar_producto(nombre_input, cantidad_input):
    """Agrega un nuevo producto o actualiza la cantidad si ya existe"""
    nombre = input(nombre_input).strip().lower()
    cantidad_input = int(input(cantidad_input))
    if nombre in inventario:
        inventario[nombre] += cantidad_input
        print(f"El producto '{nombre}' ya existe. Se actualizó su cantidad.")
    else:
        inventario[nombre] = cantidad_input
        print("Producto agregado correctamente.")

def buscar_producto(nombre_busq):
    if nombre_busq in inventario.keys():
        print(f" > {nombre_busq.upper()}: {inventario[nombre_busq]} unidades en stock.")
        return True
    else:
        print(f"El producto '{nombre_busq}' no existe.")
        return False

def editar_producto(nombre_edit):
    mostrar_inventario()
    nombre = input(nombre_edit).strip().lower()
    if buscar_producto(nombre):
        while True:
            opcion = input("¿Que deseas editar? (nombre/cantidad): ").strip().lower()
            if opcion == 'nombre':
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                inventario[nuevo_nombre] =  inventario[nombre]
                del inventario[nombre]
                print("Nombre actualizado correctamente.")
                break
            elif opcion == 'cantidad':
                nueva_cantidad = validar_enteros("Ingrese la nueva cantidad: ")
                inventario[nombre] = nueva_cantidad
                print("Producto actualizado correctamente.")
                break
            else:
                print("Error. Ingrese una opción válida")

def validar_enteros(valor_input):
    while True:
        try:
            valor = int(input(valor_input))
            if valor > 0:
                break
            else:
                print("Error. Solo ingrese valores enteros positivos")
        except ValueError:
            print("Error. Por favor ingresa solo valores númericos")
    return valor

def vender_producto(nombre_input):
    while True:
        mostrar_inventario()
        nombre_venta = input(nombre_input)
        if buscar_producto(nombre_venta):
            while True:
                nueva_cantidad = validar_enteros("Ingrese la cantidad vendida: ")
                if nueva_cantidad <= inventario[nombre_venta]:
                    break
                else:
                    print("Error. No puedes vender mas de la cantidad en stock")
            inventario[nombre_venta] -= nueva_cantidad
            print("Cambios actualizados correctamente.")
            break

def mostrar_inventario():
    # Muestra todos los productos y sus cantidades
    for producto, cantidad in inventario.items():
        print(f" > {producto}: {cantidad} unidades")

def validar_opc(opc_input):
    """Valida que la opción esté en el rango correcto"""
    while True:
        try:
            opcion = int(input(opc_input))
            if 0 < opcion < 6:
                break
            else:
                print("Fuera del rango. Ingrese un valor válido")
        except ValueError:
            print("Error. Ingrese solo valores enteros")
    return opcion

def limpiar_terminal():
    os.system("cls")

def repetir(pregunta):
    """Realiza la pregunta para repetir una operacion"""
    while True:
        resp = input(pregunta).strip().lower()
        if resp in ['s', 'n']:
            return resp
        else:
            print("Error. Ingrese solo S para si o N para no.")

while True:
    limpiar_terminal()
    print("\n" + "=" * 10 + " INVENTARIO " + "=" * 10)
    mostrar_inventario()
    print("\n1. Agregar producto\t2. Registrar venta\t3. Editar producto\t4. Buscar producto\t5. Salir")
    opcion = validar_opc("\nIngresa una opcion (1-5): ")

    if opcion == 1:
        while True:
            limpiar_terminal()
            print("=" * 10 + " AGREGAR PRODUCTO " + "=" * 10 + "\n")
            agregar_producto("Ingresa el nombre del producto: ","Ingresa la cantidad: ")
            resp = repetir("¿Desea agregar otro producto? S/N: ")
            if resp == 'n':
                print("Volviendo al menú...")
                break
    
    elif opcion == 2:
        while True:
            limpiar_terminal()
            print("=" * 10 + " REGISTRAR VENTA " + "=" * 10)
            vender_producto("Ingrese el nombre del producto vendido: ")
            resp = repetir("¿Desea registrar otra venta? S/N: ")
            if resp == 'n': break

    elif opcion == 3:
        while True:
            limpiar_terminal()
            print("=" * 10 + " EDITAR PRODUCTO " + "=" * 10)
            editar_producto("Ingresa el nombre del producto a editar: ")
            resp = repetir("¿Desea editar otro producto? S/N: ")
            if resp == 'n':
                break
    elif opcion == 4:
        while True:
            print("\n"+"=" * 10 + " BUSCAR PRODUCTO " + "=" * 10 + "\n")
            bus_producto = input("Ingresa el nombre del producto a buscar: ").lower()
            buscar_producto(bus_producto)
            resp = repetir("¿Desea buscar otro producto? S/N: ")
            if resp == 'n':
                break
    elif opcion == 5:
        print("Saliendo del programa...")
        break