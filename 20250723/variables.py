from datetime import datetime


FECHA = datetime(2015, 11, 6)  # Constante

fecha_hoy = datetime.now()  # Variable que cambia

edad = fecha_hoy.year - FECHA.year

print('Edad:', edad)
print("FECHA de nacimiento:", FECHA)

x = str(3) # Convertir a string
y = int(3) # Convertir a entero
z = float(3.1)  # Convertir a float numero con decimales

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

