# ejercicio27.py - Fibonacci
# Retorna los primeros n números de Fibonacci
# fibonacci(5) -> [0, 1, 1, 2, 3]
# Pasos:
# 1. Entender qué es Fibonacci
# 2. Empezar con [0, 1]
# 3. Siguiente número = suma de los dos anteriores
# 4. Repetir n veces

import os # Importa el módulo os para limpiar la terminal
def fibonacci(n):
    """ Retorna los primeros n números de Fibonacci """
    numeros = [0, 1]
    for numero in range (n-2):
        valor_siguiente = numeros[numero] + numeros[numero+1]
        numeros.append(valor_siguiente)
    return numeros

def repeat(prompt):
    """ Repite hasta que el usuario ingrese S o N """
    while True:
        res = input(prompt).strip().upper()
        if res in ['S','N']:
            return res
        else:
            print("Error. Ingrese solo S o N.")

def clean_terminal():
    """ Limpia la terminal """
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """ Función principal """
    while True:
        try:
            clean_terminal()
            print("=" * 10 + " NUMEROS FIBONACCI " + "=" * 10)
            n = int(input("Ingrese el número que desea saber su secuencia: "))
            if n > 0:
                secuencia = fibonacci(n) 
                print(f"\n > La secuencia del número {n} es : {secuencia}")
                res = repeat("\n¿Desea hallar la secuencia de otro número? S/N: ")
                if res == 'N': 
                    print("Saliendo del programa...")
                    break
            else:
                print("Error. Ingrese solo números mayores que 0.")
        except ValueError:
            print("Error. Ingrese solo números enteros positivos.")
            
if __name__ == '__main__':
    main()