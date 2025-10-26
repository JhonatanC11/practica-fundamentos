# ejercicio25.py - Traductor simple
# Función que traduce, si no existe retorna "Traducción no disponible"
traducciones = {
    "hola": "hello",
    "adios": "goodbye",
    "gracias": "thank you"
}

def traducir(palabra, traducciones):
    palabra = palabra.lower().strip()
    return traducciones.get(palabra, "Traducción no disponible")

def repetir(prompt):
    while True:
        res = input(prompt).lower().strip()
        if res in ['s', 'n']:
            return res
        else:
            print("Error. Ingrese solo S o N.")

def agregar_traduccion(palabra, traduccion, traducciones):
    traducciones[palabra] = traduccion
    return True

while True:
    
    print("=" * 10 + " TRADUCTOR SIMPLE " + "=" * 10) 
    print("1. Traducir una palabra.")
    print("2. Agregar una tradución.")
    print("3. Mostrar traducciones.")
    
    try:
        opcion = int(input("\nIngrese una opción: "))

        if opcion == 1:    
            while True:
                palabraTraducir = input("Ingresa la palabra a traducir: ").strip()
                if palabraTraducir:
                    print(traducir(palabraTraducir, traducciones))
            
                else:
                    print("La palabra no puede estar vacía.")

                confirmar = repetir("¿Desea traducir otra palabra? S/N: ")
                if confirmar == 'n':
                    print("Volviendo al menú...")
                    break
        
        elif opcion == 2:
            while True:    
                palabra = input("Ingresa la palabra que deseas agregar: ")
                traduccion = input(f"Ahora ingresa la palabra '{palabra}' traducida al inglés: ")
                if agregar_traduccion(palabra, traduccion, traducciones):
                    print("Traducción agregada correctamente.")

                confirmar = repetir("¿Desea agregar otra tradución? S/N: ")
                if confirmar == 'n':
                    print("Volviendo al menú...")
                    break
        
        elif opcion == 3:
            while True:
                print("Traducciones disponibles: \n")
                for key, value in traducciones.items():
                    print(f" > {key}: {value}")
                print()

                confirmar = repetir("Digite 'S' para volver al menú: ")
                if confirmar == 's':
                    break
        
        else:
            print("Error. Ingrese una opción válida.")
    
    except ValueError:
        print("Error. Ingrese solo números enteros.")