# ejercicio24.py - Registro de estudiantes
# Cada estudiante tiene: nombre, edad, notas (lista)
# Funciones: agregar, mostrar, calcular promedio de un estudiante
import os

estudiantes = {} # Diccionario principal para almacenar los estudiantes
configuracion = {'numero_notas' : 5, 'nota_maxima' : 5.0} # Configuración por defecto

#FUNCIONES PRINCIPALES: 

def agregar_estudiante(estudiantes, nombre, edad, notas):
    """Agrega un nuevo estudiante al diccionario"""

    nombre = nombre.strip().lower()
    if nombre in estudiantes:
        return f"El estudiante '{nombre}' ya existe."
    promedio = calcular_promedio_estudiante(notas, configuracion)
    estudiantes[nombre] = {'edad' : edad, 'notas' : notas, 'promedio' : promedio}
    return f"El estudiante '{nombre}' se agregó correctamente."

def eliminar_estudiante(nombre, estudiantes):
    """Elimina un estudiante del diccionario"""

    nombre = nombre.strip().lower()
    if nombre not in estudiantes:
        return (False, f"El estudiante {nombre} no existe.")
    del estudiantes[nombre]
    return (True, "Estudiante eliminado correctamente.")

def editar_nombre_estudiante (nombre_actual, nombre_nuevo, estudiantes):
    """Edita el nombre de un estudiante en el diccionario"""

    nombre_actual = nombre_actual.strip().lower()
    nombre_nuevo = nombre_nuevo.strip().lower()
    if nombre_actual not in estudiantes:
        return (False, f"El estudiante {nombre_actual} no existe.")
    if nombre_nuevo in estudiantes:
        return(False, f"El nombre {nombre_nuevo} ya existe.")
    
    estudiantes[nombre_nuevo] = estudiantes[nombre_actual]
    del estudiantes[nombre_actual]
    return (True, "Nombre actualizado correctamente.")

def editar_notas_estudiante(nombre, nuevas_notas, estudiantes):
    """Edita las notas de un estudiante en el diccionario"""
    nombre = nombre.strip().lower()
    if nombre not in estudiantes:
        return (False, f"El estudiante {nombre} no existe.")
    estudiantes[nombre]["notas"] = nuevas_notas
    promedio = calcular_promedio_estudiante(nuevas_notas, configuracion)
    estudiantes[nombre]["promedio"] = promedio
    return (True, f"Notas actualizadas correctamente.")

def buscar_estudiante(nombre, estudiantes):
    """Busca un estudiante en el diccionario"""
    nombre = nombre.strip().lower()
    if nombre not in estudiantes:
        return(False, f"El estudiante {nombre} no existe.")
    return (True, estudiantes[nombre])
    
def mostrar_estudiantes(estudiantes):
    """Muestra todos los estudiantes en el diccionario"""

    if not estudiantes:
        return (False, "No hay estudiantes registrados")
    return (True, estudiantes)

def calcular_promedio_estudiante(notas, configuracion):
    """Calcula el promedio de un estudiante"""
    if not notas:
        return 0.0
    promedio = sum(notas) / len(notas)
    return promedio

def calcular_promedio_total(estudiantes):
    """Calcula el promedio total del curso"""

    if estudiantes:
        promedios_curso = [datos['promedio'] for datos in estudiantes.values()]
        num_estudiantes = len(promedios_curso)
        promedio_total = sum(promedios_curso) / num_estudiantes
        return promedio_total

#FUNCIONES DE UTILIDAD:

def validar_nombre(texto_input):
    """Valida que el nombre no esté vacío"""

    while True:
        nombre = input(texto_input).strip()
        if nombre:
            return nombre
        print("Error: No puede estar vacío")

def validar_edad(edad_input):
    """Valida que la edad esté en un rango válido"""

    while True:
        try:
            edad = int(input(edad_input))
            if 0 < edad < 100:
                return edad
            else:
                print("Error: Ingrese una edad válida.")
        except ValueError:
            print("Error: Ingrese solo números.")

