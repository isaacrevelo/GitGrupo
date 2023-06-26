from Usuario import *
from Candidato import *
from Empresa import *
from Oferta import *
from Vacante import *
from Competencias import *
from Idioma import *
from Educacion import *
from ExperienciaLaboral import *

candidato = Candidato("1234567890", "isaacrevelo@gmail.com", "Calle 10", "Isaac Revelo", "Eh trabajado por 5 años en la NASA", "Se construyo uno de los mejores telecopios del mundo el 'James Webb' ", "Del jefe: Trabajo en nuestra empresa como ingeniero", "Si aplica")

candidato.agregar_competencia("Trabajo en equipo", "Lleve a cabo proyectos exitosos en equipo con colegas", "Considero un alto nivel de dominio")
candidato.agregar_competencia("Pensamiento critico", "Pienso en una situacion de forma calmada para dar la mejor respuesta", "Un nivel intermedio de dominio")

candidato.agregar_idioma("Ingles", "B2")
candidato.agregar_idioma("Aleman", "B1")

candidato.establecer_educacion("Ingeniero De Sistemas", "Universidad Nacional", "Tecnologia", "5 años")

candidato.agregar_experiencia_laboral("Programador", "Nintendo", "Trabaje en Nintendo haciendo la programacion de diferentes videojuegos", "5 años")

print("Nombre del candidato:", candidato.getnombre())
print("Competencias del candidato:", candidato.obtener_competencias())
print("Idiomas del candidato:", candidato.obtener_idiomas())
print("Educación del candidato:", candidato.obtener_educacion())
print("Experiencia laboral del candidato:", candidato.obtener_experiencia_laboral())

empresa = Empresa("0987654321", "Cocacola@sas.com", "Calle 50 Bogota", "COMPAÑÍA SERVICIOS DE BEBIDAS REFRESCANTES, S.L.")

oferta = Oferta("ID 01","Desarrollador", "50", "15/05/2023", "27/06/2023")

vacante = Vacante("Desarrollador de software", "7", "3500000", "Minimo de 5 años de experiencia")
oferta.agregarvacante(vacante)

print("ID de la oferta:", oferta.getid())
print("Vacantes de la oferta:")
oferta.getvacantes()

