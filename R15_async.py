
# Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
# asíncrona una función que tardará en finalizar un número concreto de
# segundos parametrizables. También debes poder asignarle un nombre.
# La función imprime su nombre, cuándo empieza, el tiempo que durará
# su ejecución y cuando finaliza.

import asyncio


async def my_funct(name: str, time: int) -> None:
    print(f"Ejecutando {name}...")
    print(f"Ejecutando por {time}")
    await asyncio.sleep(time)
    print(f"La función {name} ha terminado")


# DIFICULTAD EXTRA (opcional):
# Utilizando el concepto de asincronía y la función anterior, crea
# el siguiente programa que ejecuta en este orden:
# - Una función C que dura 3 segundos.
# - Una función B que dura 2 segundos.
# - Una función A que dura 1 segundo.
# - Una función D que dura 1 segundo.
# - Las funciones C, B y A se ejecutan en paralelo.
# - La función D comienza su ejecución cuando las 3 anteriores han finalizado.


async def main():

    # await my_funct("function 1",5)

    await asyncio.gather(
        my_funct("A",1),
        my_funct("B",2),
        my_funct("C",3)
    )

    await my_funct("D",1)


if __name__ == "__main__":
    asyncio.run(main())
