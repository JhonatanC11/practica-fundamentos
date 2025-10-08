# ejercicio18.py - Convertidor temperatura
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def validar_input(entrada):
    while True:
        try:
            resp = float(input(entrada))
            return resp
        except ValueError:
            print("Error. Ingrese solo valores númericos.")

def repetir():
    """Realiza la pregunta para repetir una operacion"""
    while True:
        resp = input("¿Desea repetir esta operación? S/N: ").strip().lower()
        if resp in ['s', 'n']:
            return resp
        else:
            print("Error. Ingrese solo S para si o N para no.")
          
while True:
    print("=" * 10 + " CONVERTIDOR DE TEMPERATURA °C Y °F " + "=" * 10)
    print("1. Celsius (°C) a Fahrenheit (°F)\n2. Fahrenheit (°F) a Celsius (°C)\n3. Salir\n")
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 0 < opcion < 4:
                break
            else:
                print("Error. Escoja un número entre 1 y 3.")
        except ValueError:
            print("Error. Ingresa una opción válida")
    if opcion == 1:
        while True:
            print("\nConvertir de °C a °F:")
            celsius = validar_input("Ingresa el valor de Celsius a convertir: ")
            print(f"{celsius} °C equivalen a: {celsius_a_fahrenheit(celsius):.1f} °F")
            if repetir() == "n": break
    elif opcion == 2:
        while True:
            print("\nConvertir de °F a °C:")
            fahrenheit = validar_input("Ingresa el valor de Fahrenheit a convertir: ")
            print(f"{fahrenheit} °F equivalen a: {fahrenheit_a_celsius(fahrenheit):.1f} °C")
            if repetir() == "n": break
    
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    print("Volviendo al menú...\n")