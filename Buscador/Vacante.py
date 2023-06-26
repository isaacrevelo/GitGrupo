from Cargo import *

class vacantes:
    def __init__(self,ocupacion,numvacantes,salario,experiencia):
        self.__ocupacion=ocupacion
        self.__numvacantes=numvacantes
        self.__salario=salario
        self.__experiencia=experiencia
        self.__cargo=None
    
    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def get_ocupacion(self):
        return self.__ocupacion

    def set_ocupacion(self, ocupacion):
        self.__ocupacion = ocupacion

    def get_num_vacantes(self):
        return self.__numvacantes

    def set_num_vacantes(self, num_vacantes):
        self.__numvacantes = num_vacantes

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def get_experiencia(self):
        return self.__experiencia

    def set_experiencia(self, experiencia):
        self.__experiencia = experiencia