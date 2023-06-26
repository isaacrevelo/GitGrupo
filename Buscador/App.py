from Cargo import *
from Departamento import *
from Oferta import *
from Ubicacion import *
from Usuario import *

while True:
    print("Menu")
    print("1. Ver informacion de la oferta")
    print("2. Ver informacion del cargo")
    print("3. Ver informacion del departamento")
    print("4. Ver informacion de la ubicación")
    print("5. Salir")
    opcion = input("Ingrese el número de la opcion que desea: ")

    if opcion == "1":
        print("Informacion de la oferta:")
        print("ID:", oferta.getid())
        print("Numero de postulados:", oferta.getnumpostulados())
        print("Fecha de publicacion:", oferta.getfechapublicacion())
        print("Fecha de cierre:", oferta.getfechacierre())
    elif opcion == "2":
        cargo.Informacioncargo()
    elif opcion == "3":
        departamento.ID()
    elif opcion == "4":
        ubicacion.mostrarubicacion()
    elif opcion == "5":
        break
    else:
        print("Opcion invalida.")

print("Gracias por probar este programa")