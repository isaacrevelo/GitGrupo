class Educacion:
    def __init__(self, nivel_educativo, institucion_educativa, campo_estudio, fecha_inicio, fecha_fin):
        self.nivel_educativo = nivel_educativo
        self.institucion_educativa = institucion_educativa
        self.campo_estudio = campo_estudio
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def getNivelEducativo(self):
        return self.nivel_educativo

    def setNivelEducativo(self, nivel_educativo):
        self.nivel_educativo = nivel_educativo

    def getInstitucionEducativa(self):
        return self.institucion_educativa

    def setInstitucionEducativa(self, institucion_educativa):
        self.institucion_educativa = institucion_educativa

    def getCampoEstudio(self):
        return self.campo_estudio

    def setCampoEstudio(self, campo_estudio):
        self.campo_estudio = campo_estudio

    def getFechaInicio(self):
        return self.fecha_inicio

    def setFechaInicio(self, fecha_inicio):
        self.fecha_inicio = fecha_inicio

    def getFechaFin(self):
        return self.fecha_fin

    def setFechaFin(self, fecha_fin):
        self.fecha_fin = fecha_fin
