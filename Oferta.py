from Vacante import *

class Oferta:
    def __init__(self,id,numpostulados,fechapublicacion,fechacierre):
        self.__id=id
        self.__vacante=[]
        self.__numpostulados=numpostulados
        self.__fechapublicacion=fechapublicacion
        self.__fechacierre=fechacierre
    
    def getid(self):
        return self.__id
    
    def setid(self,id):
        self.__id=id
    
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
        self.__vacante.append(vacante)
    
    def getvacantes(self):
        print ("vacantes: ",self)
        for v in self.__vacante:
            print(f"Ocupacion: {v.ocupacion}, Numero de vacantes: {v.numvacantes}, Salario: {v.salario}, Experiencia: {v.experiencia}")

    def __str__(self):
        return self.id