from Vacante import *

class Oferta:
    def __init__(self,id,ocupacion,numpostulados,fechapublicacion,fechacierre):
        self.__id=id
        self.__ocupacion=ocupacion
        self.__vacantes=[]
        self.__numpostulados=numpostulados
        self.__fechapublicacion=fechapublicacion
        self.__fechacierre=fechacierre
    
    def getid(self):
        return self.__id
    
    def setid(self,id):
        self.__id=id

    def get_ocupacion(self):
        return self.__ocupacion
    
    def set_ocupacion(self,ocupacion):
        self.__ocupacion=ocupacion
    
    def getnumpostulados(self):
        return self.__numpostulados
    
    def setnumpostulados(self,numpostulados):
        self.__numpostulados=numpostulados
    
    def getfechapublicacion(self):
        return self.__fechapublicacion
    
    def setfechapublicacion(self,fechapublicacion):
        self.__fechapublicacion=fechapublicacion
    
    def getfechacierre(self):
        return self.__fechacierre
    
    def setfechacierre(self,fechacierre):
        self.__fechacierre=fechacierre
    
    def agregarvacante(self,vacante):
        self.__vacantes.append(vacante)
    
    def getvacantes(self):
        for v in self.__vacantes:
            print(f"Ocupacion: {v.get_ocupacion}, Numero de vacantes: {v.get_num_vacantes}, Salario: {v.get_salario}, Experiencia: {v.get_experiencia}")

    def __str__(self):
        return self.id