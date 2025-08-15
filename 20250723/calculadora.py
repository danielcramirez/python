# Mostrar el menú de opciones
print("Seleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Salir")

while True:
    # Solicitar la operación que desea realizar
    opcion = input("Ingrese el número de la operación que desea realizar: ")

    # Salir del programa
    if opcion == '5':
        print("Saliendo de la calculadora...")
        break

    # Pedir los números para la operación
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Por favor ingrese solo números.")
        continue

    # Realizar la operación según la opción seleccionada (similar a un switch)
    if opcion == '1':
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif opcion == '2':
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif opcion == '3':
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    elif opcion == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Error: División por cero no permitida.")
    else:
        print("Opción no válida. Por favor seleccione una opción válida.")
