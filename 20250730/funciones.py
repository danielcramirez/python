#Ejemplo 1: Función sin parámetros

def saludar():
    print("¡Hola! Bienvenido a Python.")
    
# Llamamos a la función
saludar()

#Ejemplo 2: Función con parámetros

def saludar(nombre):
    print(f"¡Hola, {nombre}! Bienvenido a Python.")
    
# Llamamos a la función con un argumento
saludar("Juan")

#Ejemplo 3: Función que devuelve un valor

def sumar(a, b):
    return a + b

# Llamamos a la función y almacenamos el resultado
resultado = sumar(5, 3)
print(f"El resultado de la suma es: {resultado}")

Ejemplo 4: Función con parámetros opcionales (por defecto)
python
Copiar
def saludar(nombre="Invitado"):
    print(f"¡Hola, {nombre}! Bienvenido a Python.")
    
# Llamamos a la función sin pasar un argumento
saludar()

# Llamamos a la función pasando un argumento
saludar("Ana")
Ejemplo 5: Función con múltiples valores de retorno
python
Copiar
def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por 0"
    return suma, resta, multiplicacion, division

# Llamamos a la función y obtenemos varios resultados
s, r, m, d = operaciones(10, 2)
print(f"Suma: {s}, Resta: {r}, Multiplicación: {m}, División: {d}")