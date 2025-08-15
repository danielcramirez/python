#crear arreglo para almacenar las notas
notas = []

#ingresar notas

for i in range(5):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)

print("Notas ingresadas:", notas)   

suma = sum(notas)
print("Suma de las notas:", suma)

promedio = suma / len(notas)
print("Promedio de las notas:", promedio)

