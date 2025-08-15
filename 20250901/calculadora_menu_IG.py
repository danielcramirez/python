import tkinter as tk
from tkinter import messagebox

#Funicion para la operacion
def cacular():
    try:
        num1 = float(entry_num1.get()) #Obtiene el valor de la primera entrada
        num2 = float(entry_num2.get()) #Obtiene el valor de la segunda entrada
        operacion = operacion_var.get() #Obtiene la operacion seleccionada desde el radio button
        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            if num2 == 0:
                raise ValueError("No se puede dividir por cero.")
            resultado = num1 / num2
        else:
            pass
        label_resultado.config(text=f"Resultado: {resultado}") #Actualiza el label con el resultado

    except ValueError:
        label_resultado.config(text="Error: Ingrese números válidos.") #Muestra un mensaje de error si hay un problema con la entrada

#crear la interfaz grafica
ventana = tk.Tk()
ventana.title("Calculadora")

#Etiquetas y entradas para los números
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack()
entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack()
entry_num2 = tk.Entry(ventana)
entry_num2.pack()

# Variable para la operación seleccionada
operacion_var = tk.StringVar(value="suma")

#crear el radio butto para el menu
frame_horizontal = tk.Frame(ventana)
frame_horizontal.pack(side="top", fill="x", pady=10)
radio_suma = tk.Radiobutton(frame_horizontal, text="Suma", variable=operacion_var, value="suma")
radio_suma.pack(side="left", padx=10)
radio_resta = tk.Radiobutton(frame_horizontal, text="Resta", variable=operacion_var, value="resta") 
radio_resta.pack(side="left", padx=10)
radio_multiplicacion = tk.Radiobutton(frame_horizontal, text="Multiplicación", variable=operacion_var, value="multiplicacion")
radio_multiplicacion.pack(side="left", padx=10)
radio_division = tk.Radiobutton(frame_horizontal, text="División", variable=operacion_var, value="division")
radio_division.pack(side="left", padx=10)

# Botón para calcular
button_calcular = tk.Button(ventana, text="Calcular", command=cacular)
button_calcular.pack()

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()