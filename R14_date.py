#EJERCICIO:
#Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
#- Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
#- Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
#Calcula cuántos años han transcurrido entre ambas fechas.
import datetime

today = datetime.datetime.now()
birth_date = datetime.datetime(2004,10,14,23,30,1)

print(f"Desde mi nacimiento han pasado {today.year - birth_date.year} años")
print(today)

#DIFICULTAD EXTRA (opcional):
#Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
#10 maneras diferentes. Por ejemplo:
#- Día, mes y año.
#- Hora, minuto y segundo.
#- Día de año.
#- Día de la semana.
#- Nombre del mes.
#(lo que se te ocurra...)

print("Formatos para fecha de nacimiento")
print(f"1. Version local de fecha {birth_date.strftime('%x')}")
print(f"1. Año, mes completo, día de la semana {birth_date.strftime('%Y-%B-%A')}")
print(f"1. Año, mes abreviados, día {birth_date.strftime('%y-%b-%d')}")
print(f"1. Version local de fecha y hora{birth_date.strftime('%c')}")
print(f"1. Día del año {birth_date.strftime('%j')}")
print(f"1. Numero de día de la semana {birth_date.strftime('%u')}")
print(f"1. Numero de semana del año {birth_date.strftime('%V')}")
print(f"1. Hora y zona horario {birth_date.strftime('%X-%Z')}")
print(f"1. Hora (12) y pm{birth_date.strftime('%l-%p')}")
print(f"1. Hora (24), mes, minuto, segundo {birth_date.strftime('%H-%m-%M-%S')}")
print(f"1. Mes, día {birth_date.strftime('%b-%d')}")
