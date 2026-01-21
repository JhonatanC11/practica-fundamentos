# ejercicio45.py - Empleados con herencia
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_salario(self):
        return self.salario_base + self.bono


class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, tarifa_hora, horas_trabajadas):

        super().__init__(nombre, 0)
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_hora
    