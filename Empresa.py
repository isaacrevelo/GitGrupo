from Usuario import *
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

    def agregaroferta(self, oferta):
        self.__ofertas.append(oferta)