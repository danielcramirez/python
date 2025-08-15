print("daniel felipe ramirez vargas")
print("daniel camilo ramirez martinez")
print(2 + 2)


from datetime import datetime
 
FECHA = datetime(1985, 9, 18) # Constante
 
fecha_hoy = datetime.now() # variable que cambia
 
edad = fecha_hoy.year - FECHA.year
 
print("edad:", edad)
print("fecha de nacimiento:", FECHA)