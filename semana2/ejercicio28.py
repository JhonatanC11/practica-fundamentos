# ejercicio28.py - Anagrama
# "amor" y "roma" -> True
# "python" y "java" -> False
import os
SEPARADOR = "=" * 20
def son_anagramas(palabra1, palabra2):
    """ Retorna True si las palabras son anagramas """
    return sorted(palabra1) == sorted(palabra2)

def normalizar_palabra(palabra):
    """ Normaliza la palabra quitando espacios, pasando a minúsculas y quitando acentos """
    palabra_limpia = palabra.lower().replace(" ", "")
    remplazo = (
        ('a','á'),
        ('e','é'),
        ('i','í'),
        ('o','ó'),
        ('u','ú')
    )
    # Reemplaza las vocales acentuadas por las sin acento
    for i,j in remplazo:
        palabra_limpia = palabra_limpia.replace(j,i)

    return palabra_limpia

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

def main():
    """ Función principal """
    while True:
        clean_terminal()
        print(SEPARADOR + " ¿ES ANAGRAMA? " + SEPARADOR)
        print("A continuación ingresa las dos palabras a comparar.\n")
        
        palabra1 = input(" > Ingresa la primera palabra: ")
        palabra1 = normalizar_palabra(palabra1) # Normaliza la palabra
        
        palabra2 = input(" > Ahora ingresa la segunda palabra: ")
        palabra2 = normalizar_palabra(palabra2)
        print()
        if son_anagramas(palabra1, palabra2):
            print(f"Las palabras '{palabra1}' y '{palabra2}' son anagramas.")
        else:
            print(f"Las palabras '{palabra1}' y '{palabra2}' no son anagramas.")
        
        res = repeat("\n¿Desea comparar otras palabras? S/N: ")
        if res == 'N':
            print("Saliendo del programa...")
            break    

if __name__ == '__main__':
    main()