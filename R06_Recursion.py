
# EJERCICIO:
# Entiende el concepto de recursividad creando una función recursiva que imprima
# números del 100 al 0.

def recursive(index):
    print(index)
    index -= 1
    if index > -1:
        recursive(index)


recursive(100)


# DIFICULTAD EXTRA (opcional):
# Utiliza el concepto de recursividad para:
# - Calcular el factorial de un número concreto (la función recibe ese número)

def factorial(number: int) -> int:
    if number < 0:
        print("Los números negativos no son válidos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(3))


# - Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci
# (la función recibe la posición).


def fibonacci(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)


print(fibonacci(5))