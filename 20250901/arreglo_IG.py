import tkinter as tk  # Importa la biblioteca tkinter para crear la interfaz gráfica
from tkinter import messagebox  # Importa el módulo messagebox para mostrar mensajes de error

def notas():
    try:
        # Se obtienen las notas ingresadas por el usuario y se convierten a tipo float
        notas = [float(entry_nota1.get()), float(entry_nota2.get()),
                 float(entry_nota3.get()), float(entry_nota4.get()),
                 float(entry_nota5.get())]
        
        # Calcula la suma de las notas
        suma = sum(notas)
        
        # Calcula el promedio de las notas
        promedio = suma / len(notas)
        
        # Calcula la nota máxima
        maximo = max(notas)
        
        # Calcula la nota mínima
        minimo = min(notas)
        
        # Muestra los resultados en la interfaz
        label_resultado.config(text=f"Suma: {suma}, Promedio: {promedio}, Máximo: {maximo}, Mínimo: {minimo}")
    
    except ValueError:  # Si el usuario ingresa algo que no es un número, muestra un mensaje de error
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

# Crea la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Notas")  # Título de la ventana

# Etiqueta con instrucciones para el usuario
label_instrucciones = tk.Label(ventana, text="Ingrese los 5 números:")
label_instrucciones.pack(pady=10)  # La etiqueta tiene un espaciado vertical de 10 píxeles

# Etiquetas y campos de entrada para cada una de las 5 notas
label_nota1 = tk.Label(ventana, text="Nota 1:")
label_nota1.pack()  # Se muestra la etiqueta
entry_nota1 = tk.Entry(ventana)  # Campo para que el usuario ingrese la nota
entry_nota1.pack()  # El campo se muestra en la ventana

label_nota2 = tk.Label(ventana, text="Nota 2:")
label_nota2.pack()
entry_nota2 = tk.Entry(ventana)
entry_nota2.pack()

label_nota3 = tk.Label(ventana, text="Nota 3:")
label_nota3.pack()
entry_nota3 = tk.Entry(ventana)
entry_nota3.pack()

label_nota4 = tk.Label(ventana, text="Nota 4:")
label_nota4.pack()
entry_nota4 = tk.Entry(ventana)
entry_nota4.pack()

label_nota5 = tk.Label(ventana, text="Nota 5:")
label_nota5.pack()
entry_nota5 = tk.Entry(ventana)
entry_nota5.pack()

# Botón para calcular las operaciones
button_calcular = tk.Button(ventana, text="Calcular", command=notas)
button_calcular.pack(pady=10)  # El botón tiene un espaciado vertical de 10 píxeles

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack(pady=10)  # La etiqueta tiene un espaciado vertical de 10 píxeles

# Inicia el bucle principal de la interfaz gráfica
ventana.mainloop()
