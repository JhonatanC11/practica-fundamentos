# ejercicio22.py - Contador de palabras
texto = "python es genial python es poderoso python es facil"
#def contar_palabras(texto):
palabras = {}
veces = 0
for palabra in texto.split():
    if palabra == palabra:
        veces +1
    else:
        palabras[palabra] = veces

print(palabras)