def validar_nota(nota_input, configuracion):
    """Valida que la nota esté en el rango correcto"""

    nota_maxima = configuracion['nota_maxima']
    while True:
        try:
            nota = float(input(nota_input))
            if 0 <= nota <= nota_maxima:
                return nota
            else:
                if nota > nota_maxima:
                    print(f"Error. La maxima nota posible es de {nota_maxima}.")
                else:
                    print("Error. Ingrese una nota válida.")
        except ValueError:
            print("Error. Ingrese solo números")

def limpiar_terminal():
    """Limpia la terminal según el sistema operativo"""
    os.system("cls" if os.name == "nt" else "clear")


def solicitar_confirmacion(prompt):
    """Solicita una confirmación S/N al usuario"""

    while True:
        respuesta = input(prompt).upper().strip()
        if respuesta in ['S', 'N']:
            return respuesta == 'S'
        print("Error. Ingrese solo S o N.")
            
def ejecutar_repeticion(funcion, estudiantes):

    """Ejecuta una función y pregunta si se desea repetirla"""
    while True:
        if funcion == menu_agregar:
            funcion(estudiantes, configuracion)
        else:
            funcion(estudiantes)
        if not solicitar_confirmacion("¿Desea repetir esta operación? S/N: "):
            break

def validar_opcion(opcion_input, minimo, maximo):
    """Valida que la opción esté dentro de un rango específico"""

    while True:
        try:
            opcion = int(input(opcion_input))
            if minimo <= opcion <= maximo:
                return opcion
            else:
                print(f"Error: Fuera del rango ({minimo} - {maximo})")
        except ValueError:
            print("Error: Ingrese solo números.")

def configurar_valores(configuracion, nuevo_num_notas, nueva_nota_max):
    """Configura los valores de número de notas y nota máxima"""

    configuracion['numero_notas'] = nuevo_num_notas
    configuracion['nota_maxima'] = nueva_nota_max
    return configuracion 

#FUNCIONES DEL MENU:

def menu_agregar(estudiantes, configuracion):
    """Menú para agregar un nuevo estudiante"""
    limpiar_terminal()
    numero_notas = configuracion['numero_notas']
    print("=" * 10 + " AGREGAR ESTUDIANTE " + "=" * 10)

    nombre = validar_nombre("Ingrese el nombre: ")
    edad = validar_edad("Ingrese la edad: ")
    notas = []

    for nota in range (numero_notas):
        notas.append(validar_nota(f"Ingrese la {nota+1} nota: ", configuracion))
    
    mensaje = agregar_estudiante(estudiantes, nombre, edad, notas)
    print(mensaje)

def menu_editar(estudiantes):
    """Menú para editar un estudiante existente"""

    limpiar_terminal()
    numero_notas = configuracion['numero_notas']
    print("=" * 10 + " EDITAR ESTUDIANTE " + "=" * 10)
    ok, respuesta = mostrar_estudiantes(estudiantes)

    if not ok:
        print(respuesta)
        return 
       
    for llave, valor in respuesta.items():
        print(f" > {llave}: ")
        for i, j in valor.items():
            print(f"\t- {i}: {j}")
        print()
    
    intentos = 5
    while intentos > 0:

        nombre = validar_nombre("Ingresa el nombre del estudiante a editar: ")
        existe, mensaje = buscar_estudiante(nombre, estudiantes)

        if existe:
            print(f"\n> {nombre}:")
            for i, j in mensaje.items():
                print(f"\t- {i}: {j}")
            print()
            print("1. Editar nombre.\t2. Editar notas.\n")
            opcion = validar_opcion("Ingresa una opción: ", 1, 2)
            if opcion == 1:
                nombre_nuevo = validar_nombre("Ingresa el nuevo nombre: ")
                estado, mensaje = editar_nombre_estudiante(nombre, nombre_nuevo, estudiantes)
                if not estado:
                    print(mensaje)
                print(mensaje)  

            if opcion == 2:
                nuevas_notas = []
                for nota in range (numero_notas):
                    nuevas_notas.append(validar_nota(f"Ingrese la nueva nota {nota+1}: ", configuracion))
                estado, mensaje = editar_notas_estudiante(nombre, nuevas_notas, estudiantes)
                if not estado:
                    print(mensaje)
                print(mensaje)
            break

        else:
            print(mensaje)
            intentos -= 1

