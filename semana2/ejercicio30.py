# ejercicio30.py - Factorial
import os
SEP = "=" * 10

def factorial(n):
    """Retorna el factorial de un número junto con su secuencia."""
    # 5! = 5 * 4 * 3 * 2 * 1 = 120
    # Versión iterativa (con bucle)    
    if n == 0 or n == 1:
        return f"{n}! = 1"
    
    resultado = 1
    pasos = []
    for numero in range(n, 0, -1):
        pasos.append(str(numero))
        resultado *= numero
    
    return f"{n}! = {' * '.join(pasos)} = {resultado}"

def factorial_recursivo(n):
    """Retorna le factorial de un número, de manera recursiva llamandose así misma."""
    # Versión recursiva
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1) 
    
def validar_opc(prompt, valor_min, valor_max):
    """Valida que la opción ingresada sea correcta"""

    while True:
        try:
            opcion = int(input(prompt))
            if valor_min <= opcion <= valor_max:
                return opcion
            else:
                print("Error. Fuera del rango.")
        except ValueError:
            print("Error. Ingrese una opcion válida.")

def validar_entero(prompt):
    """Valida que los valores ingresados solo sean números positivos"""

    while True:
        try:
            numero = int(input(prompt))
            if numero >= 0:
                return numero
            else:
                print("Por favor ingresa solo números positivos.")
        
        except ValueError:
            print("Error. Ingresa solo números enteros positivos.")

def limpiar_terminal():
    """Limpia la terminal dependiendo el sistema operativo"""
    os.system("cls" if os.name == "nt" else "clear")

def repeat(prompt):
    """ Repite hasta que el usuario ingrese S o N """
    while True:
        res = input(prompt).strip().upper()
        if res in ['S','N']:
            return res
        else:
            print("Error. Ingrese solo S o N.")

def main():
    """Función principal"""

    while True:
        limpiar_terminal()
        print(SEP + " FACTORIAL DE UN NÚMERO " + SEP)
        print("1. Resolver de la forma iterativa.")
        print("2. Resolver de la forma recursiva (con bucle).")
        print("3. Salir.")
        
        opcion = validar_opc("Ingresa una opción (1-3): ", 1 , 3)

        if opcion == 1:

            while True:

                limpiar_terminal()
                print(" RESOLVER DE LA FORMA ITERATIVA ")
                numero = validar_entero("\nIngrese el número que desea saber su factorial: ")

                print(f" > El factorial de el número -> {numero}:")
                print(f" > {factorial(numero)}")

                rep = repeat("¿Desea repetir la operación? S/N: ")
                if rep == 'N':
                    break
        
        elif opcion == 2:

            while True:  

                limpiar_terminal()
                print(" RESOLVER DE LA FORMA RECURSIVA ")
                numero = validar_entero("\nIngrese el número que desea saber su factorial: ")

                print(f" > El factorial de el número -> {numero}:")
                print(f" > {numero}! = {factorial_recursivo(numero)}")

                rep = repeat("¿Desea repetir la operación? S/N: ")
                if rep == 'N':
                    break

        elif opcion == 3:

            print("Saliendo del programa...")
            break
        
if __name__ == "__main__":
    main()