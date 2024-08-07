# IMPORTANTE: Solo debes subir el fichero de código como parte del ejercicio.
import os
import xml.etree.ElementTree as ET
import json
import xmltodict
from dicttoxml import dicttoxml

# EJERCICIO:
# Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
# siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
# - Nombre
# - Edad
# - Fecha de nacimiento
# - Listado de lenguajes de programación
# Muestra el contenido de los archivos.
# Borra los archivos.


def create(name: str, age: str, bday: str, lan: list[str]) -> None:
    if os.path.exists("fichero.xml"):
        tree = ET.parse("fichero.xml")
        root = tree.getroot()

        person = ET.Element("person")
        ET.SubElement(person, "a", {"name": name})
        ET.SubElement(person, "a", {"age": age})
        ET.SubElement(person, "a", {"birthday": bday})

        for i in lan:
            ET.SubElement(person, "languaje", {"name": i})

        ET.indent(person)
        root.append(person)
        ET.indent(root)

        tree.write("fichero.xml")
    else:
        f = open("fichero.xml", "w")
        a = ET.Element("people")
        a.set("profession", "software engineer")

        person = ET.Element("person")
        ET.SubElement(person, "a", {"name": name})
        ET.SubElement(person, "a", {"age": age})
        ET.SubElement(person, "a", {"birthday": bday})

        for i in lan:
            ET.SubElement(person, "languaje", {"name": i})

        ET.indent(person)
        a.append(person)
        ET.indent(a)
        et = ET.ElementTree(a)
        et.write("fichero.xml", xml_declaration=True)


def read() -> None:
    root = ET.parse("fichero.xml")
    root_node = root.getroot()
    print(root_node.tag, root_node.attrib)
    for child in root_node:
        print(ET.tostring(child))


def delete(file: str) -> None:
    if os.path.exists(file):
        os.remove(file)
    else:
        print("File not found")


def createjs(name: str, age: str, bday: str, lan: list[str]) -> None:
    if not os.path.exists("json.txt"):
        data: dict = {"people": "software engineer",
                      name: {"edad": age,
                             "cumpleanios": bday,
                             "lenguajes": lan}}
        with open("json.txt", "a") as file:
            json.dump(data, file)
    else:
        with open("json.txt", "r") as file:
            data = json.load(file)
            data[name] = dict(edad=age, cumpleanios=bday, lenguajes=lan)
        with open("json.txt", "w") as file:
            json.dump(data, file)


def readjs(name: str) -> None:
    with open(name, "r") as file:
        data = json.load(file)

    print(data)


#create("erick", "19", "14-oct-04", ["java", "python"])
#read()
#delete("fichero.xml")

#createjs("erick", "19", "14-oct-04", ["java", "python", "sql"])
#readjs("json.txt")
#delete("json.txt")

# DIFICULTAD EXTRA (opcional):
# Utilizando la lógica de creación de los archivos anteriores, crea un
# programa capaz de leer y transformar en una misma clase custom de tu 
# lenguaje los datos almacenados en el XML y el JSON.
# Borra los archivos.


class Conveter:

    def __init__(self):
        pass

    @staticmethod
    def xml_to_json() -> None:
        with open("fichero.xml","r") as file:
            data: str = file.read()
        doc = xmltodict.parse(data)

        with open("xml_to_json.txt", "w") as file:
            json.dump(doc, file)

    @staticmethod
    def json_to_xml() -> None:
        with open("json.txt","r") as file:
            data: str = file.read()

        dict_data = json.loads(data)
        xml_data = dicttoxml(dict_data, custom_root='root', attr_type=False)

        with open("json_to_xml.xml", "w") as file:
            file.write(xml_data.decode('utf-8'))

        format = ET.parse("json_to_xml.xml")
        root = format.getroot()
        ET.indent(root)
        et = ET.ElementTree(root)
        et.write("json_to_xml.xml", xml_declaration=True)


Conveter.json_to_xml()

