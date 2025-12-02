# ejercicio35.py - Clase Libro

import os
SEP = "-" * 50

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.pagina_actual = 0
    
    def leer(self, num_paginas):
        # Avanza páginas, no puede pasar del total
        if num_paginas <= 0:
            return False, "Debe avanzar al menos 1 página."
        
        if num_paginas > self.paginas:
            return False, f"El libro '{self.titulo}' tiene solo {self.paginas} páginas."
        
        if self.pagina_actual + num_paginas > self.paginas:
            return False, f"Solo quedan {self.paginas - self.pagina_actual} páginas por leer."
        
        self.pagina_actual += num_paginas
        return True, f"{num_paginas} páginas leídas. Estás en la página {self.pagina_actual}/{self.paginas}."
     
    def progreso(self):
        # Retorna % leído
        porcentaje_leido = (self.pagina_actual / self.paginas) * 100

        return porcentaje_leido
    
    def __str__(self):
        # Retorna descripcion del objeto.
        return f"Titulo: {self.titulo}  -  Autor: {self.autor}\n   Progreso: {self.progreso()}%  -  N° Páginas: {self.paginas}"
    
class Libreria:
    
    def __init__(self):
        self.mis_libros = {}
    
    def validar_existencia(self, titulo):
        """ Valida si un libro existe por su titulo """
        
        return titulo in self.mis_libros
    
    def obtener(self, titulo):
        """ Obtiene un libro por su titulo """

        return self.mis_libros.get(titulo)
    
    def agregar(self, titulo, autor, paginas):
        """ Agrega un libro a la libreria """

        if self.validar_existencia(titulo):
            return False, f"El libro '{titulo}' ya existe."
        if paginas <= 0:
            return False, f"El número de páginas debe ser mayor que 0."
        
        self.mis_libros[titulo] = Libro(titulo, autor, paginas)
        return True, f"El libro '{titulo}' se agregó correctamente."
    
    def editar_titulo(self, titulo, nuevo_titulo):
        """ Edita el titulo de un libro existente """

        if not self.validar_existencia(titulo):
            return False, f"El libro '{titulo}' no existe."
        
        if self.validar_existencia(nuevo_titulo):
            return False, f"El titulo '{nuevo_titulo}' ya está en uso."
        
        libro = self.mis_libros.pop(titulo)
        libro.titulo = nuevo_titulo
        self.mis_libros[nuevo_titulo] = libro

        return True, "Titulo actualizado correctamente."
    
    def editar_autor(self, titulo, nuevo_autor):
        """ Edita el autor de un libro existente """

        if not self.validar_existencia(titulo):
            return False, f"El libro '{titulo}' no existe."
        
        self.mis_libros[titulo].autor = nuevo_autor
        return True, "Autor actualizado correctamente."
    
    def editar_paginas(self, titulo, nueva_paginas):
        """ Edita el número de páginas de un libro existente """

        if not self.validar_existencia(titulo):
            return False, f"El libro '{titulo}' no existe."
        
        if nueva_paginas <= 0:
            return False, "El número de páginas debe ser mayor a 0."
        
        self.mis_libros[titulo].paginas = nueva_paginas
        return True, "N° de páginas actualizado correctamente."
    
    def eliminar(self, titulo):
        """ Elimina un libro de la libreria """

        if not self.validar_existencia(titulo):
            return False, f"El libro '{titulo}' no existe."
        
        del self.mis_libros[titulo]
        return True, f"El libro '{titulo}' ha sido eliminado."
    
    def listar_libros(self):
        """ Retorna la lista de libros """

        if not self.mis_libros:
            return []

        return list(self.mis_libros.values())
        
def limpiar_terminal():
    """Limpia la terminal según el sistema operativo."""
    os.system("cls" if os.name == 'nt' else 'clear')        
 
def mostrar_menu():
    """Muestra el menú principal."""
    
    print("\n" + SEP)
    print("GESTOR DE LECTURA".center(50))
    print(SEP + "\n")
    print("1. Agregar nuevo libro.")
    print("2. Registrar avance.")
    print("3. Mis libros.")
    print("4. Editar libro.")
    print("5. Eliminar libro.")
    print("0. Salir")
    print("\n" + SEP)

