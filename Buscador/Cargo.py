class Cargo:
    def __init__(self, requisitos, duracion, tipocontrato, cupos):
        self.requisitos = requisitos
        self.duracion = duracion
        self.tipocontrato = tipocontrato
        self.cupos = cupos
    def get_requisitos(self):
        return self.__requisitos

    def set_requisitos(self, requisitos):
        self.__requisitos = requisitos

    def get_duracion(self):
        return self.__duracion

    def set_duracion(self, duracion):
        self.__duracion = duracion

    def get_tipocontrato(self):
        return self.__tipocontrato

    def set_tipocontrato(self, tipocontrato):
        self.__tipocontrato = tipocontrato

    def get_cupos(self):
        return self.__cupos

    def set_cupos(self, cupos):
        self.__cupos = cupos

    def Informacioncargo(self):
        print("Requisitos:", self.requisitos)
        print("Duración:", self.duracion)
        print("Tipo de contrato:", self.tipocontrato)
        print("Cupos:", self.cupos)