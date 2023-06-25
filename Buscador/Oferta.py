class Oferta:
    def __init__(self,id,numpostulados,fechapublicacion,fechacierre):
        self.__id=id
        #self.__vacante=[]
        self.__numpostulados=numpostulados
        self.__fechapublicacion=fechapublicacion
        self.__fechacierre=fechacierre
    
    def getid(self):
        return self.__id
    
    def setid(self,id):
        self.__id=id
    
    def getnumpostulados(self):
        return self.__numpostulados
    
    def setnumpostulados(self,numpostulados):
        self.__numpostulados=numpostulados
    
    def getfechapublicacion(self):
        return self.__fechapublicacion
    
    def setfechapublicacion(self,fechapublicacion):
        self.__fechapublicacion=fechapublicacion
    
    def getfechacierre(self):
        return self.__fechacierre
    
    def setfechacierre(self,fechacierre):
        self.__fechacierre=fechacierre