# ejercicio13.py - Promedio de calificaciones
# Pide 5 calificaciones
# Calcula y muestra el promedio

print("="*10 + " PROMEDIO NOTAS " + "="*10)
notas = [] 

for i in range(5):
    while True:
        try:
            nota_user = float(input(f"Ingrese la {i+1} nota: "))
            if 5 >= nota_user >= 0:
                notas.append(nota_user)
                break
            else:
                print("Error. Ingrese un nota entre 0 y 5")
        except ValueError:
            print("Error. Por favor ingrese solo números")

promedio = sum(notas) / len(notas)

print(f"El promedio es: {promedio}")
if promedio < 3:
    print("Tu promedio esta por debajo de 3.0. Has Reprobado :(")
else:
    print("¡Felicidades!. Has aprobado :)")