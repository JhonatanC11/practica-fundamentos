# ejercicio7.py - Contador regresivo
# Desde 10 hasta 0, imprimiendo cada número
# Al llegar a 0 imprime "¡Despegue!"
import time
contador = 10
while contador >= 0:
    print(contador)
    contador -= 1
    if contador >= 0:
        time.sleep(1)

print("¡Despegue!")   
