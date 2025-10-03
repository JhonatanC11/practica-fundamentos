# ejercicio2.py - Mayor de edad
# Pide edad y di si es mayor de edad (18+)

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        if 0 < edad < 150:
            break

        else:
            print("Valor invalido. Ingrese correctamente su edad: ")
    
    except ValueError:
        print("Valor invalido. Ingrese correctamente su edad: ")

if edad >= 18:
    print(f"Tienes {edad} años, eres mayor de edad.")
else:
    print(f"Tienes {edad} años, eres menor de edad")


