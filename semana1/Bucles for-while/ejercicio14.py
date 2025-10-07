# ejercicio14.py - Número mayor y menor
# Lista de números
# Encuentra el mayor y el menor SIN usar max() o min()
numeros = [45, 23, 67, 12, 89, 34]
menor = numeros[0]
mayor = numeros[0]
for i in numeros:
    if i < menor:
        menor = i
    elif i > mayor:
        mayor = i
print(f"De la lista {numeros}:")
print(f" El número mayor es: {mayor}")
print(f" El número menor es: {menor}")