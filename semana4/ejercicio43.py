# ejercicio43.py - Herencia básica
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        pass
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo")
    
    def presentar(self):
        print(f"Hola, soy {self.nombre}!")

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
    
    def hacer_sonido(self):
        print(f"Guau guau!. Soy tu {self.raza}")
    
class Gato(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
    def hacer_sonido(self):
        print(f"Miau!. Soy tu {self.raza}")

perro = Perro("Cristian", "25", "perrota")
perro.presentar()
perro.hacer_sonido()
perro.dormir()

gato = Gato("Aleja", "20", "gatita")
gato.presentar()
gato.hacer_sonido()
gato.dormir()