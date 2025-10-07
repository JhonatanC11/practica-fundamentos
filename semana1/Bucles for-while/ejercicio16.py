# ejercicio16.py - Calculadora
def sumar(num1, num2):
    suma = num1 + num2 
    return suma

def restar(num1, num2):
    rest = num1 - num2
    return rest

def multiplicar(num1, num2):
    multi = num1 * num2 
    return multi

def dividir(num1, num2):
    if num2 == 0:
        divi = "No es posible la division entre cero."
    else:
        divi = num1 / num2
    return divi

print("=" * 10 + " CALCULADORA " + "="*10)
print("Operaciones disponibles:")
print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n")
operacion = int(input("Elige una operación (1-4): "))
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if operacion == 1:
    resul = sumar(num1, num2)
    print(f"{num1:.0f} + {num2:.0f} = {resul:.0f}")
elif operacion == 2:
    resul = restar(num1, num2)
    print(f"{num1:.0f} - {num2:.0f} = {resul:.0f}")
elif operacion == 3:
    resul = multiplicar(num1, num2)
    print(f"{num1:.0f} x {num2:.0f} = {resul:.0f}")
elif operacion == 4:
    resul = dividir(num1, num2)
    print(f"{num1:.0f} / {num2:.0f} = {resul:.0f}")

