# ejercicio12.py - Números mayores
# Lista de 10 números random
# Muestra solo los mayores a 50
import random
numeros = [random.randint(1, 100) for _ in range(10)]
num_mayores50 = [i for i in numeros if i > 50]
print(f"Los números random: {numeros}")
if num_mayores50:
    print(f"Números mayores a 50: {num_mayores50}")
else:
    print("No hay números mayores a 50 en la lista")