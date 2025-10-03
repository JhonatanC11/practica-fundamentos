# ejercicio10.py - Adivina el número
# Número secreto del 1 al 20
# Usuario tiene 5 intentos
# Da pistas: "muy alto" o "muy bajo"
import random
numero_secreto = random.randint(1, 20)
intentos = 5

print("¡Adivina el número secreto entre 1 y 20!")
while intentos > 0:
    print (f"Intentos restantes: {intentos}")
    while True:
        try:
            numero_user = int(input("Ingresa un número (1-20): "))
            if 1 <= numero_user <= 20:
                break
            else:
                print("Fuera del rango. Ingrese un número entre 1 y 20")
        except ValueError:
            print("Error. Por favor ingrese solo números enteros")

    if numero_user == numero_secreto:
        print(f"¡Felicidades! Lo adivinaste en {6-intentos} intentos.")
        break
    elif numero_user > numero_secreto:
        print("Tu numero es muy alto. ¡Intenta con uno menor!")
    else: 
        print("Tu número es muy bajo. ¡Intenta con uno mayor!")
    intentos -= 1
if intentos == 0:
    print("Te has quedado sin intentos :(")
print(f"El número secreto era: {numero_secreto}")

