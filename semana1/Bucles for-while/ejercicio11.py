# ejercicio11.py - Gestión de lista
# Crea lista vacía
# Menu: 1.Agregar, 2.Mostrar, 3.Eliminar, 4.Salir
import time
tareas = ["Hacer algo", "Hacer nada", "Morir"]
while True:
    try:
        print("\n" + "=" * 10 + " GESTION DE LISTA " + "=" * 10)
        print(" 1. Agregar\n 2. Mostrar\n 3. Eliminar\n 4. Salir\n")

        opcion = int(input("Ingrese la opcion que desea realizar: "))

        if opcion == 1:
            while True:
                print("Agregar tarea: ")
                nuevo_ele = input("Ingrese la tarea a agregar: ")
                if nuevo_ele:
                    tareas.append(nuevo_ele)
                    print("Tarea agregada correctamente.")
                else:
                    print("No se permite agregar tareas vacías")

                while True:
                    agg_nuevo = input("\n¿Desea agregar otra tarea?: S/N").strip().lower()
                    if agg_nuevo in ['s', 'n']:
                        break
                    else:
                        print("Error. Ingrese S para si, o N para NO.")
                if agg_nuevo == "n":
                    print("Volviendo al menú principal...")
                    break 
            time.sleep(1)

        elif opcion == 2: 
            while True:
                if len(tareas) == 0:
                    print("No hay tareas en tu lista.")
                    time.sleep(1)
                else:
                    print("Lista de tareas")
                    for i, j in enumerate(tareas, start=1):
                        print(f" {i}. {j}")
                    time.sleep(1)
                volver_menu = input("\n¿Desea volver al menú principal? S/N: ").strip().lower()
                if volver_menu in ['s', 'n']:
                    break
                else:
                    print("Error. Ingrese S para si o N para no.")
        elif opcion == 3:
            while True:
                if len(tareas) == 0:
                    print("No hay tareas en tu lista.")
                    time.sleep(1)
                    break
                else:
                    print("Lista de tareas")
                    for i, j in enumerate(tareas, start=1):
                        print(f" {i}. {j}")
                    
                    while True:
                        try:
                            dele_tarea = int(input("Digite el numero de la tarea a eliminar: "))
                            if 1 <= dele_tarea <= len(tareas):
                                tareas.pop(dele_tarea - 1)
                                print("Tarea eliminada correctamente.")
                                break
                            else:
                                print("Indice invalido")
                        except ValueError:
                            print("Error. Ingrese solo el numero de la tarea a eliminar.")
                    while True:
                        elim_tarea = input("Desea eliminar otra tarea? S/N: ").strip().lower()
                        if elim_tarea in ['s', 'n']:
                            break
                        else:
                            print("Error. Ingrese S para si o N para no.")
                    if elim_tarea == "n":
                        print("Volviendo al menu principal...")
                        break
            time.sleep(1)
    
        elif opcion == 4:
            print("Saliendo del programa....")
            time.sleep(1)
            break
        
        else:
            print("Fuera del rango. Ingrese un valor entre 1 y 4.")
            time.sleep(1)
    except ValueError:
        print("Error. Ingrese solo valores enteros.")
        time.sleep(1)
