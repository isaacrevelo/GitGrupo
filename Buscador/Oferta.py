from Ubicacion import *
from Cargo import *
from Departamento import *
class Oferta:
    def __init__(self,id,numpostulados,fechapublicacion,fechacierre):
        self.id=id
        self.numpostulados=numpostulados
        self.fechapublicacion=fechapublicacion
        self.fechacierre=fechacierre
    
    def getid(self):
        return self.id
    
    def setid(self,id):
        self.id=id
    
    def getnumpostulados(self):
        return self.numpostulados
    
    def setnumpostulados(self,numpostulados):
        self.numpostulados=numpostulados
    
    def getfechapublicacion(self):
        return self.fechapublicacion
    
    def setfechapublicacion(self,fechapublicacion):
        self.fechapublicacion=fechapublicacion
    
    def getfechacierre(self):
        return self.fechacierre
    
    def setfechacierre(self,fechacierre):
        self.fechacierre=fechacierre

oferta = Oferta(1, 45324567, "2023-06-26", "2023-07-10")
cargo = Cargo("Requisitos para el cargo", "6 meses", "Contrato temporal", 9)
departamento = Departamento("Departamentos de informática y programacion", "Tipo 1")
ubicacion = Localizacion("25", "754", "Cundinamarca", "Soacha")