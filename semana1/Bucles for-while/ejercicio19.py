# ejercicio19.py - Validador de contraseña
"""
def es_password_valida(password):
    # Debe tener al menos:
    # - 8 caracteres
    # - Una mayúscula
    # - Un número
    # Retorna True o False
    if len(password) < 8:
        return False
    for char in password:
        if not char == char.upper():
            return False
        if not char == int:
"""        

password = "ho1la"  

for char in password:
    try:
        if not char == int(char):
            break
        
    except ValueError:
        print(f"{char} no")




        
        
            
            

        
