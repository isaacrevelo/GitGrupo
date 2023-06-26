class ExperienciaLaboral:
    def __init__(self, titulopuesto, empresa, descripcion,duracion):
        self.__titulopuesto=titulopuesto
        self.__empresa = empresa
        self.__descripcion = descripcion
        self.__duracion=duracion

    def get_titulo_puesto(self):
        return self.__titulopuesto

    def set_titulo_puesto(self, titulopuesto):
        self.__titulopuesto = titulopuesto

    def get_empresa(self):
        return self.__empresa

    def set_empresa(self, empresa):
        self.__empresa = empresa

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def getduracion(self):
        return self.__duracion

    def setduracion(self, duracion):
        self.__duracion= duracion

    def get_fecha_fin(self):
        return self.__fechafin

    def set_fecha_fin(self, fechafin):
        self.__fechafin = fechafin

    def get_motivo_retiro(self):
        return self.__motivoretiro

    def set_motivo_retiro(self, motivoretiro):
        self.__motivoretiro = motivoretiro
