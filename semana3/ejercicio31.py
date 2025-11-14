# ejercicio31.py - Clase Persona
# Crear 3 personas y probar métodos

class Persona():

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self, amigo):
        print(f"Hola {amigo.nombre}. Mi nombre es {self.nombre}.")
    
    def cumpleaños(self):
        print(f"Tengo {self.edad} años.")

persona_1 = Persona("Messi", 38)
persona_2 = Persona("Ronaldo", 40)
persona_3 = Persona("Neymar", 32)

persona_1.saludar(persona_2)
persona_1.cumpleaños()

persona_3.saludar(persona_1)
persona_3.saludar(persona_2)