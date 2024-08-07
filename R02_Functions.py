# EJERCICIO:
# - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
#   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
import random


def no_par_ret():
    print("Funcion sin parametros ni retorno")

no_par_ret()

def par(x):
    print(f"Función con retorno, el valor es {x}")

par(34)

def ret():
    return random.randint(0,100)

a = ret()

print(f"Valor random es {a}")

def par_ret(x):
    return  random.randint(0,x)

a = par_ret(10)

print(f"Valor random es {a}")

# - Comprueba si puedes crear funciones dentro de funciones.

def funciones():
    print("funcion 1")
    def nested():
        print("funcion 2")
    nested()

funciones()

# - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

milista = [1,3,2,4,6,5,8,7,9]
milista.sort()
for x in milista:
    print(x)


# - Pon a prueba el concepto de variable LOCAL y GLOBAL.

global_var = "global"
def variables():
    print(global_var)
    local_var = "local"

variables()
try:
    print(local_var)
except NameError:
    print("la variable local no llega al scope global")

# - Debes hacer print por consola del resultado de todos los ejemplos.
#   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#
# DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def extra(primer_num, segundo_num):

    count = 0
    for x in range (1,101):
        if x % 3 == 0 and x % 5 == 0:
            print(f"Multiplo de 5 y 3. {primer_num}, {segundo_num}")
        elif x % 3 == 0:
            print(f"Multiplo de 3. {primer_num}")
        elif x % 5 == 0:
            print(f"Multiplo de 5. {segundo_num}")
        else:
            print(x)
            count += 1
    print(f"El número de veces que se imprimió numéro fueron: {count}")


extra("Hola","Adiós")