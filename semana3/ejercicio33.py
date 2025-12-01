# ejercicio33.py - Clase Producto
import os
SEP = "-" * 50

class Producto:
    

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento al precio del producto."""

        if porcentaje < 0 or porcentaje > 100:
            return False, 'Descuento inválido. Debe estar entre 0 y 100.'
        
        self.precio = self.precio * (1 - porcentaje/100)

        return True, f'Descuento aplicado. Nuevo precio: ${self.precio:.2f}'
    
    def vender(self, cantidad):
        """Registra la venta de una cantidad del producto."""

        if cantidad <= 0:
            return False, f'La cantidad debe ser mayor a 0.'
        
        if self.stock == 0:
            return False, 'Stock en 0. No es posible vender.'
        
        if cantidad > self.stock:
            return False, f'Stock insuficiente. Disponible: {self.stock}'
        
        self.stock -= cantidad
        return True, f'Venta registrada. Stock actual: {self.stock}'
    
    def __str__(self):
        # Retorna string descriptivo del objeto
        return f"{self.nombre} - Precio:  ${self.precio} - Stock: {self.stock}"


class Inventario:

    def __init__(self):
        self.productos = {}
    
    def validar_existencia(self, nombre):
        """Verifica si un producto existe en el inventario."""

        return nombre in self.productos

    def obtener(self, nombre):
        """Obtiene un producto por su nombre."""
        return self.productos.get(nombre)
    
    def agregar(self, nombre, precio, stock):
        """Agrega un nuevo producto al inventario."""

        if self.validar_existencia(nombre):
            return False, f"El producto '{nombre}' ya existe."
        
        if precio < 0:
            return 'El precio no puede ser negativo.'
        
        if stock < 0:
            return False, 'El stock no puede ser negativo.'
        
        self.productos[nombre] = Producto(nombre, precio, stock)
        return True, 'Producto agregado correctamente.'
    
    def editar_nombre(self, nombre, nuevo_nombre):
        """Edita el nombre de un producto existente."""

        if not self.validar_existencia(nombre):

            return False, f'El producto {nombre} no existe.'
        

        if self.validar_existencia(nuevo_nombre):
            return False, f"El nombre '{nuevo_nombre}' ya está en uso."
            
        producto = self.productos.pop(nombre)
        producto.nombre = nuevo_nombre
        self.productos[nuevo_nombre] = producto

        return True, 'Nombre actualizado correctamente.'
    
    def editar_precio(self, nombre, nuevo_precio):
        """Edita el precio de un producto existente."""

        if not self.validar_existencia(nombre):
            return False, f'El producto {nombre} no existe.'
        
        if nuevo_precio < 0:
            return False, 'El precio no puede ser negativo.'

        self.productos[nombre].precio = nuevo_precio
        return True, 'Precio actualizado correctamente.'
    
    def editar_stock(self, nombre, nuevo_stock):
        """Edita el stock de un producto existente."""

        if not self.validar_existencia(nombre):
            return False, f"El producto '{nombre}' no existe"
        
        if nuevo_stock < 0:
            return False, 'El stock no puede ser negativo.'
        
        self.productos[nombre].stock = nuevo_stock
        return True, 'Stock actualizado correctamente.'
    
    def eliminar(self, nombre):
        """Elimina un producto del inventario."""

        if not self.validar_existencia(nombre):
            return False, f"El producto '{nombre}' no existe"
        
        del self.productos[nombre]
        return True, f"El producto {nombre} ha sido eliminado."
    
    def listar_productos(self):
        """Retorna una lista de todos los productos en el inventario."""

        if not self.productos:
            return []
        return list(self.productos.values())


# ==================== PROGRAMA PRINCIPAL ===================== # 

def limpiar_terminal():
    """Limpia la terminal según el sistema operativo."""
    os.system("cls" if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Muestra el menú principal del sistema."""

    print("\n" + SEP)
    print("SISTEMA DE GESTIÓN DE INVENTARIO".center(50))
    print(SEP)
    print(" 1. Agregar producto.")
    print(" 2. Ver todos los productos.")
    print(" 3. Editar producto.")
    print(" 4. Buscar producto.")
    print(" 5. Eliminar producto.")
    print(" 6. Registrar venta")
    print(" 7. Aplicar descuento")
    print(" 0. Salir")
    print(SEP)

def agregar_producto(inventario):
    """Agrega un nuevo producto al inventario."""

    print("\n --- AGREGAR PRODUCTO --- \n")

    nombre = input("Nombre del producto: ").strip()

    if not nombre:
        print(" ❌ El nombre no puede estar vacío.")
        return 
    
    try:
        precio = float(input("Precio: $"))
        stock = int(input("Stock: "))
    
    except ValueError:
        print("❌ Valores inválidos.")
    
    exito, mensaje = inventario.agregar(nombre, precio, stock)
    print("✅" if exito else "❌", mensaje)

