operacion = str(input("Ingresa la operación (suma/resta): "))
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if operacion == 'suma':
    resultado = num1 + num2
    print(f" la operacion es {num1} + {num2} = {resultado}")
elif operacion == 'resta':
    resultado = num1 - num2
    print(f" la operacion es {num1} - {num2} = {resultado}")
else:
    print("Operación no válida. Por favor, ingrese 'suma' o 'resta'.")