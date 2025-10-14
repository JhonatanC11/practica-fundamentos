# ejercicio20.py - Contador de vocales
def contar_vocales(texto):
    """Se llena un arreglo con las vocales que encuentre"""
    vocales = set()
    for char in texto.lower():
        if char in 'aeiouáéíóú':
            vocales.add(char)
    return vocales

def repetir(pregunta):
    """Realiza la pregunta para repetir una operacion"""
    while True:
        resp = input(pregunta).strip().lower()
        if resp in ['s', 'n']:
            return resp
        else:
            print("Error. Ingrese solo S para si o N para no.")

print("=" * 10 + " CONTAR VOCALES " + "=" * 10)
while True:
    texto = input("Ingrese el texto: ")
    vocales = contar_vocales(texto)
    if texto:
        print(f"El texto tiene: {len(vocales)} vocales únicas")
        if len(vocales) > 0: 
            print(f"Las vocales son: {vocales}")
    else:
        print("El texto está vacío.")
    resp = repetir("¿Desea repetir esta operacion? S/N: ")
    if resp == 'n':
        print("Saliendo del programa...")
        break