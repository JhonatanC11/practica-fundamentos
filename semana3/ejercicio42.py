# ejercicio42.py - Gestor de tareas con archivo
import json
class Tarea:
    def __init__(self, descripcion, completada = False):
        self.descripcion = descripcion
        self.completada = completada
    
    def to_dict(self):
        """
        Retorna los parametros del objeto en un diccionario.
        """
        return {
            "descripcion": self.descripcion,
            "completada": self.completada
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["descripcion"], data["completada"])
class GestorTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, descripcion):
        """
        Agrega una tarea a la lista
        """
        self.tareas.append(Tarea(descripcion))
    
    def completar_tarea(self, indice):
        """
        Cambia el estado de una tarea a completada(true)
        """
        if indice < 0 or indice >= len(self.tareas):
            return False, "Indice inválido."
        
        tarea = self.tareas[indice]
        tarea.completada = True
        return True, "Tarea marcada cómo completada."
    
    def guardar_en_json(self, archivo):
        """
        Convierte la lista de tareas (Objetos de tipo Tarea) en dict() para despues volverlos JSON.
        """

        try:
            with open(archivo, "w") as f:
                json.dump([tarea.to_dict() for tarea in self.tareas], f, indent=4)
                return True, "Las tareas han sido guardadas en formato JSON."
        
        except FileNotFoundError:
            return False, "Archivo no encontrado"
        
        except Exception as e:
            return False, f"Error creando el archivo: {e}"

    def cargar_desde_json(self, archivo):
        """
        Leé un archivo JSON con una lista de tareas, si cumple con lo necesario 
        crea objetos de tipo Tarea por cada tarea y los guarda en la lista de tareas.
        """

        try:

            with open(archivo) as f:
                lista = json.load(f)
                
                if not lista:
                    return False, "No hay tareas registradas"
                
                for tarea in lista:

                    if "descripcion" not in tarea or "completada" not in tarea:
                        return False, "El archivo no cumple con el esquema necesario"
                
                self.tareas = []

                for data in lista:
                    self.tareas.append(Tarea.from_dict(data))

                return True, "Tareas cargadas correctamente."
            
        except FileNotFoundError:
            return False, "Archivo no encontrado"

        except Exception as e:
            return False, f"Error durante la lectura: {e}"    

#EJEMPLO DE USO:
gestor = GestorTareas()
gestor.agregar_tarea("Leer 10 minutos")
gestor.agregar_tarea("Hacer ejercicio")
gestor.completar_tarea(0)
gestor.guardar_en_json("tareas.json")
gestor.cargar_desde_json("tareas.json")
gestor.guardar_en_json("lista_tareas.json")