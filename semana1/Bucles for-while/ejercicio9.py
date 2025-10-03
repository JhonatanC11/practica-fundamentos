# ejercicio9.py - Suma números positivos
# Pide números al usuario hasta que ingrese -1
# Muestra la suma de todos los números positivos
total = 0
while True:
    try:
        numero = int(input("Ingrese un número: "))
        if numero == -1:
            break
        if numero > 0:
            total += numero 
        
    except ValueError:
        print("Ingrese solo números enteros.")
    
print(f"La suma de los números positivos es: {total}")
