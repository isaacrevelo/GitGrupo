class Localizacion:
    def __init__(self, codigoD, codigoM, departamento, municipio):
        self.codigoD = codigoD
        self.codigoM = codigoM
        self.departamento = departamento
        self.municipio = municipio
    
    def get_codigoD(self):
        return self.__codigoD

    def set_codigoD(self, codigoD):
        self.__codigoD = codigoD 

    def get_codigoM(self):
        return self.__codigoM

    def set_codigoM(self, codigoM):
        self.__codigoM = codigoM

    def get_departamento(self):
        return self.__departamento

    def set_departamento(self, departamento):
        self.__departamento = departamento
    
    def get_municipio(self):
        return self.__municipio

    def set_municipio(self, municipio):
        self.__municipio = municipio


    def mostrarubicacion(self):
        print("Codigo del departamento:", self.codigoD)
        print("Codigo del municipio:", self.codigoM)
        print("Nombre del departamento:", self.departamento)
        print("Nombre del municipio:", self.municipio)