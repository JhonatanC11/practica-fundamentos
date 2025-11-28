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
            
            self.stock -= cantidad
            
            return True, f'Venta registrada correctamente. Stock actual: {self.stock}'
        
        return False, f'Stock en 0. No es posible vender.'
    
    def __str__(self):
        # Retorna string descriptivo del objeto
        return f"{self.nombre}: ${self.precio}"


class Inventario:

    def __init__(self):
        self.productos = {}
    
    def validar_existencia(self, nombre):

        productos = self.productos
        
        if nombre in productos.keys():
            return True
        
        return False

    def obtener(self, nombre):
        return self.productos.get(nombre, None)
    
    def agregar(self, nombre, precio, stock):

        existe = self.validar_existencia(nombre)

        if existe:
            return False, f"El producto '{nombre}' ya existe."

        self.productos[nombre] = Producto(nombre, precio, stock)
        return True, 'Producto agregado correctamente.'
    
    def editar_nombre(self, nombre, nuevo_nombre):

        existe = self.validar_existencia(nombre)

        if not existe:

            return False, f'El producto {nombre} no existe.'
        

        if self.validar_existencia(nuevo_nombre):
            return False, f"El nombre '{nuevo_nombre}' ya está en uso."
            
        product = self.productos.pop(nombre)
        self.productos[nuevo_nombre] = product

        return True, 'Nombre actualizado correctamente.'
    
    def editar_precio(self, nombre, nuevo_precio):

        existe = self.validar_existencia(nombre)

        if not existe:
            return False, f'El producto {nombre} no existe.'
        

        self.productos[nombre]
    
    def editar_stock(self, nombre, stock):

        producto = self.productos[nombre] 
        existe = self.validar_existencia(nombre)

        if existe:

            producto['stock'] = stock

            return True, 'Stock actualizado correctamente.'
        
        return False, f"El producto '{nombre}' no existe"
    
    def eliminar(self, nombre):

        producto = self.productos[nombre]
        existe = self.validar_existencia(nombre)

        if existe:

            del producto

            return True, f"El producto '{nombre}' ha sido eliminado correctamente."
        
        return False, f"El producto '{nombre}' no existe."