# ejercicio41.py - CSV simple
def exportar_a_csv(datos, archivo):
    
    try:
        with open(archivo, "w") as f:
            columnas = datos[0].keys()
            f.write(",".join(columnas) + "\n")
            for diccionario in datos:
                valores = diccionario.values()
                valores_str = [str(valor) for valor in valores]
                f.write(",".join(valores_str) + "\n")           
    except Exception as e:
        print(f"Hubo un error durante la escritura: {e}")    

data = [{"nombre": "Juan", "edad": 25}, {"nombre": "Messi", "edad": 39}]
exportar_a_csv(data, "datos_ejemplo.csv")