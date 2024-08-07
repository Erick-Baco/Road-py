
# EJERCICIO:
# Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
# en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
# - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
#   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...


demo = "Cadena de prueba"
demo_2 = "Hola mundo"

print(f"El caracter en la posición 3 es: {demo[3]}")

print(f"Primera palabra es: {demo[:6]}")

print(f"La longitud de la última palabra es: {len(demo[10:])}")

demo_3 = demo + " " + demo_2
print(f"Cdenas unidas: {demo_3}")

print(f"Repeticion")

print(f"Recorrido de la cadena")
for i in demo_2:
    print(i)

print(demo.lower())

print(demo.upper())

demo = demo.replace("Cadena","Chain")
print(f"Cadena modificada: {demo}")

print(demo_2.split(" "))

nombre = "Juan"
edad = 30
cadena = "Mi nombre es %s y tengo %d años." % (nombre, edad)
print(cadena)


# DIFICULTAD EXTRA (opcional):
# Crea un programa que analice dos palabras diferentes y realice comprobaciones
# para descubrir si son:
# - Palíndromos
# - Anagramas
# - Isogramas

def palindromo(first_word, second_word):
    length = len(first_word)
    index = -1
    flag = True
    if len(first_word) == len(second_word):
        for i in first_word:
            if i != second_word[index]:
                flag = False
                break
            else:
                index -= 1
    else:
        flag = False

    if flag:
        print("Palindromo")
    else:
        print("No Palindromo")

def anagrama(first_word, second_word):
    flag = True
    first_list =[]
    second_list=[]
    index = 0
    if len(first_word) == len(second_word):
        for i in first_word:
            first_list.append(i)
        for i in second_word:
            second_list.append(i)
        first_list.sort()
        second_list.sort()

        for i in first_list:
            if i != second_list[index]:
                print(second_list[index])
                flag = False
                break
            else:
                index += 1
    if flag:
        print("Anagrama")
    else:
        print("No Anagrama")
def isograma(first_word):
    list = []
    flag = True
    for i in first_word:
        list.append(i)

    for i in list:
        index = 0
        counter = []
        while index < len(list):
            if i == list[index]:
                counter.append(i)
            index += 1
        if len(counter) > 1:
            flag = False
            break

    if flag:
        print("Isograma")
    else:
        print("No isograma")
def analizador(first_word, second_word):
    palindromo(first_word, second_word)
    anagrama(first_word, second_word)
    isograma(first_word)
    isograma(second_word)

first = str(input("Introduce la primera palabra: ")).lower().strip()
second = str(input("Introduce la segunda palabra: ")).lower().strip()

analizador(first,second)

