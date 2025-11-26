# ejercicio33.py - Clase Producto
import os
SEP = "-" * 30

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def aplicar_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            return False, 'Descuento inválido. Debe estar entre 0 y 100.'
        
        self.precio = self.precio * (1 - porcentaje/100)

        return True, f'Descuento aplicado. Nuevo precio: ${self.precio:.2f}'
    
    def vender(self, cantidad):

        if self.stock > 0:

            if cantidad > self.stock:
                return False, f'No hay suficiente cantidad en stock. Stock actual: {self.stock}'
            
            self.stock =- cantidad
            
            return True, f'Venta registrada correctamente. Stock actual: {self.stock}'
        
        return False, f'Stock en 0. No es posible vender.'
    
    def __str__(self):
        # Retorna string descriptivo del objeto
        return f"{self.nombre}: ${self.precio}"

#-----------------
# FUNCIONES DE UI
#-----------------

# MENÚS
def menu_ver_productos(inventario):
    
    print(SEP + " PRODUCTOS " + SEP + "\n")


# UTILES 
def pedir_opcion(prompt):

    while True:

        opcion = input(prompt)

        ok, data = validar_opcion(opcion, min_opcion=1, max_opcion=5)

        if ok:
            return data
        
        else:
            print(f"\n{data}\n")

#------------------
# FUNCIONES ÚTILES
#------------------

def validar_opcion(opcion, min_opcion, max_opcion):
    
    """
    Docstring for validar_opcion
    
    :param opcion: Opción a validar
    :param min_opcion: Opción minima del menú
    :param max_opcion: Opción maxima del menú

    """
    try:
        opcion = int(opcion)

        if min_opcion <= opcion <= max_opcion:
            return True, opcion
        
        else:
            return False, f'ERROR: Fuera del rango ({min_opcion} - {max_opcion}).'
    
    except ValueError:
        return False, 'ERROR: Ingrese un valor válido.'

def ver_productos(inventario):

    if inventario:
        
        for llave, valor in inventario.items():
            print(f" - {llave}: {valor}")
        
    else:
        print("\n\t\t No hay productos registrados.\n")

#------------------
# FUNCIÓN PRINCIPAL
#------------------

def main():

    SEP = "-" * 30
    inventario = {}

    print(SEP + " GESTIÓN DE INVENTARIO " + SEP + "\n")
    print("\t\t1. Ver productos.", end=" ")
    print("\t2. Agregar producto.")
    print("\t\t3. Aplicar descuento.", end= " ")
    print("\t4. Vender producto.")
    print("\t\t5. Editar producto.", end=" ")
    print("\t6. Salir.\n")

    opcion = pedir_opcion("Seleccione una opción (1-6): ")

    if opcion == 1:
        menu_ver_productos(inventario)
        

if __name__ == '__main__':
    main()