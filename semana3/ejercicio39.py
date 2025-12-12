# ejercicio39.py - Leer archivo
def contar_lineas(nombre_archivo):
    """Cuenta la cantidad de lineas en un archivo"""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return sum(1 for _ in f)
    
    except FileNotFoundError:
        print("El archivo no existe.")

    except Exception as e:
        print(f"Error leyendo el archivo: {e}")

def contar_palabras(nombre_archivo):
    """Cuenta la cantidad de palabras en un archivo"""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
            return len(contenido.split())
        
    except FileNotFoundError:
        print("El archivo no existe.")

    except Exception as e:
        print(f"Error leyendo el archivo: {e}")

# Prueba
print(f"Cantidad de lineas: {contar_lineas("log.txt")}")
print(f"Cantidad de palabras: {contar_palabras("log.txt")}")