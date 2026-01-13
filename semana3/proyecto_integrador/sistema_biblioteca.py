from datetime import datetime, timedelta
import json
import unicodedata
import os

SEP = "-" * 50


# ==================
#      CLASES
# ==================
class Libro:

    def __init__(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

        # Versiones normalizadas (para busqueda)
        self._titulo_norm = normalizar_texto(titulo)
        self._autor_norm = normalizar_texto(autor)

    def to_dict(self):
        """Convierte el objeto Libro en un diccionario para JSON."""
        return {
            "id_libro": self.id_libro,
            "titulo": self.titulo,
            "autor": self.autor,
            "disponible": self.disponible,
        }


class Usuario:

    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre

        # Versiones normalizadas
        self._id_usuario_norm = normalizar_texto(id_usuario)
        self._nombre = normalizar_texto(nombre)

    def to_dict(self):
        """Convierte el objeto Usuario en un diccionario para JSON."""
        return {"id_usuario": self.id_usuario, "nombre": self.nombre}


class Prestamo:
    def __init__(
        self,
        id_libro,
        id_usuario,
        dias_prestamo=None,
        fecha_prestamo=None,
        fecha_limite=None,
        devuelto=False,
        multa_pagada=False,
    ):
        self.id_libro = id_libro
        self.id_usuario = id_usuario
        self.devuelto = devuelto
        self.multa_pagada = multa_pagada

        if fecha_prestamo and fecha_limite:
            self.fecha_prestamo = fecha_prestamo
            self.fecha_limite = fecha_limite

        else:
            self.fecha_prestamo = datetime.now()
            self.fecha_limite = self.fecha_prestamo + timedelta(days=dias_prestamo)

    def esta_atrasado(self):
        """Verifica si el préstamo está atrasado."""
        if self.devuelto:
            return False

        return datetime.now() > self.fecha_limite

    def calcular_dias_atraso(self):
        """Calcula los días de atraso del préstamo."""
        fecha_actual = datetime.now()
        if fecha_actual <= self.fecha_limite:
            return 0
        dias_atraso = fecha_actual - self.fecha_limite
        return dias_atraso.days

    def to_dict(self):
        """Convierte el objeto Prestamo en un diccionario para JSON."""
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
        """Agrega un libro al sistema de biblioteca."""
        if not libro.id_libro:
            libro.id_libro = obtener_siguiente_id(self.libros, "L")

        if libro.id_libro in self.libros:
            return False, f"Error: Ya existe un libro con este ID: '{libro.id_libro}'"

        self.libros[libro.id_libro] = libro
        ok, mensaje = self.guardar_libros_json("libros.json")
        if not ok:
            return False, mensaje
        return True, f"El libro '{libro.titulo}' se agregó correctamente."

    def agregar_usuario(self, usuario):
        """Agrega un usuario al sistema de biblioteca."""
        if not usuario.id_usuario:
            usuario.id_usuario = obtener_siguiente_id(self.usuarios, "U")

        if usuario.id_usuario in self.usuarios:
            return (
                False,
                f"Error: Ya existe un usuario con este ID: '{usuario.id_usuario}'",
            )

        self.usuarios[usuario.id_usuario] = usuario

        ok, mensaje = self.guardar_usuarios_json(archivo="usuarios.json")
        if not ok:
            return False, mensaje

        return (
            True,
            f"El usuario '{usuario.nombre}' se agregó correctamente con ID: {usuario.id_usuario}.",
        )

    def prestar_libro(
        self,
        id_usuario,
        id_libro,
        dias_prestamo,
    ):
        """Presta un libro a un usuario."""
        if dias_prestamo <= 0:
            return False, "Los dias de prestamo deben ser mayor a 0."

        if not id_usuario in self.usuarios:
            return False, f"Usuario con ID: '{id_usuario}' no encontrado."

        libro = self.libros.get(id_libro)

        if not libro:
            return False, f"Libro con ID: '{id_libro} no encontrado."

        if not libro.disponible:
            return False, f"El libro '{libro.titulo}' no está disponible."

        if len(self.ver_prestamos_usuarios(id_usuario)) >= 3:
            return False, f"Error: El usuario ya alcanzó su límite de prestamos."

        nuevo_prestamo = Prestamo(id_libro, id_usuario, dias_prestamo)
        libro.disponible = False
        self.prestamos.append(nuevo_prestamo)

        ok, mensaje = self.guardar_prestamos_json(archivo="prestamos.json")
        if not ok:
            return False, mensaje

        ok, mensaje = self.guardar_libros_json(archivo="libros.json")
        if not ok:
            return False, mensaje

        return True, f"El libro '{libro.titulo}' se prestó correctamente."

    def devolver_libro(self, id_libro):
        """Devuelve un libro prestado al sistema de biblioteca."""

        libro = self.libros.get(id_libro)

        if not libro:
            return False, f"No se encontró un libro con este ID: '{id_libro}'"

        prestamo = None
        for p in self.prestamos:
            if p.id_libro == id_libro and not p.devuelto:
                prestamo = p
                break

        if not prestamo:
            return (
                False,
                f"No se encontró ningún prestamo activo del libro con ID: {id_libro}",
            )

        if prestamo.devuelto:
            return False, f"Error. El libro con ID: '{id_libro}' ya se había devuelto."

        if prestamo.esta_atrasado() and not prestamo.multa_pagada:

                multa = self.calcular_multa(prestamo)
                return False, f"No se puede devolver. Multa pendiente por pagar: ${multa}"

        prestamo.devuelto = True
        libro.disponible = True

        ok, mensaje = self.guardar_prestamos_json(archivo="prestamos.json")
        if not ok:
            return False, mensaje

        ok, mensaje = self.guardar_libros_json(archivo="libros.json")
        if not ok:
            return False, mensaje

        return True, "Libro devuelto exitósamente."

    def calcular_multa(self, prestamo):
        """Calcula la multa por atraso de un préstamo."""
        return prestamo.calcular_dias_atraso() * self.multa_dias_atraso

    def pagar_multa(self, id_libro, monto):
        """Permite pagar la multa de un préstamo atrasado."""

        if monto <= 0:
            return False, "El monto debe ser mayor a 0."

        prestamo = None
        for p in self.prestamos:
            if p.id_libro == id_libro:
                prestamo = p
                break

        if not prestamo:
            return False, "El prestamo no existe."

        if prestamo.devuelto:
            return False, "El prestamo no está activo."

        if not prestamo.esta_atrasado():
            return False, "El prestamo no está atrasado. No hay multa por pagar."

        multa = self.calcular_multa(prestamo)

        if not monto >= multa:
            return (
                False,
                f"El monto a pagar (${monto}) no cubre el total de la multa (${multa}).",
            )

        prestamo.multa_pagada = True
        ok, mensaje = self.guardar_prestamos_json(archivo="prestamos.json")
        if not ok:
            return False, mensaje
        return True, f"Multa pagada con éxito."

    def buscar_libro_autor(self, autor):
        """Busca libros por autor."""

        autor_norm = normalizar_texto(autor)
        return [
            libro for libro in self.libros.values() if libro._autor_norm == autor_norm
        ]

    def buscar_libro_titulo(self, titulo):
        """Busca libros por título."""

        titulo_norm = normalizar_texto(titulo)
        return [
            libro for libro in self.libros.values() if libro._titulo_norm == titulo_norm
        ]

    def ver_prestamos_usuarios(self, id_usuario=None):
        """Devuelve los préstamos activos de un usuario específico o de todos los usuarios si no se especifica."""

        if id_usuario is None:
            libros_prestados = [p for p in self.prestamos if not p.devuelto]

        else:
            libros_prestados = [
                p
                for p in self.prestamos
                if p.id_usuario == id_usuario and not p.devuelto
            ]
        return libros_prestados

    def obtener_detalle_prestamo(self, prestamo):
        """Obtiene los detalles de un préstamo específico."""

        libro = self.libros.get(prestamo.id_libro)
        usuario = self.usuarios.get(prestamo.id_usuario)

        return {
            "nombre_usuario": usuario.nombre if usuario else "Desconocido",
            "titulo_libro": libro.titulo if libro else "Desconocido",
            "fecha_limite": prestamo.fecha_limite.strftime("%Y-%m-%d"),
            "esta_atrasado": prestamo.esta_atrasado(),
            "dias_atraso": prestamo.calcular_dias_atraso(),
            "multa": (self.calcular_multa(prestamo) if prestamo.esta_atrasado() else 0),
        }

    def ver_prestamos_detallados(self, id_usuario=None):
        """Devuelve los préstamos activos con detalles."""
        prestamos = self.ver_prestamos_usuarios(id_usuario)

        return [self.obtener_detalle_prestamo(p) for p in prestamos]

    def ver_prestamos_agrupados_por_usuario(self):
        """Devuelve los préstamos activos agrupados por usuario."""

        resultado = {}

        for prestamo in self.prestamos:
            if not prestamo.devuelto:
                usuario = self.usuarios.get(prestamo.id_usuario)
                nombre = usuario.nombre if usuario else "Desconocido"

                if nombre not in resultado:
                    resultado[nombre] = []

                resultado[nombre].append(self.obtener_detalle_prestamo(prestamo))

        return resultado

    def ver_libros_detallados(self):
        """Devuelve los libros registrados con detalles."""
        return [libro.to_dict() for libro in self.libros.values()]

    def ver_usuarios_detallados(self):
        """Devuelve los usuarios registrados con detalles."""
        return [usuario.to_dict() for usuario in self.usuarios.values()]

    def guardar_prestamos_json(self, archivo):
        """Guarda los préstamos en un archivo JSON."""
        try:
            with open(archivo, "w", encoding="utf-8") as file:
                json.dump(
                    [prestamo.to_dict() for prestamo in self.prestamos],
                    file,
                    indent=4,
                    ensure_ascii=False,
                )
                return True, "Prestamos guardados correctamente en JSON."

        except Exception as e:
            return False, f"Error. Hubo un problema durante la escritura: {e}"

    def guardar_libros_json(self, archivo):
        """Guarda los libros en un archivo JSON."""

        libros_dict = {}

        for libro_id, libro in self.libros.items():
            libros_dict[libro_id] = libro.to_dict()

        try:
            with open(archivo, "w", encoding="utf-8") as file:
                json.dump(libros_dict, file, indent=4, ensure_ascii=False)
                return True, "Libros guardados correctamente en JSON."

        except Exception as e:
            return False, f"Error. Hubo un problema durante la escritura: {e}"

    def guardar_usuarios_json(self, archivo):
        """Guarda los usuarios en un archivo JSON."""

        usuarios_dict = {}

        for usuario_id, usuario in self.usuarios.items():
            usuarios_dict[usuario_id] = usuario.to_dict()

        try:
            with open(archivo, "w") as file:
                json.dump(usuarios_dict, file, indent=4)
                return True, "Libros guardados correctamente en JSON."

        except Exception as e:
            return False, f"Error. Hubo un problema durante la escritura: {e}"

    def cargar_libros_json(self, archivo):
        """Carga los libros desde un archivo JSON."""

        try:
            with open(archivo, "r", encoding="utf-8") as file:
                data_dict = json.load(file)

                for id_libro, datos in data_dict.items():
                    libro = Libro(datos["id_libro"], datos["titulo"], datos["autor"])
                    libro.disponible = datos["disponible"]
                    self.libros[id_libro] = libro

                return True, "Libros cargados correctamente."

        except FileNotFoundError:
            return True, "Archivo no encontrado. Iniciando con datos vacíos."
        except Exception as e:
            return False, f"Error al cargar: {e}"

    def cargar_prestamos_json(self, archivo):
        """Carga los préstamos desde un archivo JSON."""

        try:
            with open(archivo, "r", encoding="utf-8") as file:
                data_dict = json.load(file)

                for data in data_dict:
                    prestamo = Prestamo(
                        id_libro=data["id_libro"],
                        id_usuario=data["id_usuario"],
                        fecha_prestamo=datetime.fromisoformat(data["fecha_prestamo"]),
                        fecha_limite=datetime.fromisoformat(data["fecha_limite"]),
                        devuelto=data["devuelto"],
                        multa_pagada=data["multa_pagada"],
                    )
                    self.prestamos.append(prestamo)

                return True, "Prestamos cargados correctamente."

        except FileNotFoundError:
            return True, "Archivo no encontrado. Iniciando con datos vacíos."
        except Exception as e:
            return False, f"Error al cargar: {e}"

    def cargar_usuarios_json(self, archivo):
        """Carga los usuarios desde un archivo JSON."""

        try:
            with open(archivo, "r", encoding="utf-8") as file:

                data_dict = json.load(file)

                for id_usuario, data in data_dict.items():
                    usuario = Usuario(data["id_usuario"], data["nombre"])
                    self.usuarios[id_usuario] = usuario

                return True, "Usuarios cargados correctamente."

        except FileNotFoundError:
            return True, "Archivo no encontrado. Iniciando con datos vacíos."
        except Exception as e:
            return False, f"Error al cargar: {e}"


# =================
# FUNCIONES UTILES
# =================
def normalizar_texto(texto):
    """Normaliza un texto para búsquedas insensibles a mayúsculas y acentos."""

    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto


def pedir_campo(campo):
    """Solicita un campo al usuario y valida que no esté vacío."""

    while True:
        valor = input(f"{campo}: ")
        if valor:
            return valor
        else:
            print(f"\n❌ El campo {campo.lower()} no puede estar vacío.\n")


def obtener_siguiente_id(diccionario, prefijo):
    """Genera el siguiente ID basado en el diccionario existente y el prefijo dado."""

    if not diccionario:
        return f"{prefijo}-1"

    numeros = []

    for id_actual in diccionario.keys():
        try:
            numero = int(id_actual.split("-")[1])
            numeros.append(numero)
        except (IndexError, ValueError):
            continue

    siguiente_numero = max(numeros) + 1 if numeros else 1
    return f"{prefijo}-{siguiente_numero}"


def crear_cabecera_menu(titulo):
    """Crea una cabecera de menú con el título dado."""
    
    limpiar_terminal()
    print(SEP)
    print(titulo.upper().center(50))
    print(SEP + "\n")


def limpiar_terminal():
    """Limpia la terminal según el sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")


# ================
# FUNCIONES DE UI
# ================
def mostrar_menu():
    print(SEP)
    print("SISTEMA DE BIBLIOTECA".center(50))
    print(SEP)
    print("\n 1. Agregar libro")
    print(" 2. Agregar usuario")
    print(" 3. Prestar libro")
    print(" 4. Devolver libro")
    print(" 5. Pagar multa")
    print(" 6. Buscar libro por título")
    print(" 7. Buscar libro por autor")
    print(" 8. Ver préstamos activos")
    print(" 9. Ver préstamos por usuarios")
    print(" 10. Ver libros registrados")
    print(" 11. Ver usuarios registrados")
    print(" 0. Salir\n")
    print(SEP)


def menu_agregar_libro(biblioteca):

    crear_cabecera_menu("AGREGAR LIBRO")

    titulo = pedir_campo("Titulo").strip()
    autor = pedir_campo("Autor").strip()

    nuevo_libro = Libro("", titulo, autor)
    ok, mensaje = biblioteca.agregar_libro(nuevo_libro)
    print("✅" if ok else "❌", mensaje)


def menu_agregar_usuario(biblioteca):
    crear_cabecera_menu("AGREGAR USUARIO")

    nombre = pedir_campo("Nombre").strip()

    nuevo_usuario = Usuario("", nombre)
    ok, mensaje = biblioteca.agregar_usuario(nuevo_usuario)
    print("✅" if ok else "❌", mensaje)


def menu_prestar_libro(biblioteca):
    crear_cabecera_menu("PRESTAR LIBRO")

    id_usuario = pedir_campo("ID del usuario").upper().strip()
    id_libro = pedir_campo("ID del libro").upper().strip()

    while True:
        try:
            dias_prestamo = int(input("Días de prestamo: "))
            break
        except ValueError:
            print("\n❌ Error: Ingrese un valor válido.\n")

    ok, mensaje = biblioteca.prestar_libro(id_usuario, id_libro, dias_prestamo)
    print("✅" if ok else "❌", mensaje)


def menu_devolver_libro(biblioteca):
    crear_cabecera_menu("DEVOLVER LIBRO")

    id_libro = pedir_campo("ID del libro").strip().upper()
    ok, mensaje = biblioteca.devolver_libro(id_libro)
    print("✅" if ok else "❌", mensaje)


def menu_pagar_multa(biblioteca):
    crear_cabecera_menu("PAGAR MULTA")

    id_libro = pedir_campo("Ingrese el ID del libro").strip().upper()

    while True:
        try:
            monto = float(pedir_campo("Ingrese el monto a pagar"))
            break

        except ValueError:
            print("\n❌ Error: Ingrese un valor válido.\n")

    ok, mensaje = biblioteca.pagar_multa(id_libro, monto)
    print("✅" if ok else "❌", mensaje)


def menu_buscar_libro_titulo(biblioteca):
    crear_cabecera_menu("BUSCAR LIBROS POR TITULO")

    titulo = pedir_campo("Titulo")
    libros = biblioteca.buscar_libro_titulo(titulo)
    if not libros:
        print(f"\n❌ No se encontraron libros con el titulo '{titulo}'.")
        return
    print("\n" + SEP)
    print(f"LIBROS ENCONTRADOS: {len(libros)}")
    print(SEP)
    for i, l in enumerate(libros, 1):
        estado = "Disponible ✅" if l.disponible else "Prestado ❌"
        print(f"{i}. {l.titulo} - ID: {l.id_libro} - Estado: {estado}")
    print(SEP)


def menu_buscar_libro_autor(biblioteca):
    crear_cabecera_menu("BUSCAR LIBROS POR AUTOR")

    autor = pedir_campo("Autor")
    libros = biblioteca.buscar_libro_autor(autor)

    if not libros:
        print(f"\n❌ No se encontraron libros del autor '{autor}'.")
        return

    print("\n" + SEP)
    print(f"LIBROS ENCONTRADOS: {len(libros)}")
    print(SEP)

    for i, l in enumerate(libros, 1):
        estado = "Disponible ✅" if l.disponible else "Prestado ❌"
        print(f"{i}. {l.titulo} - ID: {l.id_libro} - Estado: {estado}")
    print(SEP)


def menu_ver_prestamos_activos(biblioteca):
    crear_cabecera_menu("PRESTAMOS ACTIVOS")

    prestamos = biblioteca.ver_prestamos_detallados()

    if not prestamos:
        print("\n❌ No hay préstamos activos.")
        return

    for i, p in enumerate(prestamos, 1):
        print(f"Préstamo #{i}:")
        print(f"  Usuario         : {p["nombre_usuario"]}")
        print(f"  Libro           : {p["titulo_libro"]}")
        print(f"  Fecha límite    : {p["fecha_limite"]}")
        print(f"  Atrasado        : {'Si' if p["esta_atrasado"] else 'No'}")
        print(f"  Días de atraso  : {p["dias_atraso"]}")
        print(f"  Multa           : {p["multa"]}")
        print(SEP)


def menu_ver_prestamos_agrupados_usuario(biblioteca):
    crear_cabecera_menu("PRESTAMOS AGRUPADOS POR USUARIO: ")
    prestamos = biblioteca.ver_prestamos_agrupados_por_usuario()
    if not prestamos:
        print("\n❌ No hay préstamos activos.")
        return

    for user, p in prestamos.items():
        print(f"{user}: \n")
        for data in p:
            print("  " + "-" * 40 + "\n")
            print(f"  Libro           : {data["titulo_libro"]}")
            print(f"  Fecha límite    : {data["fecha_limite"]}")
            print(f"  Atrasado        : {'Si' if data["esta_atrasado"] else 'No'}")
            print(f"  Días de atraso  : {data["dias_atraso"]}")
            print(f"  Multa           : {data["multa"]}")
            print()

        print(SEP + "\n")


def menu_ver_libros_registrados(biblioteca):
    crear_cabecera_menu("LIBROS REGISTRADOS")
    libros = biblioteca.ver_libros_detallados()

    if not libros:
        print("\n❌ No hay libros registrados")
        return

    print(f"Cantidad de libros: {len(libros)}")

    for l in libros:
        print(SEP)
        print(f"  ID             : {l["id_libro"]}")
        print(f"  Título         : {l["titulo"]}")
        print(f"  Autor          : {l["autor"]}")
        print(f"  Disponible     : {"Si ✅" if l["disponible"] else "No ❌"}")
    print(SEP)

def menu_ver_usuarios_registrados(biblioteca):
    crear_cabecera_menu("LIBROS REGISTRADOS")
    usuarios = biblioteca.ver_usuarios_detallados()

    if not usuarios:
        print("\n❌ No hay usuarios registrados")
        return

    print(f"Cantidad de usuarios: {len(usuarios)}")

    for u in usuarios:
        print(SEP)
        print(f"  ID             : {u["id_usuario"]}")
        print(f"  Nombre         : {u["nombre"]}")
    print(SEP)
# =================
# FUNCIÓN PRINCIPAL
# =================


def main():
    biblioteca = Bibiblioteca()

    # Cargar datos desde archivos JSON
    biblioteca.cargar_libros_json("libros.json")
    biblioteca.cargar_usuarios_json("usuarios.json")
    biblioteca.cargar_prestamos_json("prestamos.json")

    while True:
        limpiar_terminal()
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_agregar_libro(biblioteca)

        elif opcion == "2":
            menu_agregar_usuario(biblioteca)

        elif opcion == "3":
            menu_prestar_libro(biblioteca)

        elif opcion == "4":
            menu_devolver_libro(biblioteca)

        elif opcion == "5":
            menu_pagar_multa(biblioteca)

        elif opcion == "6":
            menu_buscar_libro_titulo(biblioteca)

        elif opcion == "7":
            menu_buscar_libro_autor(biblioteca)

        elif opcion == "8":
            menu_ver_prestamos_activos(biblioteca)

        elif opcion == "9":
            menu_ver_prestamos_agrupados_usuario(biblioteca)

        elif opcion == "10":
            menu_ver_libros_registrados(biblioteca)

        elif opcion == "11":
            menu_ver_usuarios_registrados(biblioteca)
        
        elif opcion == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()