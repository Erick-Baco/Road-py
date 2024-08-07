# EJERCICIO:
# Implementa los mecanismos de introducción y recuperación de elementos propios de las
# pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
# o lista (dependiendo de las posibilidades de tu lenguaje).

from collections import deque
from Retos.R07_Stacks_Queue.Queue import Queue
from Retos.R07_Stacks_Queue.Stack import Stack

cola: deque = deque()

mi_pila: Stack = Stack([])

mi_pila.insert("Pablo")
mi_pila.insert("Jose")
mi_pila.__str__()
mi_pila.expulse()
print("==========================")
mi_pila.__str__()

#print("\t")
#mi_cola: Queue = Queue()
#mi_cola.insert("Maria")
#mi_cola.insert("Juana")
#mi_cola.__str__()
#mi_cola.expulse()
#print("==========================")
#mi_cola.__str__()

print("\t")
cola.append("Maria")
cola.append("Juana")
print(cola)
print("==========================")
cola.popleft()
print(cola)

# DIFICULTAD EXTRA (opcional):
# - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#   el nombre de una nueva web.


def back() -> None:
    if historial.length() >= 2:
        historial.expulse()
        menu()
    else:
        print("No hay páginas por mostrar")
        menu()


def forward(page: str) -> None:
    historial.insert(page)
    menu()


historial: Stack = Stack(["Home"])
#historial.insert("Home")


def menu() -> None:
    global historial
    print(f"Bienvenido a tu historial, actualmente te encuentras en {historial.last()}, qué deseas hacer:")
    option: str = str(input("(Atrás) / (Adelante + nombre de la página): ").lower().strip())

    if option.find(" "):
        processed: tuple = option.partition(" ")
        action: str = processed[0]
        page: str = processed[2]

    if action == "atras":
        back()

    if action == "adelante":
        forward(page)


menu()
# - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#   interpretan como nombres de documentos.

cola_impresora: Queue = Queue()

def impresora():
    print("Cola de impresora")
    option: str = str(input("Escribe 'imprimir' o el nombre del archivo: ").lower().strip())  # type: ignore

    if option == "s":
        pass
    elif option == "imprimir":
        if cola_impresora.length() > 0:
            print(f"Imprimiendo {cola_impresora.last()}")
            cola_impresora.expulse()
            impresora()
        else:
            print("Cola de impresión vacía ")
            impresora()
    else:
        print(f"{option} añadido a la cola de impresion")
        cola_impresora.insert(option)
        impresora()


# impresora()