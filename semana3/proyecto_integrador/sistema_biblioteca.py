from datetime import datetime, timedelta
import json


# ==================
#      CLASES
# ==================
class Libro:

    def __init__(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.disponible = True


class Usuario:

    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre


class Prestamo:
    def __init__(self, id_libro, id_usuario, dias_prestamo):
        self.id_libro = id_libro
        self.id_usuario = id_usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_limite = self.fecha_prestamo + timedelta(days=dias_prestamo)
        self.devuelto = False
        self.multa_pagada = False

    def esta_atrasado(self):
        if self.devuelto:
            return False

        return datetime.now() > self.fecha_limite

    def calcular_dias_atraso(self):
        fecha_actual = datetime.now()
        if fecha_actual <= self.fecha_limite:
            return 0
        dias_atraso = fecha_actual - self.fecha_limite
        return dias_atraso.days

    def to_dict(self):

        return {
            "id_libro": self.id_libro,
            "id_usuario": self.id_usuario,
            "fecha_prestamo": self.fecha_prestamo.isoformat(),
            "fecha_limite": self.fecha_limite.isoformat(),
            "devuelto": self.devuelto,
            "multa_pagada": self.multa_pagada,
        }


class Bibiblioteca:

    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.prestamos = []
        self.multa_dias_atraso = 100

    def agregar_libro(self, libro):
        if libro.id_libro in self.libros:
            return False, f"Error: Ya existe un libro con este ID: '{libro.id_libro}'"

        self.libros[libro.id_libro] = libro
        return True, f"El libro '{libro.titulo}' se agregó correctamente."

    def agregar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            return (
                False,
                f"Error: Ya existe un usuario con este ID: '{usuario.id_usuario}'",
            )

        self.usuarios[usuario.id_usuario] = usuario
        return True, f"El usuario '{usuario.nombre}' se agregó correctamente."

    def prestar_libro(
        self, id_usuario, id_libro, dias_prestamo, archivo="prestamos.json"
    ):

        if not id_usuario in self.usuarios:
            return False, f"Usuario con ID: '{id_usuario}' no encontrado."

        libro = self.libros.get(id_libro)

        if not libro:
            return False, f"Libro con ID: '{id_libro} no encontrado."

        if not libro.disponible:
            return False, f"El libro '{libro.titulo}' no está disponible."

        if self.ver_prestamos_usuarios(id_usuario) >= 3:
            return False, f"Error: El usuario ya alcanzó su límite de prestamos."

        nuevo_prestamo = Prestamo(id_libro, id_usuario, dias_prestamo)
        libro.disponible = False
        self.prestamos.append(nuevo_prestamo)

        ok, mensaje = self.guardar_prestamos_json(archivo)
        if not ok:
            return False, mensaje

        return True, f"El libro '{libro.titulo}' se prestó correctamente."

    def devolver_libro(self, id_libro):

        libro = self.libros.get(id_libro)

        if not libro:
            return False, f"No se encontró un libro con este ID: '{id_libro}'"

        for prestamo in self.prestamos:
            if prestamo.id_libro == id_libro:
                break

        if not prestamo:
            return False, f"No se encontró ningún prestamo del libro con ID: {id_libro}"

        if prestamo.devuelto:
            return False, f"Error. El libro con ID: '{id_libro}' ya se había devuelto."

        if prestamo.esta_atrasado():

            if not prestamo.multa_pagada:
                multa = self.calcular_multa(prestamo)
                return False, f"Multa pendiente por pagar: ${multa}"

        prestamo.devuelto = True
        libro.disponible = True
        return True, "Libro devuelto exitósamente."

    def calcular_multa(self, prestamo):
        return prestamo.calcular_dias_atraso() * self.multa_dias_atraso

    def pagar_multa(self, prestamo, monto):

        if not prestamo in self.prestamos:
            return False, "El prestamo no existe."

        if prestamo.devuelto:
            return False, "El prestamo no está activo."

        multa = self.calcular_multa(prestamo)

        if not monto >= multa:
            return (
                False,
                f"El monto a pagar ({monto}) no cubre el total de la multa ({multa}).",
            )

        prestamo.multa_pagada = True
        return True, f"Multa pagada con éxito."

    def ver_prestamos_usuarios(self, id_usuario):
        libros_prestados = [p.id_usuario == id_usuario for p in self.prestamos]
        return len(libros_prestados)

    def guardar_prestamos_json(self, archivo):

        try:
            with open(archivo, "w") as file:
                json.dump(
                    [prestamo.to_dict() for prestamo in self.prestamos], file, indent=4
                )
                return True, "Prestamos guardados correctamente en JSON."

        except Exception as e:
            return False, f"Error. Hubo un problema durante la escritura: {e}"


biblioteca = Bibiblioteca()

libro1 = Libro("L001", "El poder del ahora", "Jhonatan")
libro2 = Libro("L002", "Cien años de soledad", "Garcia Marquez")
libro3 = Libro("L003", "Deja de ser tú", "Joe Dispenza")
libro4 = Libro("L004", "Meditaciones", "Marco Aurelio")

usuario1 = Usuario("U001", "Jhonatan Camacho")
usuario2 = Usuario("U002", "Juan Pablo")
usuario3 = Usuario("U003", "Alejandrina")
usuario4 = Usuario("U004", "Cristinita")

print("AGREGAR LIBROS: ")
print(biblioteca.agregar_libro(libro1))
print(biblioteca.agregar_libro(libro2))
print(biblioteca.agregar_libro(libro3))
print(biblioteca.agregar_libro(libro4))


print("\nAGREGAR LIBRO QUE YA EXISTE: ")
print(biblioteca.agregar_libro(libro1))

print("\nAGREGAR USUARIOS: ")
print(biblioteca.agregar_usuario(usuario1))
print(biblioteca.agregar_usuario(usuario2))
print(biblioteca.agregar_usuario(usuario3))
print(biblioteca.agregar_usuario(usuario4))

print("\nAGREGAR USUARIO QUE YA EXISTE: ")
print(biblioteca.agregar_usuario(usuario1))

print("\nLIBROS: ")
print(biblioteca.libros)

print("\nUSUARIOS: ")
print(biblioteca.usuarios)

print("\nPRESTAR LIBRO: \n")
print(biblioteca.prestar_libro("U001", "L001", 15))

print("\nPRESTAR EL MISMO LIBRO: ")
print(biblioteca.prestar_libro("U001", "L001", 15))

print("\nPRESTAR +3 LIBROS: \n")
print(biblioteca.prestar_libro("U001", "L002", 15))
print(biblioteca.prestar_libro("U001", "L003", 15))
print("Libros prestados:", biblioteca.ver_prestamos_usuarios("U001"))
print(biblioteca.prestar_libro("U001", "L004", 15))

print("\nPRESTAR LIBRO QUE NO EXISTE: \n")
print(biblioteca.prestar_libro("U001", "L006", 15))

print("\nPRESTAR LIBRO A USUARIO QUE NO EXISTE: \n")
print(biblioteca.prestar_libro("U006", "L001", 15))
