# ejercicio4.py - Calificación
# Pide nota (0-100) y muestra:
# 90-100: A, 80-89: B, 70-79: C, 60-69: D, <60: F
def calificacion (nota):
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >=70:
        return "C"
    elif nota >=60:
        return "D"
    else:
        return "F"
    
while True:
    try:
        nota = float(input("Ingrese su nota: "))
        if 0 <= nota <= 100:
            break
        else:
            print("Valor invalido. Ingrese un numero positivo entre 0 y 100")
    except ValueError:
        print("Valor invalido. Ingrese valores numericos. ")

print(f"Tu nota es {nota}, por ende tu calificacion es: {calificacion(nota)}")
