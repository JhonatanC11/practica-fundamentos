
#==================
#      CLASES 
#==================
class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
    
    def marcar_como_prestado(self):

        if not self.disponible:
            return False, "El libro ya está prestado."
        
        self.disponible = False
        return True, "Libro marcado como prestado."
    
    def marcar_como_disponible(self):

        if self.disponible:
            return False, "El libro ya estaba marcado como disponible"
        
        self.disponible = True
        return True, "Libro marcado como disponible"

class Usuario:

    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.libros_prestados = []
        self.deuda = 0

    def obtener_libros_prestados(self):
        return self.libros_prestados
    
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
    
    def validar_existencia_usuario(self, identificacion):
        return any(usuario.identificacion == identificacion for usuario in self.usuarios)
    
    def agregar_usuario(self, nombre, identificacion):
        
        if self.validar_existencia_usuario(identificacion):
            return False, "Este usuario ya existe."
        
        nuevo_usuario = Usuario(nombre, identificacion)
        self.usuarios.append(nuevo_usuario)
        
        return True, "Usuario agregado correctamente."

hola = Biblioteca()
print(hola.agregar_usuario("Juan", "123"))
print("¿Existe el usuario?: ", hola.validar_existencia_usuario("123"))
print(hola.agregar_usuario("Juan", "123"))