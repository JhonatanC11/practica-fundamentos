# Escribir un programa que pregunte al usuario su edad 
# y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Ingresa tu edad: "))
for i in range (edad):
    print(f"Ya cumpliste: {i+1} años")

# Escribir un programa que pida al usuario un número entero positivo y muestre 
# por pantalla todos los números impares desde 1 hasta ese número separados por comas.

while True:
    try:
        numero = int(input("Ingrese un número: "))
        if numero > 0:
            break
        else:
            print("Por favor ingrese un numero positivo. ")
    except ValueError:
        print("Error. Ingrese solo numero enteros.")
print(f"Numeros pares desde 1 hasta {numero}: ")
for i in range(numero+1):
    if not i % 2 == 0:
        print(i, end=",")

# Escribir un programa que pida al usuario un número entero
# positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
while True:
    try:
        numero = int(input("Ingrese un número: "))
        if numero > 0:
            break
        else: 
            print("Por favor ingrese un número positivo.")
    except ValueError:
        print("Error. Ingrese solo numeros enteros.")
for i in range (numero, -1, -1):
    print(i, end=",")

# Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión.
print("Calculadore de interés simple\n")
capital_ini = float(input("Ingrese el capital inicial: "))
tasa_anual = float(input("Ingrese la tasa de interés anual: "))
tiempo = int(input("Ingrese el tiempo de la inversión en años: "))

intereses = 0
capital_total = capital_ini
for i in range(tiempo):
    interes_anual = capital_total * tasa_anual / 100
    capital_total += interes_anual
    intereses += interes_anual
    print(f"Capital total tras {i+1} años: {capital_total:.2f}")
print(f"Intereses generados en total: {intereses:.2f}")

    





