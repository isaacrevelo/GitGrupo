class Idioma:
    def __init__(self, nombreidioma, nivelidioma, certificacionidioma):
        self.__nombreidioma = nombreidioma
        self.__nivelidioma = nivelidioma
        self.__certificacionidioma = certificacionidioma

    def getNombreIdioma(self):
        return self.__nombreidioma

    def setNombreIdioma(self, nombreidioma):
        self.__nombreidioma = nombreidioma

    def getNivelIdioma(self):
        return self.__nivelidioma

    def setNivelIdioma(self, nivelidioma):
        self.__nivelidioma = nivelidioma

    def getCertificacionIdioma(self):
        return self.__certificacionidioma

    def setCertificacionIdioma(self, certificacionidioma):
        self.__certificacionidioma = certificacionidioma
