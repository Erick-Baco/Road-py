
# Utilizando tu lenguaje, explora el concepto de expresiones regulares,
# creando una que sea capaz de encontrar y extraer todos los números
# de un texto.

import re

txt: str = "Hola soy erick, hoy estamos a 8 de agosto de 2024"

x = re.findall("[0-9]",txt)
print(x)

# DIFICULTAD EXTRA (opcional):
# Crea 3 expresiones regulares (a tu criterio) capaces de:
# - Validar un email.
# - Validar un número de teléfono.
# - Validar una url.

txt = "jesusbaco542@gmail.com"

if re.match(r"^[a-z0-9]+@[a-z]+\.[a-z]{2,}$",txt):
    print("email valido")
else:
    print("f")

txt = "5610263904"

if re.match(r"^[0-9]{10}",txt):
    print("teléfono válido")
else:
    print("f")

txt = "https://chatgpt.com"

if re.match(r"^https://+[a-z]+\.[a-z]{2,}$",txt):
    print("direción válida ")
else:
    print("f")



