"""/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */"""

a = 1

b = 5

c = [1,2,3,4,5]

d = True

e = False

# Aritméticos
print("Aritméticos")
print(a + b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)

print("Lógicos")
print(d and e)
print(d or e)
print(not  e)

print("Comparación")
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b)
print(a == b)

print("Asignación")
a -= 2
print(a)
a += 5
print(a)
a *= 3
print(a)
a /= 4
print(a)
a //= 3
print(a)
a %= 1
print(a)
a **= 4
print(a)

print("Identidad")
print(a is b)
print(a is not c)

print("Pertenencia")
print(a not in c)
print(b in c)

print("Bits")
"""
& (AND): Realiza la operación AND bit a bit.
| (OR): Realiza la operación OR bit a bit.
^ (XOR): Realiza la operación XOR (T y F) bit a bit.
~ (NOT): Invierte todos los bits.
<< (Desplazamiento a la izquierda): Desplaza los bits a la izquierda.
>> (Desplazamiento a la derecha): Desplaza los bits a la derecha.
"""
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101

print(a & b)  # Salida: 12 (0000 1100)
print(a | b)  # Salida: 61 (0011 1101)
print(a ^ b)  # Salida: 49 (0011 0001)
print(~a)  # Salida: -61 (1100 0011)
print(a << 2)  # Salida: 240 (1111 0000)
print(a >> 2)  # Salida: 15 (0000 1111)

print("Estructuras")
print("if")
if (a <= b):
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es mayor que {b}")

print("for")
for x in c:
    print(x)

print("while")
x = 0
while x < len(c):
    print(c[x])
    x += 1

print("Try")
try:
    f = open("demo.txt")
    f.close()
except FileNotFoundError:
    print("No encontrado")


def extra():
    x = 10
    while x < 56:
        if x != 16 and (x % 2 == 0) and (x % 3 != 0):
            print(x)
            x += 1
        else:
            x += 1

    print("for")

    for i in range(10,56):
        if (i != 16) and (i % 2 == 0) and (i % 3 != 0):
            print(i)



extra()

