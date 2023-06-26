class Departamento:
    def __init__(self, nombreD, tipoD):
        self.nombreD = nombreD
        self.tipoD = tipoD
    
    def get_nombreD(self):
        return self.__nombreD

    def set_nombreD(self, nombreD):
        self.__nombreD = nombreD

    def get_tipoD(self):
        return self.__tipoD

    def set_tipoD(self, tipoD):
        self.__tipoD = tipoD

    def ID(self):
        print("Nombre del departamento:", departamento.nombreD)
        print("Tipo de departamento:", departamento.tipoD)
departamento = Departamento("Departamentos de informática y programacion", "Tipo 1")