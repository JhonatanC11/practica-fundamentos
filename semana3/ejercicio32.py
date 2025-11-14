# ejercicio32.py - Clase CuentaBancaria
import os
import time

SEP = "-" * 30
SEP1 = "=" * 30

class CuentaBancaria:
    def __init__(self, titular, saldo_actual, contactos, num_cuenta):
        self.titular = titular
        self.num_cuenta = num_cuenta 
        self.saldo_actual = saldo_actual
        self.contactos = contactos
    
    def depositar(self, monto):
        """ Deposita un monto en la cuenta """

        self.saldo_actual += monto
        return {
            'exito' : True,
            'mensaje' : 'Depósito realizado exitósamente.'
        }
    
    def retirar(self, monto):
        """ Retira un monto de la cuenta """

        if monto > self.saldo_actual:
            return {
                'exito': False,
                'mensaje' : f'Saldo insuficiente. Saldo actual: {self.saldo_actual}'
            }
        
        self.saldo_actual -= monto
        return {
            'exito' : True,
            'mensaje' : 'Retiro realizado exitósamente.'
        }
    
    def hay_saldo(self):
        """ Verifica si hay saldo en la cuenta """

        if self.saldo_actual > 0:
            return True
        return False
    
    def enviar_dinero(self, monto, destinatario):
        """ Envía dinero a otra cuenta """

        if monto > self.saldo_actual:
            return {
                'exito' : False,
                'mensaje' : f'Error: Saldo insuficiente. Saldo actual: {self.saldo_actual}'
            }
        
        self.saldo_actual -= monto
        destinatario.saldo_actual += monto
        return {
            'exito' : True,
            'mensaje' : 'Envío realizado exitósamente.',
            'monto' : monto
        }
    
    def agregar_cuenta(self, titular, num_cuenta):
        """ Agrega una nueva cuenta a los contactos """

        if titular in self.contactos:
            return {
                'exito': False,
                'mensaje': f'{titular} ya existe en tus cuentas registradas.'
            }
        
        elif num_cuenta in self.contactos:
            return {
                'exito': False,
                'mensaje': f'El número de cuenta {num_cuenta} ya existe en tus cuentas registradas.'
            }
        
        self.contactos[titular] = num_cuenta
        return {
            'exito': True,
            'mensaje': 'Cuenta registrada correctamente.'
        }
    
    

def validar_opc(prompt, valor_min, valor_max):
    """Valida que la opción ingresada sea correcta"""

    while True:
        try:
            opcion = int(input(prompt))
            if valor_min <= opcion <= valor_max:
                return opcion
            else:
                print("Error. Fuera del rango.")
        except ValueError:
            print("Error. Ingrese una opcion válida.")

def validar_monto(prompt):
    """ Valida que el monto ingresado sea correcto """

    while True:

        try:
            monto = float(input(prompt))
            if monto > 0:
                return monto
            else:
                print("Error: Ingrese un monto válido.")

        except ValueError:
            print("Error: Ingrese un monto válido.")

def validar_num_cuenta(prompt):
    """ Valida que el número de cuenta ingresado sea correcto """

    while True:
        try:
            num_cuenta = int(input(prompt))
            if num_cuenta > 0:
                return num_cuenta 

            else:
                print("Error: Ingrese un número de cuenta válido.")
        
        except ValueError:
            print("Error: Ingrese un número de cuenta válido.")


def agregar_cuenta_obj(nombre_titular, num_cuenta, saldo_actual = 1000):
    """ Crea un objeto CuentaBancaria como ejemplo de cuenta destinataria """

    cuenta_1 = CuentaBancaria(nombre_titular, saldo_actual, {}, num_cuenta)
    return cuenta_1


def limpiar_terminal():
    """ Limpia la terminal """

    os.system('cls' if os.name == 'nt' else 'clear')

def repetir(prompt):
    """ Repite hasta que el usuario ingrese S o N """
    while True:
        res = input(prompt).strip().upper()
        if res in ['S','N']:
            return res
        else:
            print("Error. Ingrese solo S o N.")

