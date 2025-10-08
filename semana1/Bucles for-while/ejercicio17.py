# ejercicio17.py - Validador de edad
def es_mayor_edad(edad):
    return edad >= 18
    
def puede_conducir(edad):
    return edad >= 16

def repetir(pregunta):
    """Realiza la pregunta para repetir una operacion"""
    while True:
        resp = input(pregunta).strip().lower()
        if resp in ['s', 'n']:
            return resp
        else:
            print("Error. Ingrese solo S para si o N para no.") 

while True:   
    print("=" * 10 + " VALIDADOR DE EDAD " + "=" * 10)
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if 0 <= edad <= 110:
                break
            else:
                print("Error. Por favor ingrese una edad válida.")

        except ValueError:
            print("Error. Por favor ingrese solo números enteros.")
    if es_mayor_edad(edad):
        print(f"Tienes {edad} años. Por ende, eres mayor de edad")
    else:
        print(f"Tienes {edad} años. Por ende, eres menor de edad")

    if puede_conducir(edad):
        print("Puedes conducir")
    else:
        print("No puedes conducir")
    
    resp = repetir("¿Desea validar otra edad? S/N: ")
    if resp == "n":
        break
print("Saliendo del programa...")
# Fin del programa