# ejercicio29.py - Números primos
# Retorna lista de todos los primos hasta n
import os
import math
SEPARADOR = "=" * 20

# FUNCIONES PRINCIPALES: 
def es_primo(numero):
    """ Retorna True si el número es primo """
    if numero < 2:
        return False
    
    if numero == 2:
        return True
    
    if numero % 2 == 0:
        return False
    
    limite = int(math.isqrt(numero))
    for divisor in range(3, limite + 1, 2):
        if numero % divisor == 0:
            return False
    return True

def primos_hasta(n):
    """ Retorna una lista con todos los números primos hasta n """
    numeros_primos = []
    for numero in range (2, n+1):
        if es_primo(numero):
            numeros_primos.append(numero)
    return numeros_primos

#FUNCIONES DE UTILIDAD:

def clean_terminal():
    """Limpia la terminal, dependiendo del sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def repeat(prompt):
    """ Repite hasta que el usuario ingrese S o N """
    while True:
        res = input(prompt).strip().upper()
        if res in ['S','N']:
            return res
        else:
            print("Error. Ingrese solo S o N.")

def validar_entero_positivo(prompt):
    """ Valida que el usuario ingrese un número entero positivo """
    while True:
        try:
            numero = int(input(prompt))
            if numero > 0:
                return numero
            else:
                print("Error. Ingrese solo números enteros positivos.")
        except ValueError:
            print("Error. No se permiten letras.")

def validar_opcion(prompt, valor_ini, valor_limi):
    """ Valida que el usuario ingrese una opción dentro de un rango """
    while True:
        try:
            opcion = int(input(prompt))
            if valor_ini <= opcion <= valor_limi:
                return opcion
            else:
                print("Error. Ingrese una opción válida.")
        except ValueError:
            print("Error. Ingrese solo números enteros.")

def main():
    """ Función principal """

    while True:

        try:
            clean_terminal()
            print(SEPARADOR + " NÚMEROS PRIMOS " + SEPARADOR)
            print("\n 1. Saber si un número es primo o no.")
            print(" 2. Mostrar todos los primos hasta 'n' número.")  
            print(" 3. Salir.\n")

            opcion = validar_opcion("Ingrese una opción: ", 1 , 3)
            print()

            if opcion == 1:

                while True:
                    numero = validar_entero_positivo("Ingrese el número: ")

                    if es_primo(numero):
                        print(f"El número {numero} es primo.")
                    else:
                        print(f"El número {numero} no es primo.")

                    res = repeat("\n¿Deseas probar con otro número? S/N: ")
                    if res == 'N':
                        break
            
            elif opcion == 2:

                while True:

                    numero = validar_entero_positivo("¿Hasta que número deseas mostrar los primos?: ")
                    primos = primos_hasta(numero)
                    print(f"Los numeros primos hasta {numero} son:\n -> {primos}")

                    res = repeat("\n¿Desea consultar con otro número? S/N: ")
                    if res == 'N':
                        break
            elif opcion == 3:
                print("Saliendo del programa...")
                break

        except ValueError:
            print("Error. Ingrese solo números.")

# EJECUCIÓN DEL PROGRAMA
if __name__ == '__main__':
    main()      