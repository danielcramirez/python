def sumar (a, b):
    return a + b
def restar (a, b):
    return a - b
def multiplicar (a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b
def main():
    print("calculadora basica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    opcion = input("Seleccione una operación (1 o 2): ")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if opcion == "1":
        resultado = sumar(num1, num2)
        print(f"La suma de {num1} y {num2} es: {resultado}")
    elif opcion == "2":
        resultado = restar(num1, num2)
        print(f"La resta de {num1} y {num2} es: {resultado}")
    elif opcion == "3":
        resultado = multiplicar(num1, num2)
        print(f"La multiplicación de {num1} y {num2} es: {resultado}")
    elif opcion == "4":
        resultado = dividir(num1, num2)
        print(f"La división de {num1} y {num2} es: {resultado}")
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.") 
    
if __name__ == "__main__":
    main()