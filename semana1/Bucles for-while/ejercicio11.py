# ejercicio11.py - Gestión de lista
# Crea lista vacía
# Menu: 1.Agregar, 2.Mostrar, 3.Eliminar, 4.Salir
import time
tareas = ["Hacer algo", "Hacer nada", "Morir"]
while True:
    print("\n","="*10, "GESTION DE LISTA", "="*10)
    print(" 1. Agregar\n 2. Mostrar\n 3. Eliminar\n 4. Salir\n")

    opcion = int(input("Ingrese la opcion que desea realizar: "))

    if opcion == 1:
        print("Agregar tarea: ")
        while True:
            nuevo_ele = input("Ingrese la tarea a agregar: ")
            if nuevo_ele:
                tareas.append(nuevo_ele)
                if nuevo_ele in tareas:
                    print("Tarea agregada correctamente")

                else:
                    print("Error agregando la tarea")

                agg_nuevo = input("\n¿Desea agregar otra tarea?: S/N").lower()
                if agg_nuevo == "n":
                    break
                elif agg_nuevo == "s":
                    pass
                else:
                    print("Error, ingrese S para si o N para no.")
 
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
            menu = input("\n¿Desea volver al menú principal? S/N: ").lower()
            if menu == "s":
                break
            elif menu == "n":
                pass
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
                dele_tarea = int(input("Digite el numero de la tarea a eliminar: "))
                for i in range(len(tareas)):
                    if dele_tarea - 1 == i:
                        tareas.remove(tareas[i])
                        print(f"Tarea eliminada correctamente")
                        time.sleep(1)
                elim_tarea = input("Desea eliminar otra tarea? S/N: ").lower()
                if elim_tarea == "s":
                    pass


