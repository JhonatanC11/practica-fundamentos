# ejercicio15.py - Eliminar duplicados
# Lista con números repetidos
# Crear nueva lista sin duplicados
# No usar set()
lista = [1, 2, 2, 3, 4, 4, 5, 5, 5]
nueva_lista = []

for num in lista:
    if not num in nueva_lista:
        nueva_lista.append(num)

print(f"Lista inicial: {lista}")
print(f"Lista sin duplicados: {nueva_lista}")