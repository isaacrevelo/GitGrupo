class Educacion:
    def __init__(self, nivel_educativo, institucion_educativa, campo_estudio, duracion):
        self.__nivel_educativo = nivel_educativo
        self.__institucion_educativa = institucion_educativa
        self.__campoestudio = campo_estudio
        self.__duracion=duracion

    def getNivelEducativo(self):
        return self.__nivel_educativo

    def setNivelEducativo(self, nivel_educativo):
        self.__nivel_educativo = nivel_educativo

    def getInstitucionEducativa(self):
        return self.__institucion_educativa

    def setInstitucionEducativa(self, institucion_educativa):
        self.__institucion_educativa = institucion_educativa

    def getCampoEstudio(self):
        return self.__campoestudio

    def setCampoEstudio(self, campo_estudio):
        self.__campoestudio = campo_estudio

    def getduracion(self):
        self.__duracion
    
    def setduracion(self,duracion):
        self.__duracion=duracion