def ver_productos(inventario):
    """Muestra todos los productos en el inventario."""

    print("\n --- LISTADO DE PRODUCTOS --- \n")

    productos = inventario.listar_productos()

    if not productos: 
        print("No hay productos registrados.")
        return 
    
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto}.")

def buscar_producto(inventario):
    """Busca un producto por su nombre."""

    print("\n --- BUSCAR PRODUCTO --- \n")

    nombre = input("Ingrese el nombre del producto: ").strip()

    producto = inventario.obtener(nombre)

    if producto:
        print("\n✅ Producto encontrado:")
        print(producto)
    
    else:
        print(f"❌ El producto '{nombre}' no existe en tu inventario.")
    
def editar_producto(inventario):
    """Edita los detalles de un producto existente."""

    print("\n --- EDITAR PRODUCTO --- \n")

    nombre = input("Nombre: ")

    if not inventario.validar_existencia(nombre):
        print(f"❌ El producto '{nombre}' no existe.")
        return
    
    print(f"\n¿Qué deseas editar del producto '{nombre}':")
    print("1. Nombre.")
    print("2. Precio.")
    print("3. Stock")

    opc = input("Selecciona una opción: ").strip()

    if opc == "1":

        nuevo_nombre = input("Nuevo nombre: ").strip()

        if not nuevo_nombre:
            print("❌ El nombre no puede estar vacío.")
            return 
        
        exito, mensaje = inventario.editar_nombre(nombre, nuevo_nombre)
    
    elif opc == "2":

        try:
            nuevo_precio = float(input("Nuevo precio: $"))
            exito, mensaje = inventario.editar_precio(nombre, nuevo_precio)
        
        except ValueError:
            print("❌ Precio inválido.")
            return
    
    elif opc == "3":

        try:
            nuevo_stock = int(input("Nuevo stock: "))
            exito, mensaje = inventario.editar_stock(nombre, nuevo_stock)
        
        except ValueError:
            print("❌ Stock inválido.")
            return
    
    else:
        print("❌ Opción inválida.")
        return
    
    print("✅" if exito else "❌", mensaje)

def eliminar_producto(inventario):
    """Elimina un producto del inventario."""

    print("\n --- ELIMINAR PRODUCTO --- \n")

    nombre = input("Nombre del producto a eliminar: ").strip()
    confirmar = input(f"¿Está seguro que desea eliminar el producto '{nombre}'? (s/n): ")

    if confirmar != "s":
        print("❌ Operación cancelada.")
        return
    
    exito, mensaje = inventario.eliminar(nombre)
    print("✅" if exito else "❌", mensaje)

def registrar_venta(inventario):
    """Registra la venta de un producto."""

    print("\n --- REGISTRAR VENTA --- \n")
    nombre = input("Nombre del producto: ").strip()

    producto = inventario.obtener(nombre)
    if not producto:
        print(f"❌ El producto '{nombre}' no existe.")
        return
    
    try:
        cantidad = int(input("Cantidad a vender: "))
        exito, mensaje = producto.vender(cantidad)
        print("✅" if exito else "❌", mensaje)
    
    except ValueError:
        print("❌ Cantidad inválida.")
    
def aplicar_descuento(inventario):
    """Aplica un descuento a un producto."""
    
    print("\n --- APLICAR DESCUENTO --- \n")
    nombre = input("Nombre del producto: ").strip()
    
    producto = inventario.obtener(nombre)

    if not producto:
        print(f"❌ El producto '{nombre}' no existe.")
        return
    
    try:
        porcentaje = float(input("Porcentaje de descuento: "))
        exito, mensaje = producto.aplicar_descuento(porcentaje)
        print("✅" if exito else "❌", mensaje)
    
    except ValueError:
        print("❌ Porcentaje inválido.")
    
def main():
    """Función principal del programa."""
    
    inventario = Inventario()

    while True:
        mostrar_menu()
        
        opcion = input("Seleccione una opción (0-7): ").strip()

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            ver_productos(inventario)
        elif opcion == "3":
            editar_producto(inventario)
        elif opcion == "4":
            buscar_producto(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            registrar_venta(inventario)
        elif opcion == "7":
            aplicar_descuento(inventario)
        elif opcion == "0":
            print("¡Hasta Luego!...")
            break
        else:
            print("❌ Opción inválida.")

        input("\nPresione Enter para continuar...")
        limpiar_terminal()

if __name__ == '__main__':
    main()  