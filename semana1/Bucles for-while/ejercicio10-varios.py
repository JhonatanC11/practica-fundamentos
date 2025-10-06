import time
import sys
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

for i in range (tiempo):
    interes_anual = capital_total * tasa_anual / 100
    capital_total += interes_anual
    intereses += interes_anual
    print(f"Capital total tras {i+1} años: {capital_total:.2f}")
print(f"Interes generados en total: {intereses:.2f}")

#Escribir un programa que pida al usuario un número entero y muestre por pantalla
#un triángulo rectángulo como el de más abajo, de altura el número introducido.
numero = int(input("Ingrese un número: "))
for i in range(numero):
    for j in range (i+1):
        print("*", end="")
    print("")

#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.    
for i in range (1, 11):
    print(f"Tabla del {i}: ")
    for j in range (1, 11):
        print(f"{i} X {j} = {i * j}")
    print("")

#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario
#por la contraseña hasta que introduzca la contraseña correcta.

contraseña = "hola123"

while True:
    intentos = 5
    while intentos > 0:
        print(f"Tienes solo {intentos} intentos.")
        contra_input = str(input("Ingrese la contraseña: "))
        if contra_input == contraseña:
            break
        else:
            print("Contraseña incorrecta. Intente nuevamente. ")
            intentos -= 1
    if intentos == 0:
        print("Demasiados intentos fallidos. Saliendo del sistema...")
        time.sleep(2)
        sys.exit()

    print("Bienvenido al sistema. ")
    break

#Escribir un programa que pida al usuario un número entero y 
#muestre por pantalla si es un número primo o no.

numero = int(input("Ingrese un numero: "))
if numero <= 1:
    print(f"{numero} no es primo")
else:
    for i in range (2, numero):
        if numero % i == 0:
            break
    if (i+1) == numero:
        print(f"{numero} es primo")      
    else:
        print(f"{numero} no es primo")  

#Escribir un programa que pida al usuario una palabra 
#y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = str(input("Ingrese una palabra: "))
for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])


#Escribir un programa en el que se pregunte al usuario por una frase
#y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Ingresa una frase: ")
letra = input("Ingresa una letra: ")
n_letra = 0
for i in frase:
    if letra == i:
        n_letra += 1

print(f"La letra {letra} se repite {n_letra} veces.") 


#Escribir un programa que muestre el eco de todo lo que el usuario
#introduzca hasta que el usuario escriba “salir” que terminará.
salir = "salir"
while True:
    palabra = input("Ingresa lo que quieras: ")
    print(palabra)
    if palabra == salir:
        break

        
        

    


    



