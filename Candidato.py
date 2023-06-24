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
