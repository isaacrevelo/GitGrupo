from Usuario import *
from Candidato import *
from Empresa import *
from Oferta import *
from Vacante import *
from Competencias import *
from Idioma import *
from Educacion import *
from ExperienciaLaboral import *

candidato = Candidato("1234567890", "correo@example.com", "Dirección de prueba", "Nombre del candidato", "Perfil profesional", "Proyectos destacados", "Referencias laborales", "Libreta militar")

candidato.agregar_competencia("Competencia 1", "Descripción de la competencia 1", "Nivel de dominio 1")
candidato.agregar_competencia("Competencia 2", "Descripción de la competencia 2", "Nivel de dominio 2")

candidato.agregar_idioma("Idioma 1", "Nivel de idioma 1")
candidato.agregar_idioma("Idioma 2", "Nivel de idioma 2")

candidato.establecer_educacion("Nivel educativo", "Institución educativa", "Campo de estudio", "Duración")

candidato.agregar_experiencia_laboral("Título del puesto", "Empresa", "Descripción de la experiencia laboral", "Duración")

print("Nombre del candidato:", candidato.getnombre())
print("Competencias del candidato:", candidato.obtener_competencias())
print("Idiomas del candidato:", candidato.obtener_idiomas())
print("Educación del candidato:", candidato.obtener_educacion())
print("Experiencia laboral del candidato:", candidato.obtener_experiencia_laboral())

empresa = Empresa("0987654321", "correo@empresa.com", "Dirección de la empresa", "NIT de la empresa")

oferta = Oferta("ID de la oferta", "Número de postulados", "Fecha de publicación", "Fecha de cierre")

vacante = Vacante("Ocupación de la vacante", "Número de vacantes", "Salario de la vacante", "Experiencia requerida")
oferta.agregarvacante(vacante)

print("ID de la oferta:", oferta.getid())
print("Vacantes de la oferta:")
oferta.getvacantes()
