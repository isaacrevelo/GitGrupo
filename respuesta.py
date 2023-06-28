class respuesta:
    def __init__(self,id_respuesta,nombre_autor,destinatarios,estado):
        self.id_respuesta=id_respuesta
        self.nombre_autor=nombre_autor
        self.destinatarios=destinatarios
        self.estado=estado
    def get_id_respuesta(self):
        return self.id_respuesta
    def set_id_respuesta(self,id_respuesta):
        self._id_respuesta=id_respuesta
    def get_nombre_autor(self):
        return self.nombre_autor
    def set_nombre_autor(self,nombre_autor):
        self._nombre_autor=nombre_autor
    def getdestinatarios(self):
        return self.destinatarios
    def setdestinatarios(self,destinatarios):
        self._destinatarios=destinatarios
    def getestado(self):
        return self.estado
    def setestado(self,estado):
        self._estado=estado
    def Informacioncargo(self):
        print("id de la respuesta:", self._id_respuesta)
        print("nombre del auotor:", self._nombre_autor)
        print("destinatarios:", self._destinatarios)
        print("estado:", self._estado)           


        