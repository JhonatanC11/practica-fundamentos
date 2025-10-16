# ejercicio21.py - Agenda de contactos
contactos = {"Juan":{
    "email" : "ejemplo@meail.com",
    "telefono": 123456
    }}

def agregar_contacto(nombre, telefono, email):
    """Agrega un nuevo contacto a la agenda"""
    contactos.update({nombre: {"email":email, "telefono": telefono}})

def buscar_contacto(nombre):
    """Busca un contacto por nombre y muestra sus datos"""
    if nombre in contactos:
        print(f"Datos de {nombre}:")
        print(f"Email: {contactos[nombre]["email"]}\nTelefono: {contactos[nombre]["telefono"]}")
        return True
    else:
        print(f"{nombre} no se encuentra en tus contactos.")
        return False


def mostrar_todos():
    """Muestra todos los contactos en la agenda"""
    if contactos:
        for llave, valor in contactos.items():
            print(f"Datos de {llave}:")
            for i, j in valor.items():
                print(f" - {i}: {j}")
            print()

def repetir(pregunta):
    """Realiza la pregunta para repetir una operacion"""
    while True:
        resp = input(pregunta).strip().lower()
        if resp in ['s', 'n']:
            return resp
        else:
            print("Error. Ingrese solo S para si o N para no.")

def validar_input(nombre_input):
    """Valida que el nombre no esté vacío"""
    while True:
        nombre = input(nombre_input).strip()
        if nombre: 
            return nombre
        else:
            print("Error. Ingrese un valor válido.")

def validar_opc(opc_input):
    """Valida que la opción esté en el rango correcto"""
    while True:
        try:
            opcion = int(input(opc_input))
            if 0 < opcion < 5:
                break
            else:
                print("Fuera del rango. Ingrese un valor válido")
        except ValueError:
            print("Error. Ingrese solo valores enteros")
    return opcion

def editar_contacto(nombre_input):
    """Edita el contacto si lo encuentra"""
    nom_edit = input(nombre_input)
    if buscar_contacto(nom_edit):
        while True:
            opcion = input("¿Que deseas editar? (nombre/email/telefono): ").lower().strip()
            if opcion == 'email':
                nuevo_email = input("Ingrese el nuevo email: ")
                contactos[nom_edit]["email"] = nuevo_email
                print("Correo actualizado correctamente.")
                break
            elif opcion == 'telefono':
                nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                contactos[nom_edit]["telefono"] = nuevo_telefono
                print("Telefono actualizado correctamente")
                break
            elif opcion == 'nombre':
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                contactos[nuevo_nombre] = contactos[nom_edit]
                del contactos[nom_edit]
                print("Nombre actualizado correctamente")
                break
            else:
                print("Error. Opcion inválida.")

def eliminar_contacto(nombre_input):
    """Elimina el contacto si lo encuentra"""
    nom_del = input(nombre_input)
    if buscar_contacto(nom_del):
        del contactos[nom_del]
        print("Contacto eliminado correctamente.")


# Menú principal
while True:
    print("=" * 10 + " AGENDA DE CONTACTOS " + "=" * 10)
    print("1. Agregar nuevo contacto\n2. Ver contactos\n3. Buscar contacto\n4. Salir")
    opcion = validar_opc("Ingresa una opcion (1-4): ")
    if opcion == 1:
        while True:
            print("=" * 10 + " AGREGAR CONTACTO " + "=" * 10)
            nombre_input = validar_input("Ingrese el nombre: ")
            while True:
                try:
                    telefono = input("Ingresa el telefono: ").strip()
                    if telefono.isdigit() and 0 < len(telefono) <= 10:
                        break
                    else:
                        print("Error. Ingrese un número de teléfono válido, 1 y 10 caracteres")
                except ValueError:
                    print("Error. Ingrese solo valores enteros.")

            email = validar_input("Ingresa el email: ")
            agregar_contacto(nombre_input, telefono, email)

            if nombre_input in contactos:
                print(f"El contacto {nombre_input} se agregó correctamente.")
            else:
                print("Ocurrió un error al agregar el contacto.")
            resp = repetir("¿Desea agregar otro contacto? S/N: ")
            if resp == 'n':
                print("Saliendo al menú principal...")
                break
    elif opcion == 2:
        while True:
            print("=" * 10 + " LISTA DE CONTACTOS " + "=" * 10)
            mostrar_todos()
            print("Acciones:\n 1. Editar\n 2. Borrar\n 3. Volver al menú")
            opcion = validar_opc("Digite la opción que desea realizar (1-3): ")
            if opcion == 1:
                editar_contacto("Ingrese el nombre del contaco a editar: ")
            elif opcion == 2:
                eliminar_contacto("Ingrese el nombre del contacto a eliminar: ")
            elif opcion == 3:
                print("Volviendo al menú principal...")
                break
    elif opcion == 3:
        while True: 
            nombre_bus = validar_input("Ingresa el nombre del contacto a buscar: ")
            buscar_contacto(nombre_bus)
            resp = repetir("¿Desea buscar otro contacto? S/N: ")
            if resp == 'n':
                print("Saliendo al menú principal...")
                break

    elif opcion == 4:
        print("Saliendo del programa...")
        break