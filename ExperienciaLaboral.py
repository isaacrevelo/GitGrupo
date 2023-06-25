class ExperienciaLaboral:
    def __init__(self, titulopuesto, empresa, descripcion, fechainicio, fechafin, motivoretiro):
        self.__titulo_puesto = titulopuesto
        self.__empresa = empresa
        self.__descripcion = descripcion
        self.__fechainicio = fechainicio
        self.__fechafin = fechafin
        self.__motivoretiro = motivoretiro

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

    def get_fecha_inicio(self):
        return self.__fechainicio

    def set_fecha_inicio(self, fechainicio):
        self.__fechainicio = fechainicio

    def get_fecha_fin(self):
        return self.__fechafin

    def set_fecha_fin(self, fechafin):
        self.__fechafin = fechafin

    def get_motivo_retiro(self):
        return self.__motivoretiro

    def set_motivo_retiro(self, motivoretiro):
        self.__motivoretiro = motivoretiro
