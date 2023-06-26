from Usuario import *
from Oferta import *
class Empresa(Usuario):
    def __init__(self, telefono, correo, direccion,nit):
        super().__init__(telefono, correo, direccion)
        self.__nit=nit
        self.__ofertas=[]

    def getnit(self):
        return self.__nit

    def setnit(self, nit):
        self.__nit = nit

    def getofertas(self):
        return self.__ofertas

    def agregaroferta(self, id,numpostulados,fechapublicacion,fechacierre):
        ofer=Oferta(id,numpostulados,fechapublicacion,fechacierre)
        self.__ofertas.append(ofer)
