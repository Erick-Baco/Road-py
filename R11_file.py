import os
# Desarrolla un programa capaz de crear un archivo que se llame como
# tu usuario de GitHub y tenga la extensión .txt.
# Añade varias líneas en ese fichero:
# - Tu nombre.
# - Edad.
# - Lenguaje de programación favorito.
# Imprime el contenido.
# Borra el fichero.

f = open("Erick-Baco-Moure.txt","w")
f.write("Erick \n")
f.write("19 \n")
f.write("Python \n")
f.close()
f = open("Erick-Baco-Moure.txt","r")
print(f.read())

if os.path.exists("Erick-Baco-Moure.txt"):
    os.remove("Erick-Baco-Moure.txt")


# DIFICULTAD EXTRA (opcional):
# Desarrolla un programa de gestión de ventas que almacena sus datos en un 
# archivo .txt.
# - Cada producto se guarda en una línea del archivo de la siguiente manera:
#   [nombre_producto], [cantidad_vendida], [precio].
# - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#   actualizar, eliminar productos y salir.
# - También debe poseer opciones para calcular la venta total y por producto.
# - La opción salir borra el .txt.


def menu() -> None:
    print("1.- Añadir producto")
    print("2.- Consultar ")
    print("3.- Actualizar producto")
    print("4.- Eliminar producto")
    print("5.- Calcular venta total")
    print("6.- Calcular venta por producto")
    print("0.- Salir")
    option: str = input("Selecciona una opción: ").strip()
    if option == "1":
        add()
    elif option == "2":
        read()
    elif option == "3":
        update()
    elif option == "4":
        delete()
    elif option == "5":
        total()
    elif option == "6":
        product: str = input("Introduce el nombre del producto: ").strip().lower()
        suma: float = individual(product)
        print("\n\t Almacen")
        print(f"Las ventas de {product} suman: ${suma} \n")

        menu()
    else:
        salir()


def total() -> None:
    f = open("Erick-Baco-Moure.txt", "r")
    data: str = f.read()
    f.close()
    lines: list[str] = data.split("\n")
    sumatoria: list[float] = []
    products: list[list[str]] = []
    names: list[str] = []

    for registro in lines:
        products.append(registro.split(","))

    for product in products:
        if product[0] != "":
            names.append(product[0].strip("[$] "))

    for name in names:
        sumatoria.append(individual(name))

    print("\n\t Almacen")
    print(f"Las ventas totales son de: ${sum(sumatoria)} \n")

    menu()


def individual(product: str) -> float:

    f = open("Erick-Baco-Moure.txt", "r")
    data: str = f.read()
    f.close()
    lines: list[str] = data.split("\n")

    extract: list[str] = []
    for j in lines:
        if product in j:
            extract = j.split(",")

    quantity: float = float(extract[1].strip("[] "))
    price: float = float(extract[2].strip("[$] "))

    return quantity * price


def delete() -> None:
    product: str = input("Introduce el nombre del producto: ").strip().lower()

    f = open("Erick-Baco-Moure.txt", "r")
    data: str = f.read()
    f.close()
    lines: list[str] = data.split("\n")

    for i, j in enumerate(lines):
        if product in j:
            print("\n\t Almacen")
            print(f"{product} ha sido eliminado del almacen \n")
            lines.pop(i)

    f = open("Erick-Baco-Moure.txt", "w")

    for prod in lines:
        f.write(f"{prod} \n")

    f.close()
    menu()


def update() -> None:
    product: str = input("Introduce el nombre del producto: ").strip().lower()
    modificar: str = input("Valor a modificar: ").strip().lower()
    new: str = input("Introduce el valor nuevo: ").strip().lower()

    f = open("Erick-Baco-Moure.txt", "r")
    data: str = f.read()
    f.close()
    lines: list[str] = data.split("\n")

    for i,j in enumerate(lines):
        if product in j:
            print("\n\t Almacen")
            print(f"Se ha modificado {modificar} por {new} en {product} \n")
            lines[i] = lines[i].replace(modificar,new)

    f = open("Erick-Baco-Moure.txt", "w")

    for prod in lines:
        f.write(f"{prod} \n" )

    f.close()
    menu()


def add() -> None:
    f = open("Erick-Baco-Moure.txt", "a")
    product: str = input("Introduce el nombre del producto: ").strip().lower()
    quantity: str = input("Cantidad vendida: ").strip().lower()
    price: str = input("Precio: ").strip().lower()
    print("\n\t Almacen")
    print(f"Se ha añadido {product} al almacen \n")
    f.write(f"[{product}],[{quantity}],[{price}] \n")
    f.close()
    menu()


def read() -> None:
    f = open("Erick-Baco-Moure.txt", "r")
    print("\n\t Almacen")
    print(f.read())
    f.close()
    menu()


def salir() -> None:
    print("Programa finalizado")
    if os.path.exists("Erick-Baco-Moure.txt"):
        os.remove("Erick-Baco-Moure.txt")
        print("Archivo eliminado")
    else:
        print("Archivo no encontrado")


menu()
