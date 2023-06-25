from Usuario import *

class Candidato(Usuario):
    def __init__(self, telefono, correo, direccion,
                 nombre,perfilprofesional,proyectosdestacados,
                 referenciaslaborales,libretamilitar,competencias,
                 experiencia,educacion,idioma):
        super().__init__(telefono, correo, direccion)
        self.__nombre=nombre
        self.__perfilprofesional=perfilprofesional
        self.__proyectosdestacados=proyectosdestacados
        self.__referenciaslaborales=referenciaslaborales
        self.__libretamilitar=libretamilitar
        self.__competencias=competencias
        self.__experiencia=experiencia
        self.__educacion=educacion
        self.__idioma=idioma

    def getnombre(self):
        return self.__nombre

    def setnombre(self, nombre):
        self.__nombre = nombre

    def getperfilprofesional(self):
        return self.__perfilprofesional

    def setperfilprofesional(self, perfilprofesional):
        self.__perfilprofesional = perfilprofesional

    def getproyectosdestacados(self):
        return self.__proyectosdestacados

    def setproyectosdestacados(self, proyectosdestacados):
        self.__proyectosdestacados = proyectosdestacados

    def getreferenciaslaborales(self):
        return self.__referenciaslaborales

    def setreferenciaslaborales(self, referenciaslaborales):
        self.__referenciaslaborales = referenciaslaborales

    def getlibretamilitar(self):
        return self.__libretamilitar

    def setlibretamilitar(self, libretamilitar):
        self.__libretamilitar = libretamilitar

    def getcompetencias(self):
        return self.__competencias

    def setcompetencias(self, competencias):
        self.__competencias = competencias

    def getexperiencia(self):
        return self.__experiencia

    def setexperiencia(self, experiencia):
        self.__experiencia = experiencia

    def geteducacion(self):
        return self.__educacion

    def seteducacion(self, educacion):
        self.__educacion = educacion

    def getidioma(self):
        return self.__idioma

    def setidioma(self, idioma):
        self.__idioma = idioma
