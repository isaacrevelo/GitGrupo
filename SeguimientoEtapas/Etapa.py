class Etapa:
    
    def __init__(self, revision_curriculum, entrevista_inicial, validar_referencias, contratado, no_contratado):
        self.__revision_curriculum=revision_curriculum
        self.__entrevista_inicial=entrevista_inicial
        self.__validar_referencias=validar_referencias
        self.__contratado=contratado
        self.__no_contratado=no_contratado
    
    def setRevisionCurriculum(self):
        self.__revision_curriculum='Revision de Curriculum'
    
    def getRevisionCurriculum(self):
        return self.__revision_curriculum
    
    def setEntrevistaInicial(self):
        self.__entrevista_inicial='Entrevista Inicial'
    
    def getEntrevistaInicial(self):
        return self.__entrevista_inicial
    
    def setValidarReferencias(self):
        self.__validar_referencias='Validacion de Referencias'
    
    def getValidarReferencias(self):
        return self.__validar_referencias
    
    def setContractado(self):
        self.__contratado='Contratado'
    
    def getContractado(self):
        return self.__contratado
    
    def setNoContractado(self):
        self.__no_contratado='No Contractado'
    
    def getNoContractado(self):
        return self.__no_contratado