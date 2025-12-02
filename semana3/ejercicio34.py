# ejercicio34.py - Clase Rectangulo
import os
SEP = "-" * 50

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        """Calcula el área de un rectángulo."""
        
        if self.base <= 0 or self.altura <= 0: 
            return False, "ERROR: Las dimensiones de un rectángulo deben ser números positivos."
        
        area = self.base * self.altura 
        return True, f"El área del rectángulo es de: {area:.2f}"
    
    def calcular_perimetro(self):
        """Calcula el perimetro de un rectángulo."""

        if self.base <= 0 or self.altura <= 0:
            return False, "ERROR: Las dimensiones de un rectángulo deben ser números positivos."
        
        perimetro = 2 * (self.base + self.altura)

        return True, f"El perimetro del rectángulo es de: {perimetro:.2f}"


# =========== FUNCIONES DE INTERFAZ =========== #

def limpiar_terminal():
    """Limpia la terminal según el sistema operativo."""
    os.system("cls" if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Muestra el menú principal."""

    print("\n" + SEP)
    print("ÁREA Y PERIMETRO DE UN RECTÁNGULO".center(50))
    print(SEP + "\n")
    print("1. Calcular el área.")
    print("2. Calcular perimetro.")
    print("3. Salir.")
    print("\n" + SEP)

def menu_area():
    """Muestra el menú para calcular el área."""
    print("\n --- CALCULAR ÁREA --- \n")

    try:
        base = float(input("Base: "))
        altura = float(input("Altura: "))

        rectangulo_1 = Rectangulo(base, altura)
        
        exito, mensaje = rectangulo_1.calcular_area()
        print("✅" if exito else "❌", mensaje)

    except ValueError:
        print("❌ Valores inválidos. Verifique e intente nuevamente.")

def menu_perimetro():
    """Muestra el menú para calcular el perimetro."""
    print("\n --- CALCULAR PERIMETRO --- \n")

    try:
        base = float(input("Base: "))
        altura = float(input("Altura: "))

        rectangulo_1 = Rectangulo(base, altura)
        
        exito, mensaje = rectangulo_1.calcular_perimetro()
        print("✅" if exito else "❌", mensaje)
        
    except ValueError:
        print("❌ Valores inválidos. Verifique e intente nuevamente.")

# ========== FUNCIÓN DE EJECUCIÓN PRINCIPAL =======

def main():
    """ FUNCIÓN PRINCIPAL """
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            menu_area()
        elif opcion == "2":
            menu_perimetro()
        elif opcion == "3":
            print(" ¡Hasta Luego!...")
            break
        else: 
            print("❌ Opción inválida.")
        
        input("\nPresione Enter para continuar...")
        limpiar_terminal()

if __name__ == "__main__":
    main()