# ejercicio26.py - Palíndromo
# ANTES de codificar, escribe:
# 1. Qué es un palíndromo (en tus palabras)
# 2. Pasos en español:
#    - Quitar espacios
#    - Convertir a minúsculas
#    - Comparar texto con su reverso
# 3. Ahora codifica
import os
def es_palindromo(text):
    # "anilina" -> True
    # "python" -> False
    # Ignora mayúsculas y espacios
    return text == text[::-1]

def repeat(prompt):
    while True:
        res = input(prompt).strip().upper()
        if res in ['S','N']:
            return res
        else:
            print("Error. Ingrese solo S o N.")

def normalize_text(text):
    cleanText = text.lower().replace(" ", "")
    replace = (
        ('a','á'),
        ('e','é'),
        ('i','í'),
        ('o','ó'),
        ('u','ú')
    )
    for a, b in replace:
        if b in cleanText:
            cleanText = cleanText.replace(b, a)
    return cleanText

def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    
    while True:
        clean_terminal()
        print("=" * 10 + " ¿ES PALINDROMO? " + "=" * 10)    
        text = input("Ingrese el texto o palabra: ").strip()
        textClean = normalize_text(text)

        if es_palindromo(textClean):
            print(f"\n -> '{text}' es un palindromo.")

        else:
            print(f"\n -> '{text}' no es un palindrimo.")

        res = repeat("\n¿Desea probar con otro texto? S/N: ")
        if res == 'N': 
            print("Saliendo del programa...")
            break

if __name__ == '__main__':
    main()