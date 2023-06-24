from Usuario import *
class Empresa(Usuario):
    def __init__(self, telefono, correo, direccion,nit):
        super().__init__(telefono, correo, direccion)
        self.__nit=nit
        self.__ofertas=[]
