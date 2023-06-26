from Etapa import *

class Seguimiento:

    def __init__(self, estado):
        self.__estado=estado
        
    def CambiarEtapa(self, aux):
        etapa = Etapa(None, None, None, None, None)
        if aux == 1:
            etapa.setRevisionCurriculum()
            self.__estado=etapa.getRevisionCurriculum()
        elif aux == 2:
            etapa.setEntrevistaInicial()
            self.__estado=etapa.getEntrevistaInicial()
        elif aux == 3:
            etapa.setValidarReferencias()
            self.__estado=etapa.getValidarReferencias()
        elif aux == 4:
            etapa.setContractado()
            self.__estado=etapa.getContractado()
        elif aux == 5:
            etapa.setNoContractado()
            self.__estado=etapa.getNoContractado()

    def getEstado(self):
        return self.__estado

        
