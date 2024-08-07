#Crea una función que se encargue de sumar dos números y retornar
#su resultado.
#Crea un test, utilizando las herramientas de tu lenguaje, que sea
#capaz de determinar si esa función se ejecuta correctamente.

import pytest


def sum(x: int,y: int) -> int:
    return x + y


@pytest.mark.parametrize(
    "input_1,input_2,expected",
    [
        (1,6,7),
        (6,sum(3,6),15),
        (sum(1,2),3,6),
        (1,2,sum(1,2))
    ]
)
def test_sum(input_1: int, input_2: int,expected: int):
    assert sum(input_1,input_2) == expected

#DIFICULTAD EXTRA (opcional):
#Crea un diccionario con las siguientes claves y valores:
#"name": "Tu nombre"
#"age": "Tu edad"
#"birth_date": "Tu fecha de nacimiento"
#"programming_languages": ["Listado de lenguajes de programación"]
#Crea dos test:
#- Un primero que determine que existen todos los campos.
#- Un segundo que determine que los datos introducidos son correctos.


my_dict: dict = {"name": "Erick",
                 "age": "19",
                 "birth_date": "2004-10-14",
                 "programming_languages": ["java", "python", "c"]}


@pytest.mark.parametrize(
    "data",
    [my_dict]
)
def test_fields(data):
    items = data.values()
    for i in items:
        assert len(i) > 0

@pytest.mark.parametrize(
    "data",
    [my_dict]
)
def test_field_type(data):
    items = data.values()
    for i in items:
        assert type(i) == str or type(i) == list