def main ():
    """ Función principal del programa """

    # Crear una cuenta bancaria principal
    cuenta_principal = CuentaBancaria("Jhonatan", 1000.0, {'Juan':1001, 'Messi':1002 }, 123456) 
    
    while True:
        
        limpiar_terminal()
        print("\n" + SEP + " CUENTA BANCARIA " + SEP + "\n")
        print(f"\t\tBienvenido {cuenta_principal.titular}")
        print(f"\t\tSaldo actual: {cuenta_principal.saldo_actual}\n")
        print(" 1. Depositar.")
        print(" 2. Retirar.")
        print(" 3. Enviar.")
        print(" 4. Ver cuentas registradas.")
        print(" 5. Agregar cuentas.")
        print(" 6. Salir.")

        opc = validar_opc(" \nSelecciona una opcion (1-6): ", 1 , 6)

        if opc == 1:
            
            while True:
                limpiar_terminal()
                print("\n" + SEP + " DEPOSITAR " + SEP + "\n")

                monto = validar_monto("Ingrese el monto a depositar en su cuenta: ")
                resultado = cuenta_principal.depositar(monto)

                if resultado['exito']:
                    
                    print(f"\n {resultado['mensaje']}\n")

                    respuesta = repetir("¿Desea depósitar nuevamente? S/N: ")
                    if respuesta == 'N': break

                else:
                    
                    print(resultado['mensaje'])
                    print("Volviendo al menú principal...")
                    time.sleep(3)
                    break

        
        elif opc == 2:
            
            while True:

                limpiar_terminal()
                print("\n" + SEP + " RETIRAR " + SEP + "\n")
                print(f"\t\tSaldo actual: {cuenta_principal.saldo_actual}\n")

                if cuenta_principal.hay_saldo():
                    
                    monto = validar_monto("Ingrese el monto a retirar: ")
                    resultado = cuenta_principal.retirar(monto)

                    if resultado["exito"]:
                        print(f"\n{resultado["mensaje"]}\n")

                        respuesta = repetir("¿Desea realizar otro retiro? S/N: ")
                        if respuesta == 'N': break
                    
                    else:
                        print(f"\n{resultado["mensaje"]}\n")
                        print("Volviendo al menú principal...")
                        time.sleep(2)
                        break

                else:
                    print("\nSu saldo es $0, imposible retirar.\n")
                    print("Volviendo al menú principal...")
                    time.sleep(2)
                    break
        
        elif opc == 3:

            while True: 
                
                limpiar_terminal()
                print("\n" + SEP + " ENVIAR " + SEP + "\n")
                print(f"\t\tSaldo actual: {cuenta_principal.saldo_actual}\n")
                print(" 1. Enviar a cuentas registradas.")
                print(" 2. Enviar a una nueva cuenta.")
                print(" 3. Volver.")

                opc_envio = validar_opc("\nSeleccione una opción: ", 1 , 3 )

                if opc_envio == 1:
                    
                    limpiar_terminal()
                    print("\n" + SEP + " ENVIAR " + SEP + "\n")

                    if cuenta_principal.contactos:
                        
                        print("Cuentas registradas: \n") 
                        
                        for i, titular in enumerate(cuenta_principal.contactos.keys(), start=1):
                            print(f"\t{i}. {titular}")
                        print()

                        indice_titular = validar_opc("Seleccione el indice de la cuenta: ", 1, len(cuenta_principal.contactos))
                        titular_seleccionado = list(cuenta_principal.contactos.keys())[indice_titular - 1]
                        num_cuenta = cuenta_principal.contactos[titular_seleccionado]

                        monto = validar_monto("Ingrese el monto a enviar: ")
                        cuenta_1 = CuentaBancaria(titular_seleccionado, 1000, {}, num_cuenta)

                        resultado = cuenta_principal.enviar_dinero(monto, cuenta_1)

                        if resultado["exito"]:
                            
                            print(f"\n{resultado['mensaje']}\n")
                            print(f"${resultado['monto']} enviados a {cuenta_1.titular}.\n")
                        
                        else:
                            print(f"\n{resultado['mensaje']}\n")
                        
                        print("Volviendo al menú...")
                        time.sleep(5)

                    else:
                        
                        print("\n\t\t No hay cuentas registradas.\t\t\n")
                        time.sleep(3)
                
                elif opc_envio == 2:

                    limpiar_terminal()
                    print("\n" + SEP + " ENVIAR " + SEP + "\n")
                    
                    nombre_titular = input("Ingrese el nombre del titular: ")
                    num_cuenta = validar_num_cuenta("Ingrese el numero de cuenta: ")

                    cuenta_1 = agregar_cuenta_obj(nombre_titular, num_cuenta)

                    monto = float(input("Ingrese el monto a enviar: "))
                    
                    resultado = cuenta_principal.enviar_dinero(monto, cuenta_1)

                    if resultado["exito"]:
                        
                        print(f"\n{resultado["mensaje"]}\n")
                        print(f"${resultado["monto"]} enviados a {cuenta_1.titular}.\n")
                        
                        res = repetir("¿Desea agregar este contacto? S/N: ")

                        if res == 'S':
                            resultado = cuenta_principal.agregar_cuenta(nombre_titular, num_cuenta)

                            if resultado["exito"]:
                                print(f"\n{resultado["mensaje"]}\n")
                            
                            else:
                                print(f"\n{resultado["mensaje"]}\n")
                    else:

                        print(f"\n{resultado["mensaje"]}\n")

                    print("Volviendo al menú...")
                    time.sleep(3)
                    
                elif opc_envio == 3:
                    break 

        elif opc == 4:
            
            while True:
                
                limpiar_terminal()
                print("\n" + SEP1 + " CUENTAS REGISTRADAS " + SEP1)

                if cuenta_principal.contactos:
                    cuentas = cuenta_principal.contactos
                    for nombre, num_cuenta in cuentas.items():
                        print(f"\n\t- Nombre: {nombre}\n\t- Número cuenta: {num_cuenta}\n")
                        print("-" * 80)
                    print()

                    input("Oprima enter para volver al menu...")
                    break

                else:
                    print("\n\t\t No hay cuentas registradas.\t\t\n")
                    time.sleep(3)
                    break

        elif opc == 5:
            
            while True:
                
                limpiar_terminal()
                print("\n" + SEP + " REGISTRAR NUEVA CUENTA " + SEP + "\n")
                
                while True:

                    limpiar_terminal()
                    print("\n" + SEP + " REGISTRAR NUEVA CUENTA " + SEP + "\n")

                    cuentas = cuenta_principal.contactos
                    nombre_titular = input("Ingrese el nombre del titular de la cuenta: ")
                    num_cuenta = validar_num_cuenta(f"Ingrese el número de cuenta de {nombre_titular}: ")

                    if nombre_titular in cuentas.keys():

                        print(f"\n\t{nombre_titular} ya existe en tus cuentas registradas.\n\n")
                        respuesta = repetir("¿Desea intentarlo nuevamente? S/N: ")
                        if respuesta == 'N':
                            break

                    elif num_cuenta in cuentas.values():
                        
                        print(f"\n\tEl número de cuenta: {num_cuenta} ya está registrado.\n\n")
                        respuesta = repetir("¿Desea intentarlo nuevamente? S/N: ")

                        if respuesta == 'N':
                            break
                    
                    

                    cuenta_1 = agregar_cuenta_obj(nombre_titular, num_cuenta)

                    if cuenta_principal.agregar_cuenta(nombre_titular,num_cuenta):

                        print(f"\n{nombre_titular} agregado correctamente.\n")
                        break
                
                respuesta = repetir("¿Desea agregar otra cuenta? S/N: ")

                if respuesta == 'N':
                    break
        
        elif opc == 6:
            
            print("Saliendo del programa...")
            break

if __name__ == '__main__':
    main()