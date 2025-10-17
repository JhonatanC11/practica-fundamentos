# ejercicio22.py - Contador de palabras
def contar_palabras(texto):
    """Cuenta la cantidad de veces que aparece cada palabra en el texto"""
    palabras = {}
    for palabra in texto.split():
        if palabra in palabras:
            palabras[palabra] += 1
        else:
            palabras[palabra] = 1
    return palabras

def mostrar_palabras(texto):
    """Muestra las palabras y la cantidad de veces que aparecen"""
    palabras = contar_palabras(texto)
    for palabra, veces in palabras.items():
        print(f"'{palabra}' : {veces} veces")

def validar_texto(texto_input):
    """Valida que el nombre no esté vacío"""
    while True:
        texto = input(texto_input).strip().lower()
        if texto: 
            return texto
        else:
            print("Error. El texto no puede estar vacío")

def repetir(pregunta):
    """Realiza la pregunta para repetir una operacion"""
    while True:
        resp = input(pregunta).strip().lower()
        if resp in ['s', 'n']:
            return resp
        else:
            print("Error. Ingrese solo S para si o N para no.")

# Menú principal
while True:
    print("=" * 10 + " CONTADOR DE PALABRAS " + "=" * 10)
    texto = validar_texto("Ingrese un texto: ")
    mostrar_palabras(texto)
    resp = repetir("¿Desea repeteir esta acción? S/N: ")
    if resp == 'n':
        print("Saliendo del programa...")
        break