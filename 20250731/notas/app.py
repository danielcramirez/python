from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def promedio():
    promedio_notas = None
    if request.method == 'POST':  # Corregir de 'post' a 'POST'
        # Intentamos convertir los valores de entrada a float
        try:
            # Obtenemos los números del formulario
            nota1 = float(request.form['n1'])
            nota2 = float(request.form['n2'])
            nota3 = float(request.form['n3'])
            promedio_notas = (nota1 + nota2 + nota3) / 3
        except (ValueError, TypeError):
            promedio_notas = "Error: Entrada no válida"
    return render_template('notas_sb.html', promedio_notas=promedio_notas)

if __name__ == '__main__':
    app.run(debug=True)
