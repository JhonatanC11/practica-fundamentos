def tiene_mayuscula(contraseña):
    for char in contraseña:
        if 'A' <= char <= 'Z':
            return True
    return False

def tiene_numero(contraseña):
    for char in contraseña:
        if '0' <= char <= '9':
            return True
    return False
    
def es_password_valida(contraseña):
    if len(contraseña) < 8:
        return False
    elif not tiene_mayuscula(contraseña):
        return False
    elif not tiene_numero(contraseña):
        return False
    else:
        return True
    
def password_valida_meto(contraseña):
    if len(contraseña) < 8:
        return False
    elif not any(char.isupper() for char in contraseña):
        return False
    elif not any(char.isdigit() for char in contraseña):
        return False
    else:
        return True 

print("=" * 10 + " Validador de contraseña " + "=" * 10)
print("Su contraseña debe tener al menos:\n 1. 8 caracteres\n 2. Una mayúscula\n 3. Un número")

print("Usando lógica pura: ")
while True:
    contraseña = input("Ingrese una contraseña: ")
    if es_password_valida(contraseña):
        print("Bien hecho. Tu contraseña es válida.")
        break
    else:
        if len(contraseña) < 8:
            print("Tu contraseña debe tener al menos 8 caracteres.") 
        elif not tiene_numero(contraseña):
            print("Tu contraseña debe tener al menos un número.")
        elif not tiene_mayuscula(contraseña):
            print("Tu contraseña debe tener al menos una mayúscula.")

print("Ahora usando métodos de python: ")

while True:
    contraseña = input("Ingrese una contraseña: ")
    if password_valida_meto(contraseña):
        print("Bien hecho. Tu contraseña es válida.")
        break
    else:
        if len(contraseña) < 8:
            print("Tu contraseña debe tener al menos 8 caracteres.") 
        elif not tiene_numero(contraseña):
            print("Tu contraseña debe tener al menos un número.")
        elif not tiene_mayuscula(contraseña):
            print("Tu contraseña debe tener al menos una mayúscula.")
