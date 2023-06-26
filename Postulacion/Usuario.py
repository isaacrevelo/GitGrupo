class Usuario:
    def __init__(self,telefono,correo,direccion):
        self.__telefono=telefono
        self.__correo=correo
        self.__direccion=direccion
    
    def gettelefono(self):
        return self.__telefono
    
    def settelefono(self,telefono):
        self.__telefono=telefono
    
    def getcorreo(self):
        return self.__correo
    
    def settelefono(self,correo):
        self.__correo=correo
    
    def getdireccion(self):
        return self.__direccion
    
    def setdireccion(self,direccion):
        self.__direccion=direccion