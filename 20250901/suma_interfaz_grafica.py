import tkinter as tk
from tkinter import messagebox

def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

ventana = tk.Tk()
ventana.title("Suma de Dos Números")

label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack()

entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack()

entry_num2 = tk.Entry(ventana)
entry_num2.pack()

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack()

label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack()

ventana.mainloop()