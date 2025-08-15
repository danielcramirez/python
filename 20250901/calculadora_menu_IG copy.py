import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Organización de Widgets")

# Panel vertical (uno debajo del otro)
frame_vertical = tk.Frame(ventana)
frame_vertical.pack(side="top", fill="x", pady=10)

label1 = tk.Label(frame_vertical, text="Etiqueta 1")
label1.pack(side="top", pady=5)

label2 = tk.Label(frame_vertical, text="Etiqueta 2")
label2.pack(side="top", pady=5)

label3 = tk.Label(frame_vertical, text="Etiqueta 3")
label3.pack(side="top", pady=5)

# Panel horizontal (de izquierda a derecha)
frame_horizontal = tk.Frame(ventana)
frame_horizontal.pack(side="top", fill="x", pady=10)

button1 = tk.Button(frame_horizontal, text="Botón 1")
button1.pack(side="left", padx=10)

button2 = tk.Button(frame_horizontal, text="Botón 2")
button2.pack(side="left", padx=5)

button3 = tk.Button(frame_horizontal, text="Botón 3")
button3.pack(side="left", padx=5)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
