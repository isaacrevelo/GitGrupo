def mostrar_menu():
    print("menu ")
    print("1. Crear respuesta")
    print("2. Ver información de la respuesta")
    print("3. Crear prueba")
    print("4. Ver información de la prueba")
    print("5. Salir")


def crear_respuesta():
    id_respuesta = input("Ingrese el ID de la respuesta: ")
    nombre_autor = input("Ingrese el nombre del autor: ")
    destinatarios = input("Ingrese los destinatarios: ")
    estado = input("Ingrese el estado: ")

    nueva_respuesta = id_respuesta(id_respuesta, nombre_autor, destinatarios, estado)
    print("Respuesta creada con éxito!")


def ver_info_respuesta():
    id_respuesta = input("Ingrese el ID de la respuesta: ")

    

def crear_prueba():
    nombre_prueba = input("Ingrese el nombre de la prueba: ")
    preguntas_prueba = input("Ingrese las preguntas de la prueba: ")
    resultado = input("Ingrese el resultado: ")
    fecha_ejecucion = input("Ingrese la fecha de ejecución: ")

    nueva_prueba = preguntas_prueba(nombre_prueba, preguntas_prueba, resultado, fecha_ejecucion)
    print("Prueba creada con éxito!")


def ver_info_prueba():
    nombre_prueba = input("Ingrese el nombre de la prueba: ")

    
def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_respuesta()
        elif opcion == "2":
            ver_info_respuesta()
        elif opcion == "3":
            crear_prueba()
        elif opcion == "4":
            ver_info_prueba()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


ejecutar_menu()
