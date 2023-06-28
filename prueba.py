class prueba:
    def __init__(self,nombre_prueba,preguntas_prueba,resultado,fecha_ejecucion):
        self.nombre_prueba=nombre_prueba
        self.preguntas_pruebas=preguntas_prueba
        self.resultado=resultado
        self.fecha_ejecucion=fecha_ejecucion
    def get_nombre_prueba(self):
        return self.nombre_prueba
    def set_nombre_prueba(self,nombre_prueba):
        self._nombre_prueba=nombre_prueba
    def get_preguntas_pruebas(self):
        return self.preguntas_pruebas
    def set_preguntas_pruebas(self,preguntas_pruebas):
        self._preguntas_pruebas=preguntas_pruebas
    def getresultado(self):
        return self.resultado
    def setresultado(self,resultado):
        self._resultado=resultado
    def get_fecha_ejecucion(self):
        return self.fecha_ejecucion
    def set_fecha_ejecucion(self,fecha_ejecucion):
        self._fecha_ejecucion=fecha_ejecucion
    def calificacion(self):
        print("nombre de la prueba:", self._nombre_prueba)
        print("preguntas de la prueba:", self._preguntas_pruebas)
        print("el resultado es:", self._resultado)
        print("la fecha es:", self._fecha_ejecucion)    


