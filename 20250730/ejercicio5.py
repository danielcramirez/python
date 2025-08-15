# Paso 1: Inicializar la variable para almacenar la suma
suma = 0

# Paso 2: Usar un ciclo while para pedir al usuario un número y sumar los valores positivos
while True:
    numero = int(input("Ingresa un número positivo o un negativo): "))
    
    # Paso 3: Si el número ingresado es negativo, terminar el ciclo
    if numero < 0:
        break
    
    suma += numero  # Sumar el número positivo

# Mostrar la suma total de los números positivos
print("La suma total de los números positivos es:", suma)
