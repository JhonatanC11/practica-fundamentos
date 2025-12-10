# ejercicio37.py - Sistema de Empleados
import os 

SEP = "-" * 60

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
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
        return f"Nombre: {self.nombre}  -  Salario: ${self.salario:.2f}"

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
    
    def validar_existencia(self, empleado):
        return empleado in self.empleados
    
    def contratar(self, empleado):
        """Agrega un emplea a la lista de empleados."""
        
        if not isinstance(empleado, Empleado):
            return False, "ERROR: Se esperaba un objeto de tipo Empleado."
        
        self.empleados.append(empleado)
        return True, f"Empleado agregado correctamente."
    
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
    
    print("\n --- CONTRATAR EMPLEADO --- \n")

    nombre_emp = input("Nombre del empleado: ").strip()
    salario_emp = input("Salario: ")

    if not nombre_emp or not salario_emp:
        print("❌ El nombre y el salario no pueden estar vacíos.")
        return
    
    nuevo_empleado = Empleado(nombre_emp, salario_emp)
    exito, mensaje = empresa.contratar(nuevo_empleado)

    print("✅" if exito else "❌", mensaje)

def menu_aumentar_salario(empresa):
    print("\n --- AUMENTAR SUELDO --- \n")
    
    nombre_emp = input("Nombre del empleado: ").strip()
    porcentaje = float(input("Porcentaje de aumento: "))



