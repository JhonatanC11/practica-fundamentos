# ejercicio38.py - Escribir archivo
from datetime import datetime
# Añade mensaje a archivo log.txt con fecha/hora  

def escribir_log(mensaje, archivo = "log.txt"): 
    """Escribe un mensaje en un archivo de log con fecha y hora."""
    timestamp = datetime.now().isoformat()

    try:

        with open(archivo, "a", encoding="utf-8") as f:
            f.write("-" * 50 + "\n")
            f.write(f"MENSAJE: {mensaje}\n")
            f.write(f"HORA: {timestamp}\n")

    except Exception as e:
        print(f"Error al escribir el log: {e}")
    
# Prueba:
escribir_log("Hola, ¿cómo estas?")