# ejercicio19.py - Validador de contraseña
def tiene_mayuscula(password):
    for char in password:
        hay_mayuscula = False
        if char == char.upper():
            hay_mayuscula = True
            break     
    return hay_mayuscula

def tiene_numero(password):
    hay_numero = False
    for char in password:
        try:
            if int(char):
                hay_numero = True
                break
        except ValueError:
            pass
    return hay_numero
    
def es_password_valida(password):
    # Debe tener al menos:
    # - 8 caracteres
    # - Una mayúscula
    # - Un número
    # Retorna True o False
    if len(password) < 8:
        return False
    elif not tiene_mayuscula(password):
        return False
    elif not tiene_numero(password):
        return False
    else:
        return True
    
    
contraseña = input("Ingrese su contraseña: ")
print(es_password_valida(contraseña))


        



        
        
            
            

        
