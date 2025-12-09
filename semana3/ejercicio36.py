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
        estado = '❌ Prestado' if self.prestado else '✅ Disponible'
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
    
def limpiar_terminal():
    """Limpia la terminal según el sistema operativo."""
    os.system("cls" if os.name == 'nt' else 'clear') 

def mostrar_menu():
    print("\n" + SEP)
    print("SISTEMA DE GESTIÓN DE BIBLIOTECA".center(50))
    print(SEP)
    print("\n1. Mostrar libros.")
    print("2. Agregar libro.")
    print("3. Buscar libro por titulo.")
    print("4. Prestar libro.")
    print("5. Devolver libro.")
    print("0. Salir\n")
    print(SEP)

def menu_mostrar_libros(biblioteca):
    print("\n --- LIBROS --- \n")

    if not biblioteca.libros:
        print("❌ Biblioteca vacía.")
        return
    
    for i, libro in enumerate(biblioteca.libros, 1):
        print(f" {i}. {libro}.")

def menu_agregar_libro(biblioteca):
    print("\n --- AGREGAR LIBRO --- \n")
    
    titulo = input("Titulo del libro: ").strip()
    if not titulo:
        print("❌ El titulo no puede estar vacío.")
        return

    autor = input("Autor: ").strip()
    if not autor:
        print("❌ El autor no puede estar vacío.")
        return
    
    nuevo_libro = Libro(titulo, autor)
    exito, mensaje = biblioteca.agregar_libro(nuevo_libro)
    
    print("✅" if exito else "❌", mensaje)

def menu_buscar_libro(biblioteca):
    print("\n --- BUSCAR LIBRO --- \n")

    titulo = input("Titulo del libro: ").strip()
    libro = biblioteca.buscar_por_titulo(titulo)

    if not libro:
        print(f"❌ El libro '{titulo}' no existe.")
        return
    
    print(f"✅ Libro encontrado: {libro}")

def menu_prestar_libro(biblioteca):
    print("\n --- PRESTAR LIBRO --- \n")

    titulo = input("Titulo del libro: ").strip()
    libro = biblioteca.buscar_por_titulo(titulo)
    
    if not libro:
        print(f"❌ El libro '{titulo}' no existe.")
        return
    
    exito = libro.prestar()
    if exito:
        print(f"✅ El libro '{titulo}' ha sido prestado correctamente.")
    else:
        print(f"❌ El libro '{titulo}' ya está prestado.")
    
def menu_devolver_libro(biblioteca):
    print("\n --- DEVOLVER LIBRO --- \n")

    titulo = input("Titulo del libro: ").strip()
    libro = biblioteca.buscar_por_titulo(titulo)

    if not libro:
        print(f"❌ El libro '{titulo}' no existe.")
        return
    
    exito, mensaje = libro.devolver()
    print("✅" if exito else "❌", mensaje)

def main():
    biblioteca = Biblioteca()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            menu_mostrar_libros(biblioteca)
        elif opcion == '2':
            menu_agregar_libro(biblioteca)
        elif opcion == '3':
            menu_buscar_libro(biblioteca)
        elif opcion == '4':
            menu_prestar_libro(biblioteca)
        elif opcion == '5':
            menu_devolver_libro(biblioteca)
        elif opcion == '0':
            print("Saliendo del sistema de gestión de biblioteca. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Por favor, intente de nuevo.")
        
        input("\nPresione Enter para continuar...")
        limpiar_terminal()

if __name__ == "__main__":
    main()