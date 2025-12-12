# ejercicio40.py - JSON básico
import json

def guardar_contactos(contactos, archivo):
    # contactos es un diccionario
    # Guardar en JSON
    """Convierte los datos de un diccionario en un JSON"""
    try:
        with open(archivo, "w") as f:
            json.dump(contactos, f, indent=4)
        
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")

    except Exception as e:
        print(f"Error escribiendo el archivo: {e}")

def cargar_contactos(archivo):
    # Leer JSON y retornar diccionario
    """Lee un archiovp JSON y retorna un diccionario"""
    
    try:
        with open(archivo) as f:
            datos = json.load(f)
            return datos

    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")

    except Exception as e:
        print(f"Error escribiendo el archivo: {e}")

# DICCIONARIO DE EJEMPLO:
contactos = {
    "messi" : {
        "telefono" : "123456",
        "correo" : "10101",
        "apodo" : "cr7",
        "datos adicionales": {
            "RH" : "A+",
            "edad" : 28,
            "sueldo": 1275.48,
            "hijos" : {
                "cantidad" : 2,
                "primer_hijo":{
                    "nombre": "juan",
                    "edad" : 10,
                },
                "segundo_hijo": {
                    "nombre" : "Messi",
                    "edad" : 7                }
            }
        }
    },
    "cierrroalas7" : "123",
    "critian orlando" : "123456"
}

guardar_contactos(contactos, "ejemplo.json")
print(cargar_contactos("ejemplo.json"))