# ejercicio3.py - Calculadora de descuento
# Precio de producto, si es mayor a $100 aplica 10% descuento
# Muestra precio final
while True:
    try:
        precio_prod = float(input("Ingrese el precio del producto: "))
        if precio_prod > 0:
            break
        else:
            print("Valor no válido. Ingrese números positivos.")
    except:
        print("Valor no valido. Ingrese valores numericos")

if precio_prod > 100:
    precio_prod = precio_prod - precio_prod * 0.10
    print("Tu producto sobrepasa el valor de 100$, obtuviste un decuento del 10% ")
    print(f"Tu producto quedó en: {precio_prod}")
else:
    print("Tu producto no alcanzó para el descuento :c")