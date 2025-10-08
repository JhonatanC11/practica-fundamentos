# ejercicio16.py - Calculadora
def sumar(num1, num2):
    """Sumar dos números"""
    return num1 + num2

def restar(num1, num2):
    """Restar dos números"""
    return num1 - num2

def multiplicar(num1, num2):
    """Multiplicar dos números"""
    return num1 * num2

def dividir(num1, num2):
    """Dividir dos números. Con condición para la división entre 0"""
    if num2 == 0:
        divi = "No es posible la division entre cero."
    else:
        divi = num1 / num2
    return divi

def repetir(pregunta):
    """Realiza la pregunta para repetir una operacion"""
    while True:
        resp = input(pregunta).strip().lower()
        if resp in ['s', 'n']:
            return resp
        else:
            print("Error. Ingrese solo S para si o N para no.") 

def mostrar_menu():
    """Muestra el menú"""
    print("=" * 10 + " CALCULADORA " + "="*10)
    print("Operaciones disponibles:")
    print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir\n")
    
#Bucle principal
while True:
    mostrar_menu()
    while True:
        try:
            operacion = int(input("Elige una operación (1-5): "))
            if 0 < operacion <=5:
                break
            else:
                print("Fuera del rango. Por favor ingresa solo números de 1 a 5")
        except ValueError:
            print("Error. Por favor ingrese solo números enteros.")
            
    if operacion == 5:
        print("Saliendo del programa...")
        break

    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if operacion == 1:
                print(f"Resultado:\n{num1} + {num2} = {sumar(num1, num2)}")
                resp = repetir("¿Desea realizar otra suma? S/N: ")
                 

            elif operacion == 2:
                print(f"{num1} - {num2} = {restar(num1, num2)}")
                resp = repetir("¿Desea realizar otra resta? S/N: ")

            elif operacion == 3:
                print(f"{num1} x {num2} = {multiplicar(num1, num2)}")
                resp = repetir("¿Desea realizar otra multiplicación? S/N: ")

            elif operacion == 4:
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
                resp = repetir("¿Desea realizar otra division? S/N: ")
            
            if resp == 'n': 
                print("Volviendo al menú...")
                break
        except ValueError:
            print("Error. Ingrese solo números enteros")