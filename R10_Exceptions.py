# Explora el concepto de manejo de excepciones según tu lenguaje.
# Fuerza un error en tu código, captura el error, imprime dicho error
# y evita que el programa se detenga de manera inesperada.
# Prueba a dividir "10/0" o acceder a un índice no existente de un listado para intentar provocar un error.

try:
    print(10 / 0)
except ZeroDivisionError:
    print("No puedes dividir entre cero")
else:
    print(10 / 2)
finally:
    print("Thanks")

mylist: list[int] = [1,2,3,4,5]
# position: int = int(input("Que número de la lista quieres: ").strip())
#if position > len(mylist) - 1:
#   raise NameError
#else:
#    print(mylist[position])

# DIFICULTAD EXTRA (opcional):
# Crea una función que sea capaz de procesar parámetros, pero que también
# pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
# corresponderse con un tipo de excepción creada por nosotros de manera
# personalizada, y debe ser lanzada de manera manual) en caso de error.
# - Captura todas las excepciones desde el lugar donde llamas a la función.
# - Imprime el tipo de error.
# - Imprime si no se ha producido ningún error.
# - Imprime que la ejecución ha finalizado.


class errorStr(Exception):
    def __init__(self, message: str):
        super().__init__(message)


def cacha(var1: int, var2: str, var3:list):
    try:
        print(10 / var1)
        if var2 != "uwu":
            raise errorStr("Tu variable 2 no dice uwu")
        else:
            print("uwu")
        print(var3[var1])
    except Exception as e:
        print(f"Error {e}")
    else:
        print("Ejecucion sin errores")




cacha(7,"uwu",[1,2,3,4,5])
