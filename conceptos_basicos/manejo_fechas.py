import datetime
import pytz

# Capturar el año, mes, dia, hora, minuto, segundo y milisegundos actuales del dispositivo.
d = datetime.datetime.now()
print(d)
# Capturar el año, mes, dia, hora, minuto, segundo y milisegundos actuales universalmente.
dUtc = datetime.datetime.utcnow()
print(d)

# Acceder a las diferentes partes de la fecha
t = datetime.datetime.today()
print(t.year)
print(t.month)
print(t.day)

# Establecer un formato para mostrar lo que se desee y como se desee del datetime
print(d.strftime("%d/%m/%Y  %H:%M:%S"))
print(d.strftime("%d/%m/%Y"))
print(d.strftime("%H:%M:%S"))

# TIME ZONES (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
madrid_timezone = pytz.timezone("Europe/Madrid")
madrid_time = datetime.datetime.now(madrid_timezone)
print(f"- Madrid: ", madrid_time.strftime("%d/%m/%Y  %H:%M:%S"))