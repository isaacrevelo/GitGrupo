class Competencias:
    def __init__(self, nombrecompetencia, descripcion, niveldominio, logrosdestacados):
        self.__nombrecompetencia = nombrecompetencia
        self.__descripcion = descripcion
        self.__niveldominio = niveldominio
        self.__logrosdestacados = logrosdestacados

    def getnombrecompetencia(self):
        return self.__nombrecompetencia

    def getdescripcion(self):
        return self.__descripcion

    def getniveldominio(self):
        return self.__niveldominio

    def getlogrosdestacados(self):
        return self.__logrosdestacados

    def setnombrecompetencia(self, nombrecompetencia):
        self.__nombrecompetencia = nombrecompetencia

    def setdescripcion(self, descripcion):
        self.__descripcion = descripcion

    def setniveldominio(self, niveldominio):
        self.__niveldominio = niveldominio

    def setlogrosdestacados(self, logrosdestacados):
        self.__logrosdestacados = logrosdestacados
