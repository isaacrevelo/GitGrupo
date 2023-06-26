class Cargo:
    def __init__(self,requisitos,duracion,tipocontrato,ubicacion,cupos):
        self.__requisitos=requisitos
        self.__duracion=duracion
        self.__tipocontrato=tipocontrato
        self.__ubicacion=ubicacion
        self.__cupos=cupos
    
    def getrequisitos(self):
        return self.__requisitos

    def setrequisitos(self, requisitos):
        self.__requisitos = requisitos

    def getduracion(self):
        return self.__duracion

    def setduracion(self, duracion):
        self.__duracion = duracion

    def gettipocontrato(self):
        return self.__tipocontrato

    def settipocontrato(self, tipocontrato):
        self.__tipocontrato = tipocontrato

    def getubicacion(self):
        return self.__ubicacion

    def setubicacion(self, ubicacion):
        self.__ubicacion = ubicacion

    def getcupos(self):
        return self.__cupos

    def setcupos(self, cupos):
        self.__cupos = cupos