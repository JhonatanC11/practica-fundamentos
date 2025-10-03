# ejercicio1.py - Par o Impar
# Pide un número al usuario y di si es par o impar
numero = int(input("Introduce un numero entero y positivo: "))
while not (numero>0):
    numero = int(input("Valor invalido. Introduce un numero entero y positivo: "))

if numero % 2 == 0:
    print("El numero ", numero, "es par")
else:
    print ("El numero ", numero, "es impar")