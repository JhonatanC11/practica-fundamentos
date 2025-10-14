# ejercicio21.py - Agenda de contactos
contactos = {"Juan":{
    "email" : "ejemplo@meail.com",
    "telefono": 123456
    }}

def agregar_contacto(nombre, telefono, email):
    contactos.update({nombre: {"email":email, "telefono": telefono}})

def buscar_contacto(nombre):
    print(f"Datos de {nombre}:")
    for i,j in contactos[nombre].items():
        print(f" - {i}: {j}")

def mostrar_todos():
    for llave, valor in contactos.items():
        print(f"Datos de {llave}:")
        for i, j in valor.items():
            print(f" - {i}: {j}")

nombre = input("Nombre: ")
telefono = int(input("Telefono: "))
email = input("Email: ")

while True:
    print("=" * 10 + " AGENDA DE CONTACTOS " + "=" * 10)

agregar_contacto(nombre, telefono, email)
buscar_contacto(nombre)
mostrar_todos()

