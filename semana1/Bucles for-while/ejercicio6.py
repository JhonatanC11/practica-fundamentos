# ejercicio6.py - Tabla de multiplicar
# Pide un número y muestra su tabla del 1 al 10
while True:
    try:
        numero = int(input("Ingrese un numero para saber su tabla de multiplicar (1-10): "))
        if numero > 0:
            break
        else: 
            print("Número no valido. Ingrese solo números positivos. ")
    except ValueError:
        print("Valor no válido. Ingrese valores enteros")

contador = 1
while contador <= 10:
    print(f"{numero} X {contador} = {numero*contador}")
    contador += 1