def menu_agregar(libreria):
    """Menú para agregar un nuevo libro."""

    print("\n --- AGREGAR LIBRO --- \n")

    titulo = input("Titulo: ").strip()
    
    if not titulo:
        print("❌ El nombre no puede estar vacío.")
        return
    
    autor = input("Autor: ").strip()

    if not autor:
        print("❌ El autor no puede estar vacío.")
        return
    
    try:
        paginas = int(input("N° de páginas: "))
        exito, mensaje = libreria.agregar(titulo, autor, paginas)
        print("✅" if exito else "❌", mensaje)

    except ValueError:
        print("❌ ERROR: Valor de número de páginas inválido.")
        return 

def menu_registrar_avance(libreria):
    """Menú para registrar el avance de lectura de un libro."""

    print("\n --- REGISTRAR AVANCE --- \n")

    titulo = input("Titulo del libro: ").strip()

    libro = libreria.obtener(titulo)

    if not libro:
        print(f"❌ El libro '{titulo}' no existe.")
        return
    
    try:
        paginas_leidas = int(input("Número de páginas leídas: "))
        exito, mensaje = libro.leer(paginas_leidas)
        print("✅" if exito else "❌", mensaje)
    
    except ValueError:
        print("❌ ERROR: Valor de número de páginas inválido.")

def menu_ver_libros(libreria):
    """Menú para ver los libros registrados."""

    print("\n --- MIS LIBROS --- \n")

    libros = libreria.listar_libros()

    if not libros:
        print("❌ No hay libros registrados.")
        return

    for i, libro in enumerate(libros, 1):
        print(f"{i}. {libro}")
        print()

def menu_editar_libro(libreria):
    """Menú para editar los detalles de un libro."""

    print("\n --- EDITAR LIBRO --- \n")

    titulo = input("Titulo del libro: ").strip()

    if not libreria.validar_existencia(titulo):
        print(f"❌ El libro '{titulo}' no existe.")
        return  
    
    print("\n¿Que deseas editar?: \n")
    print("1. Titulo.")
    print("2. Autor.")
    print("3. Páginas.\n")

    opc = input("Seleccione una opción: ").strip()
    if opc == "1":

        nuevo_titulo = input("Nuevo titulo: ").strip()

        if not nuevo_titulo:
            print("❌ El titulo no puede estar vacío.")
            return
        
        exito, mensaje = libreria.editar_titulo(titulo, nuevo_titulo)
    
    elif opc == "2":

        nuevo_autor = input("Nuevo autor: ").strip()

        if not nuevo_autor:
            print("❌ El autor no puede estar vacío.")
            return
        
        exito, mensaje = libreria.editar_autor(titulo, nuevo_autor)
    
    elif opc == "3":
        
        try:
            nueva_paginas = int(input("Nuevas páginas: "))
            exito, mensaje = libreria.editar_paginas(titulo, nueva_paginas)
        
        except ValueError:
            print("❌ ERROR: Valor de número de páginas inválido.")
            return
    
    else:
        print("❌ ERROR: Seleccione una opción válida.")
        return

    print("✅" if exito else "❌", mensaje)

def menu_eliminar_libro(libreria):
    """Menú para eliminar un libro."""

    print("\n --- ELIMINAR LIBRO --- \n")

    titulo = input("Titulo del libro: ").strip()
    confirmar = input(f"¿Esta seguro que desea eliminar el libro '{titulo}'? (s/n): ").lower()
    
    if confirmar != "s":
        print("❌ Operacion cancelada.")
        return
    
    exito, mensaje = libreria.eliminar(titulo)
    print("✅" if exito else "❌", mensaje)

def main():
    """ Función principal del programa. """

    libreria = Libreria()

    while True:

        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_agregar(libreria)
        elif opcion == "2":
            menu_registrar_avance(libreria)
        elif opcion == "3":
            menu_ver_libros(libreria)
        elif opcion == "4":
            menu_editar_libro(libreria)
        elif opcion == "5":
            menu_eliminar_libro(libreria)
        elif opcion == "0":
            print("¡Hasta Luego!...")
            break
        else:
            print("❌ Opción inválida.")
        
        input("\nPresione Enter para continuar...")
        limpiar_terminal()

if __name__ == "__main__":
    main()