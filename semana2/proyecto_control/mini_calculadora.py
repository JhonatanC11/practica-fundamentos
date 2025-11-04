# mini_calculadora.py
# Sistema de calculadora con:
# - Operaciones básicas
# - Historial de operaciones (lista de diccionarios)
# - Guardar historial en archivo de texto
# - Menú completo
# Esto debe tomar 2-3 horas
# Si te toma menos, no lo estás haciendo bien
# Si te toma más de 5 horas, estás sobre-pensando
import os
SEP = "=" * 20 

#========================
#Funciones de operaciones
#========================

def sumar(n1, n2):
    resultado = n1 + n2
    return resultado

def restar(n1, n2):
    resultado = n1 - n2
    return resultado

def multiplicar(n1, n2):
    resultado = n1 * n2
    return resultado

def dividir(n1, n2):
    resultado = n1 / n2
    return resultado

def guardar_operacion(n1, operacion, n2, resultado, historial):

    historial.append({
        "operacion" : f"{n1} {operacion} {n2}",
        "resultado" : resultado
        })

    return historial

def realizar_operacion(n1, n2, operacion, historial):

    if operacion == "+":
        resultado = sumar(n1, n2)
    
    elif operacion == "-":
        resultado = restar(n1, n2)
    
    elif operacion == "*":
        resultado = multiplicar(n1, n2)
    
    elif operacion == "/":
        resultado = dividir(n1, n2)

    guardar_operacion(n1, operacion, n2, resultado, historial)

    return f"\n{formatear_numero(n1)} {operacion} {formatear_numero(n2)} = {formatear_numero(resultado)}"

def mostrar_historial(historial):
    for operacion in historial:
        print(SEP)
        for clave, valor in operacion.items():
            print(f"{clave}: {valor}")
        print(SEP)    
        print()

def guardar_txt(historial):
    operaciones = open("operaciones.txt", "x")
    for operacion in historial:
        operaciones.write(SEP+"\n")
        for clave, valor in operacion.items():
            operaciones.write(f"{clave}: {valor}")
        operaciones.write("\n"+SEP)    
        operaciones.write("\n")
    operaciones.close()
    
#==================
# FUNCIONES UTILES
#==================

def validar_numero(prompt):
    while True:
        try:
            numero = float(input(prompt))
            return numero
        
        except ValueError:
            print("Error. Ingrese un valor numérico.")

def preguntar_numeros():
    
    n1 = validar_numero("Ingresa el primer número: ")
    n2 = validar_numero("Ingresa el segundo número: ")

    return n1, n2

def preguntar_numeros_division():
    n1 = validar_numero("Ingresa el primer número: ")
    
    while True:
        n2 = validar_numero("Ingresa el segundo número: ")
        
        if not n2 == 0:
            break
        else:
            print("Error. No es posible la división entre 0.")
        
    return n1, n2

def repeat(prompt):
    """ Repite hasta que el usuario ingrese S o N """
    while True:
        res = input(prompt).strip().upper()
        if res in ['S','N']:
            return res
        else:
            print("Error. Ingrese solo S o N.")

def ejecutar_con_repeticion(menu, historial):
    while True:
        menu(historial)
        res = repeat("Desea repetir esta operacion? S/N: ")
        if res == 'N':
            break
    
def formatear_numero(num):
    if isinstance(num, float) and num.is_integer():
        return int(num)
    return num

def clean_terminal():
    """Limpia la terminal, dependiendo del sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

#===================
# FUNCIONES DE MENÚ
#===================

def menu_sumar(historial):
    clean_terminal()
    print(SEP + " SUMAR " +  SEP + "\n")
    
    n1, n2 = preguntar_numeros()
    resultado = realizar_operacion(n1, n2, "+", historial) 
    
    print(resultado)

def menu_restar(historial):
    clean_terminal()
    print(SEP + " RESTAR " +  SEP + "\n")
    
    n1, n2 = preguntar_numeros()
    resultado = realizar_operacion(n1, n2, "-", historial) 
    
    print(resultado)

def menu_multiplicar(historial):
    clean_terminal()
    print(SEP + " MULTIPLICAR " +  SEP + "\n")
    
    n1, n2 = preguntar_numeros()
    resultado = realizar_operacion(n1, n2, "*", historial) 
    
    print(resultado)

def menu_dividir(historial):
    clean_terminal()
    print(SEP + " DIVIDIR " +  SEP + "\n")
    
    n1, n2 = preguntar_numeros_division()
    resultado = realizar_operacion(n1, n2, "/", historial) 
    
    print(resultado)

def menu_historial(historial):
    print(SEP + " HISTORIAL " +  SEP + "\n")

    if historial:
        mostrar_historial(historial)

        res = repeat("Desea guardar su historial en un archivo .txt? S/N: ")
        if res == 'S':
            guardar_txt(historial)
        

    



#===================
# FUNCIÓN PRINCIPAL
#===================

def main():
    historial = []
    while True:
        clean_terminal()
        print(SEP + " CALCULADORA " + SEP)
        
        print("1. Sumar.")
        print("2. Restar.")
        print("3. Multiplicar.")
        print("4. Dividir.")

        opc = int(input("\nIngrese una opción: "))

        if opc == 1:
            ejecutar_con_repeticion(menu_sumar, historial)
        
        elif opc == 2:
            ejecutar_con_repeticion(menu_restar, historial)
        
        elif opc == 3:
            ejecutar_con_repeticion(menu_multiplicar, historial)
        
        elif opc == 4:
            ejecutar_con_repeticion(menu_dividir, historial)
        
        elif opc == 5:
            ejecutar_con_repeticion(menu_historial, historial)

        elif opc == 6:
            print("Saliendo del programa...")
            break

    
if __name__ == "__main__":
    main()    
