# ejercicio36.py - Biblioteca
import os 

SEP = "-" * 50

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False
    
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False
    
    def devolver(self):
        
        if not self.prestado:
            return False, f"El libro '{self.titulo}' no estaba prestado."
        
        self.prestado = False
        return True, f"El libro '{self.titulo}' se ha devuelto correctamente."
    
    def esta_prestado(self):
        return self.prestado
    
    def __str__(self):
        estado = '✅ Prestado' if self.prestado else '❌ Disponible'
        return f"Titulo: {self.titulo}  -  Autor: {self.autor}  -  Estado: {estado}"

class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        
        if not isinstance(libro, Libro):
            return False, "ERROR: Se esperaba un objeto de tipo Libro."
        
        if self.libro_existe(libro.titulo):
            return False, f"El libro '{libro.titulo}' ya existe."
        
        self.libros.append(libro)
        return True, f"El libro '{libro.titulo}' se agregó correctamente."
    
    def buscar_por_titulo(self, titulo):
        
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None
    
    def libro_existe(self, titulo):
        return any(libro.titulo == titulo for libro in self.libros)
    
    def libros_disponibles(self):
        return [libro for libro in self.libros if not libro.prestado]
    
    def libros_prestados(self):
        return [libro for libro in self.libros if libro.prestado]
    
    def listar_libros(self):
        if not self.libros:
            return []
        return self.libros
    
    def total_libros(self):
        return len(self.libros)
    
    def __str__(self):

        if not self.libros:
            return "Biblioteca vacía."
        
        disponibles = len(self.libros_disponibles)
        prestados = len(self.libros_prestados)

        return f"Biblioteca: {self.total_libros} libros ({disponibles} disponibles. {prestados} prestados.)"
    

def mostrar_menu():
    print("\n" + SEP)
    print("SISTEMA DE GESTIÓN DE BIBLIOTECA".center(50))
    print(SEP)
    print("1. Mostrar libros.")
    print("2. Agregar libro.")
    print("3. Buscar libro por titulo.")
    print("0. Salir")
    print(SEP + "\n")

def menu_mostrar_libros(biblioteca):
    print(" --- LIBROS --- \n")

    if not biblioteca.libros:
        print("❌ Biblioteca vacía.")
        return
    
    for i, libro in enumerate(biblioteca.libros, 1):
        print(f" {i}. {libro}.")

def menu_agregar_libro(biblioteca):
    print(" --- AGREGAR LIBRO --- \n")

    titulo = input("Titulo del libro: ").strip()
    autor = input("Autor: ").strip()
    nuevo_libro = Libro(titulo, autor)
    exito, mensaje = biblioteca.agregar_libro(nuevo_libro)
    
    print("✅" if exito else "❌", mensaje)