# ejercicio37.py - Sistema de Empleados
import os 

SEP = "-" * 60

class Empleado:
    def __init__(self, nombre, salario, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.salario = salario
    
    def aumentar_salario(self, porcentaje):
        """Aumenta el salario de un empleado, mediante porcentaje."""
        if porcentaje <= 0:
            return False, "El porcentaje para aumentar el salario debe ser mayor que 0."
        
        aumento = self.salario * (porcentaje/100)
        self.salario += aumento
        return True, "Salario aumentado correctamente."
    
    def __str__(self):
        """Retorna el objeto de una manera mas clara."""
        return f"Nombre: {self.nombre}  -  Salario: ${self.salario:.2f}  -  Identificación: {self.identificacion}."

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
    
    def contratar(self, empleado):
        """Agrega un empleado a la lista de empleados."""
        
        if not isinstance(empleado, Empleado):
            return False, "ERROR: Se esperaba un objeto de tipo Empleado."
        
        self.empleados.append(empleado)
        return True, f"Empleado agregado correctamente."
    
    def validar_existencia(self, identificacion):
        """Verifica la existencia de un empleado mediante su identificación."""
        for empleado in self.empleados:
            if empleado.identificacion == identificacion:
                return True
        return False
    
    def obtener_empleado_por_identificacion(self, identificacion):
        """Devuelve un empleado si se encuentra, mediante su identificación"""
        for empleado in self.empleados:
            if empleado.identificacion == identificacion:
                return empleado
            
        return None
    
    def nomina_total(self):
        """Devuelve la suma de todos los salarios"""
        return sum(e.salario for e in self.empleados)
    
    def empleado_mejor_pagado(self):
        """Devuelve el empleado con el salario mas alto de la lista."""
        return max(self.empleados, key= lambda e: e.salario)

#------------------------
# FUNCIONES DE INTERFAZ 
#------------------------

def mostrar_menu():
    """Funcíon para mostrar el menú de la app."""
    
    print(SEP)
    print("EMPRESA: ELVER GOMEZ TORVA".center(60))
    print(SEP)
    print("\n1. Contratar empleado.")
    print("2. Aumentar salario.")
    print("3. Listar empleados.")
    print("4. Nomina total.")
    print("5. Mejor pagado.")
    print("0. Salir\n")
    print(SEP)

def menu_contratar(empresa):
    """Muestra el menú para contratar a un empleado"""

    print("\n --- CONTRATAR EMPLEADO --- \n")
    try:
        nombre_emp = input("Nombre del empleado: ").strip()
        identificacion = input("Identificación del empleado: ").strip()
        salario_emp = float(input("Salario: "))

        existe = empresa.validar_existencia(identificacion)
        if existe:
            print("\n❌ Ya existe un empleado con esa identificación.")
            return

        if not nombre_emp or not salario_emp or not identificacion:
            print("\n❌ Ningún campo puede estar vacío.")
            return

        nuevo_empleado = Empleado(nombre_emp, salario_emp, identificacion)
        exito, mensaje = empresa.contratar(nuevo_empleado)

        print("✅" if exito else "❌", mensaje)
    
    except ValueError:
        print("\n❌ ERROR: Ingrese un salario válido.")
        return
def menu_aumentar_salario(empresa):
    """Muestra el menú para aumentar el salario de un empleado"""
    print("\n --- AUMENTAR SUELDO --- \n")
    
    try:
        identificacion = input("Numero de identificación del empleado: ").strip()
        empleado = empresa.obtener_empleado_por_identificacion(identificacion)

        if empleado is None:
            print(f"❌ El empleado no existe.")
            return
        
        porcentaje = float(input("Porcentaje de aumento: "))
        exito, mensaje = empleado.aumentar_salario(porcentaje)
        print("✅" if exito else "❌", mensaje)

    except ValueError:
        print("❌ ERROR: Ingrese un porcentaje válido.")  
        return

def menu_listar_empleados(empresa):
    """Muestra el menú mediante una lista que contiene todos los empleados."""
    print("\n --- EMPLEADOS --- \n")

    for i, empleado in enumerate(empresa.empleados, 1):
        print(f"{i}. {empleado}")
    
def menu_nomina_total(empresa):
    """Muestra el menú para mostrar la nómina total de la empresa (suma de todos los salarios)"""
    print("\n --- NOMINA TOTAL --- \n")

    if not empresa.empleados:
        print("❌ Debe de haber al menos 1 empleado para calcular la nómina total.")
        return 
    
    nomina_total = empresa.nomina_total()
    print(f"Nómina total de la empresa: ${nomina_total:.2f}")

def menu_mejor_pagado(empresa):
    """Muestra a el empleado con mayor sueldo de la empresa."""
    print("\n --- EMPLEADO MEJOR PAGADO --- \n")

    if not empresa.empleados:
        print("❌ No hay empleados registrados.")
        return
    
    empleado_mejor_pagado = empresa.empleado_mejor_pagado()
    print(empleado_mejor_pagado)

#------------------
# FUNCIONES UTILES
#------------------
def limpiar_terminal():
    """Limpia la terminal dependiendo del sistema operativo"""
    os.system("cls" if os.name == "nt" else "clear")

#-------------------
# FUNCIÓN PRINCIPAL
#-------------------

def main():
    empresa = Empresa("ELVER GOMEZ TORVA")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            menu_contratar(empresa)
        elif opcion == '2':
            menu_aumentar_salario(empresa)
        elif opcion == '3':
            menu_listar_empleados(empresa)
        elif opcion == '4':
            menu_nomina_total(empresa)
        elif opcion == '5':
            menu_mejor_pagado(empresa)
        elif opcion == '0':
            print("¡Hasta Luego!...")
            break
        else:
            print("\n❌ Opción inválida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")
        limpiar_terminal()

if __name__ == "__main__":
    main()