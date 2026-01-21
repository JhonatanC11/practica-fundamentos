# ejercicio44.py - Sistema de vehículos
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca 
        self.modelo = modelo
        self.anio = anio 
    
    def arrancar(self):
        pass

class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, cilindrada):
        super().__init__(marca, modelo, anio)
        self.cilindrada = cilindrada

