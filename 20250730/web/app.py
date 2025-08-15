from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def suma():
    resultado = None
    if request.method == 'POST':
        # Intentamos convertir los valores de entrada a float
        try:
            # Obtenemos los números del formulario
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            resultado = num1 + num2
        except (ValueError, TypeError):
            resultado = "Error: Entrada no válida"
    return render_template('suma.html', resultado=resultado)
if __name__ == '__main__':
    app.run(debug=True)