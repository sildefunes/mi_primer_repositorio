#hoja nueva de ruteo
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/formulario', methods=['GET', 'POST'])
def formulario(): 
    if request.method == 'POST':
        nombre = request.form['nombre']
        return f'Tu nombre es {nombre}'
    return render_template('formulario.html')

if __name__=="__main__":
    app.run(debug=True)


