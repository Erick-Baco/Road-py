# EJERCICIO:
# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#
# DIFICULTAD EXTRA (opcional):
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#   los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
#   (o el número de dígitos que quieras)
# - También se debe proponer una operación de finalización del programa.
#

mis_contactos = {"Erick":5610263904,"Eder":1122334455}


def contactos():
    print("Contactos")
    for x in mis_contactos:
        print(f"- {x} ")
    continuar()
def buscar():
    print("Contactos")
    nombre = input("Introduce el nombre de la persona: ")
    numero = mis_contactos.get(nombre)
    print(f"El número de {nombre} es {numero}")
    continuar()
def agregar():
    print("Agregar")
    nombre = input("Introduce el nombre de la persona: ")
    numero = str(input("Introduce el número de la persona: "))
    if len(numero) == 10:
        mis_contactos[nombre] = numero
    else:
        print("Numéro de carácteres incorrecto")
    continuar()
def actualizar():
    print("Actualizar")
    nombre = input("Introduce el nombre de la persona: ")
    numero = str(input("Introduce el nuevo número de la persona: "))
    if len(numero) == 10:
        mis_contactos[nombre] = numero
    else:
        print("Numéro de carácteres incorrecto")
    continuar()
def eliminar():
    print("Eliminar")
    nombre = input("Introduce el nombre de la persona: ")
    mis_contactos.pop(nombre)
    continuar()

def menu():
    print("AGENDA PERSONAL")
    print("menú de acciones")
    print("1.- Ver lista de contactos")
    print("2.- Buscar")
    print("3.- Agregar contacto")
    print("4.- Actualizar contacto")
    print("5.- Eliminar contacto")
    print("6.- Volver al menú")
    print("0.- Salir")
    opcion = int(input("Selecciona una opción: "))
    print(f"opcion elegida {opcion}")
    elegir(opcion)

def elegir(eleccion):
    if eleccion == 0:
        exit()
    elif eleccion == 1:
        contactos()
    elif eleccion == 2:
        buscar()
    elif eleccion == 3:
        agregar()
    elif eleccion == 4:
        actualizar()
    elif eleccion == 5:
        eliminar()
    elif eleccion == 6:
        menu()

def continuar():
    print("Qúe deseas hacer ahora?")
    print("6.- Volver al menú")
    print("0.- Salir")
    opcion = int(input("Selecciona una opción: "))
    elegir(opcion)



menu()

