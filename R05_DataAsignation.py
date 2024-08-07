
# EJERCICIO:
# - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#   su tipo de dato.

valor_uno = 5
valor_dos = valor_uno
valor_uno = 10
print(f"El primer valor es {valor_uno}")
print(f"El segundo valor es {valor_dos}")

lista_uno = [1,2,3,4,5]
lista_dos = lista_uno
lista_uno.pop()
print(f"Lista uno: {lista_uno}")
print(f"Lista dos: {lista_dos}")

# - Muestra ejemplos de funciones con variables que se les pasan "por valor" y por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.

def valores(valor):
    valor *= 2

valores(valor_uno)
print(f"El primer valor sigue siendo {valor_uno}")

def valores(valor):
    return valor * 2

valor_uno = valores(valor_uno)
print(f"Primer valor modificado {valor_uno}")

def referencia(valor):
    for i,n in enumerate(valor):
        valor[i] += 1

referencia(lista_uno)
print(lista_uno)
print(lista_dos)
# (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
#
# DIFICULTAD EXTRA (opcional):
# Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
# - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#   se asigna a dos variables diferentes a las originales. A continuación, imprime
#   el valor de las variables originales y las nuevas, comprobando que se ha invertido
#   su valor en las segundas.
#   Comprueba también que se ha conservado el valor original en las primeras.

var_1 = 1
var_2 = 2
var_3 = [1,2,3,4,5]
var_4 = [5,4,3,2,1]


def switch(f, s):
    f = s
    return f


res_1 = switch(var_1,var_2)
res_2 = switch(var_2,var_1)
print(f"Original 1: {var_1}")
print(f"Copia 1: {res_1}")
print(f"original 2: {var_2}")
print(f"Copia 2: {res_2}")

print("=====================")

def switch2(f, s):
    f = s
    return f
print(f"Prueba 1: {var_3}")
print(f"Prueba 2: {var_4}")

res_3 = switch2(var_3,var_4)
res_4 = switch2(var_4,var_3)


print(f"Copia 1: {res_3}")
print(f"Copia 2: {res_4}")
print(f"Prueba 1: {var_3}")
print(f"Prueba 2: {var_4}")



