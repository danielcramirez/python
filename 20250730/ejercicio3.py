inicio = int(input("Ingrese el valor de inicio: "))
fin = int(input("Ingrese el valor de fin: "))
contador = 0
for i in range(inicio, fin + 1):
    if (i % 3) == 0:
        print(i, "Si es Divisible entre 3")
        contador += 1
    else:
        print(i, "No es Divisible entre 3")
print("Total de números divisibles entre 3:", contador)