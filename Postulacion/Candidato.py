from Usuario import *
from Competencias import *
from Idioma import *
from Educacion import *
from ExperienciaLaboral import *

class Candidato(Usuario):
    def __init__(self, telefono, correo, direccion,
                 nombre,perfilprofesional,proyectosdestacados,
                 referenciaslaborales,libretamilitar):
        super().__init__(telefono, correo, direccion)
        self.__nombre=nombre
        self.__perfilprofesional=perfilprofesional
        self.__proyectosdestacados=proyectosdestacados
        self.__referenciaslaborales=referenciaslaborales
        self.__libretamilitar=libretamilitar
        self.__competencias=[]
        self.__experiencia=[]
        self.__educacion=None
        self.__idioma=[]

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

    def agregar_competencia(self, nombrecompetencia, descripcion, niveldominio):
        competencia = Competencias(nombrecompetencia, descripcion, niveldominio)
        self.__competencias.append(competencia)

    def obtener_competencias(self):
        return self.__competencias

    def agregar_idioma(self, nombreidioma, nivelidioma):
        idiomas = Idioma(nombreidioma, nivelidioma)
        self.__idioma.append(idiomas)

    def obtener_idiomas(self):
        return self.__idioma

    def establecer_educacion(self, nivel_educativo, institucion_educativa, campo_estudio, duracion):
        educacion = Educacion(nivel_educativo, institucion_educativa, campo_estudio, duracion)
        self.__educacion = educacion

    def obtener_educacion(self):
        return self.__educacion

    def agregar_experiencia_laboral(self, titulopuesto, empresa, descripcion,duracion):
        experienciaL = ExperienciaLaboral(titulopuesto, empresa, descripcion,duracion)
        self.__experiencia.append(experienciaL)

    def obtener_experiencia_laboral(self):
        return self.__experiencia