def menu_mostrar(estudiantes):
    """Menú para mostrar todos los estudiantes"""

    limpiar_terminal()
    print("=" * 10 + " LISTA DE ESTUDIANTES " + "=" * 10)
    existe, mensaje = mostrar_estudiantes(estudiantes)
    if not existe:
        print(mensaje)
    for nombre, valor in estudiantes.items():
        print(f" > {nombre}: ")
        for i, j in valor.items():
            print(f"\t- {i}: {j}")
        print()

def menu_eliminar(estudiantes):
    """Menú para eliminar un estudiante existente"""

    limpiar_terminal()
    print("=" * 10 + " ELIMINAR ESTUDIANTE " + "=" * 10)
    ok, respuesta = mostrar_estudiantes(estudiantes)
    
    if not ok:
        print(respuesta)
        return
    
    for llave, valor in respuesta.items():
        print(f" > {llave}: ")
        for i, j in valor.items():
            print(f"\t- {i}: {j}")
        print()
    intentos = 5
    while intentos > 0:
        nombre = validar_nombre("Ingresa el nombre del estudiante a eliminar: ")
        existe, mensaje = eliminar_estudiante(nombre, estudiantes)
        if existe:
           print(mensaje)
           break
        else:
            print(mensaje) 
            intentos -= 1

def menu_configuracion(configuracion):
    """Menú para configurar los valores de número de notas y nota máxima"""
    limpiar_terminal()
    print("=" * 10 + " CONFIGURACION " + "=" * 10 + "\n")
    print(f" > Nota maxima: {configuracion['nota_maxima']}")
    print(f" > Numero de notas permitidas: {configuracion['numero_notas']}\n")
    opcion = solicitar_confirmacion("¿Desea actualizar estos valores? S/N: ")
    if opcion:
        nuevo_n_notas = int(input("Ingrese el nuevo número de notas permitido: "))
        nueva_nota_maxima = float(input("Ingrese la nueva nota máxima permitída: "))

        nueva_config = configurar_valores(configuracion, nuevo_n_notas, nueva_nota_maxima)
        print("Valores actualizados correctamente:\n")
        for i, j in nueva_config.items():
            print(f" > {i}: {j}")

def menu_promedio_curso(estudiantes):
    """Menú para calcular el promedio total del curso"""
    limpiar_terminal()
    print("=" * 10 + " PROMEDIO TOTAL DEL CURSO " + "=" * 10 + "\n")
    promedio_total = calcular_promedio_total(estudiantes)
    if promedio_total is None:
        print("No hay estudiantes.")
        return
    promedios_curso = [datos['promedio'] for datos in estudiantes.values()]
    print(f"Promedios del curso: {promedios_curso}")
    print(f"Promedio total del curso: {promedio_total}")    

# MENU PRINCIPAL
def main():
    """Función principal que ejecuta el menú del programa"""

    while True:
        limpiar_terminal()
        print("=" * 10 + " REGISTRO DE ESTUDIANTES " + "=" * 10)
        print(" 1. Agregar estudiante\n 2. Mostrar estudiantes\n 3. Editar estudiante\n 4. Eliminar estudiante\n 5. Calcular promedio del curso\n 6. Configurar valores\n 7. Salir")
        opcion = validar_opcion("Ingresa una opcion (1-7): ", 1 , 7)

        if opcion == 1:
            ejecutar_repeticion(menu_agregar, estudiantes)
        
        elif opcion == 2:
            ejecutar_repeticion(menu_mostrar, estudiantes)
        
        elif opcion == 3:
            ejecutar_repeticion(menu_editar, estudiantes)
        
        elif opcion == 4: 
            ejecutar_repeticion(menu_eliminar, estudiantes)
        
        elif opcion == 5: 
            ejecutar_repeticion(menu_promedio_curso, estudiantes)

        elif opcion == 6:
            ejecutar_repeticion(menu_configuracion,configuracion)
        
        elif opcion == 7:
            print("Saliendo del programa...")
            break

# EJECUCION DEL PROGRAMA
if __name__ == "__main__":
    main()