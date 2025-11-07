# mini_calculadora.py
# Sistema de calculadora con:
# - Operaciones básicas
# - Historial de operaciones (lista de diccionarios)
# - Guardar historial en archivo de texto
# - Menú completo
# Esto debe tomar 2-3 horas
# Si te toma menos, no lo estás haciendo bien
# Si te toma más de 5 horas, estás sobre-pensando
import datetime as dt
import os
import time
SEP = "=" * 20 

#========================
#Funciones de operaciones
#========================

def sumar(n1, n2):
    """Suma dos números y devuelve el resultado."""
    resultado = n1 + n2
    return resultado

def restar(n1, n2):
    """Resta dos números y devuelve el resultado."""
    resultado = n1 - n2
    return resultado

def multiplicar(n1, n2):
    """Multiplica dos números y devuelve el resultado."""
    resultado = n1 * n2
    return resultado

def dividir(n1, n2):
    """Divide dos números y devuelve el resultado."""
    resultado = n1 / n2
    return resultado

def guardar_operacion(n1, operacion, n2, resultado, historial):
    """Guarda la operación realizada en el historial."""
    historial.append({
        "operacion" : f"{n1} {operacion} {n2}",
        "resultado" : resultado
        })

    return historial

def realizar_operacion(n1, n2, operacion, historial):
    """Realiza la operación solicitada y guarda el resultado en el historial."""
    resultado = None

    if operacion == "+":
        resultado = sumar(n1, n2)
    
    elif operacion == "-":
        resultado = restar(n1, n2)
    
    elif operacion == "*":
        resultado = multiplicar(n1, n2)
    
    elif operacion == "/":
        resultado = dividir(n1, n2)

    guardar_operacion(n1, operacion, n2, resultado, historial)

    return f"\n > {formatear_numero(n1)} {operacion} {formatear_numero(n2)} = {formatear_numero(resultado)}\n"

def mostrar_historial(historial):
    """Muestra el historial de operaciones en pantalla."""

    fecha_y_hora_actual = dt.datetime.now()
    for operacion in historial:
        print(f"\nOperaciones de: {fecha_y_hora_actual.strftime('%d/%m/%Y a las %H:%M:%S')}")
        for clave, valor in operacion.items():
            print(f"{clave}: {valor}")
        print("\n" + "-" * 50)    
    print()

def guardar_txt(historial):
    """Guarda el historial de operaciones en un archivo de texto."""

    fecha_y_hora_actual = dt.datetime.now()
    with open("historial.txt", "a") as operaciones:

        operaciones.write("\n\n" + "="*50 + "\n")
        operaciones.write(f"OPERACIONES DE: {fecha_y_hora_actual.strftime('%d/%m/%Y a las %H:%M:%S')}\n")
        operaciones.write("="*50 + "\n")

        for operacion in historial:
            operaciones.write("-"*30 + "\n")
            for clave, valor in operacion.items():
                operaciones.write(f" > {clave}: {valor}\n")
            
    
#==================
# FUNCIONES UTILES
#==================

def validar_numero(prompt):
    """ Valida que el usuario ingrese un número válido """
    while True:
        try:
            numero = float(input(prompt))
            return numero
        
        except ValueError:
            print("Error. Ingrese un valor numérico.")

def preguntar_numeros():
    """ Pregunta al usuario por dos números válidos """

    n1 = validar_numero("Ingresa el primer número: ")
    n2 = validar_numero("Ingresa el segundo número: ")

    return n1, n2

def preguntar_numeros_division():
    """ Pregunta al usuario por dos números válidos, asegurando que el segundo no sea 0 """

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
    """Ejecuta una función de menú y permite repetirla según la elección del usuario."""
    while True:
        if menu == menu_historial:
            menu(historial)
            if not historial:
                print("Saliendo al menú principal...")
                time.sleep(3)
                return 'N'
            res = input("Oprima cualquier letra para volver al menú: ")
            return 'N'
        
        menu(historial)
        res = repeat("¿Desea repetir esta operacion? S/N: ")
        if res == 'N':
            return res
    
def formatear_numero(num):
    """Formatea un número para mostrarlo sin decimales si es entero."""
    if isinstance(num, float) and num.is_integer():
        return int(num)
    return num

def clean_terminal():
    """Limpia la terminal, dependiendo del sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_opcion(prompt, valor_min, valor_max):
    """Valida que el usuario ingrese una opción dentro de un rango específico."""
    while True:
        try:
            opc = int(input(prompt))
            if valor_min <= opc <= valor_max:
                return opc
            else:
                print(f"Error. Fuera del rango ({valor_min} - {valor_max}).")
        except ValueError:
            print("Error. Ingresa una opcion válida.")

#===================
# FUNCIONES DE MENÚ
#===================

def menu_sumar(historial):
    """Menú para realizar la suma de dos números."""
    clean_terminal()
    print(SEP + " SUMAR " +  SEP + "\n")
    
    n1, n2 = preguntar_numeros()
    resultado = realizar_operacion(n1, n2, "+", historial) 
    
    print(resultado)

def menu_restar(historial):
    """Menú para realizar la resta de dos números."""
    clean_terminal()
    print(SEP + " RESTAR " +  SEP + "\n")
    
    n1, n2 = preguntar_numeros()
    resultado = realizar_operacion(n1, n2, "-", historial) 
    
    print(resultado)

def menu_multiplicar(historial):
    """Menú para realizar la multiplicación de dos números."""
    clean_terminal()
    print(SEP + " MULTIPLICAR " +  SEP + "\n")
    
    n1, n2 = preguntar_numeros()
    resultado = realizar_operacion(n1, n2, "*", historial) 
    
    print(resultado)

def menu_dividir(historial):
    """Menú para realizar la división de dos números."""

    clean_terminal()
    print(SEP + " DIVIDIR " +  SEP + "\n")
    
    n1, n2 = preguntar_numeros_division()
    resultado = realizar_operacion(n1, n2, "/", historial) 
    
    print(resultado)

def menu_historial(historial):
    """Menú para mostrar y guardar el historial de operaciones."""

    clean_terminal()
    print(SEP + " HISTORIAL " +  SEP)

    if historial:
        mostrar_historial(historial)

        res = repeat("¿Desea guardar su historial en un archivo .txt? S/N: ")
        if res == 'S':
            guardar_txt(historial)
            print(" > Archivo guardado exitosamente.")
    else:
        print("\t No hay operaciones registradas.\n")


#===================
# FUNCIÓN PRINCIPAL
#===================

def main():
    """Función principal que ejecuta el menú de la calculadora."""
    historial = []
    while True:
        clean_terminal()
        print(SEP + " CALCULADORA " + SEP)
        
        print("1. Sumar.")
        print("2. Restar.")
        print("3. Multiplicar.")
        print("4. Dividir.")
        print("5. Mostrar historial.")
        print("6. Salir.")

        opc = validar_opcion("\nIngrese una opción: ", 1 , 6)

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