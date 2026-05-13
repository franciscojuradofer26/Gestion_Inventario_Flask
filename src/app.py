import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session
import database
import verify

load_dotenv()

app = Flask(__name__)  # Flask busca templates/ y static/ dentro de src/ automáticamente
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SESSION_PERMANENT'] = False  # La sesión se borra al cerrar el navegador

# Inicializa la BD y crea el usuario admin si no existe
database.inicializar_DB()
database.registrar_usuario("admin", "1234")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if database.verificar_login(username, password):
            session.permanent = False
            session['usuario'] = username
            return redirect(url_for('index'))
        else:
            error = "Usuario o contraseña incorrectos"

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    productos_db = database.productos()
    return render_template('index.html', productos=productos_db)

@app.route('/nuevo', methods=['POST'])
def nuevo_producto():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    nombre = request.form.get('nombre')
    try:
        cantidad = int(request.form.get('cantidad'))
    except (ValueError, TypeError):
        cantidad = 0

    if verify.verificar_producto(nombre, cantidad):
        database.insertar_producto(nombre, cantidad)

    return redirect(url_for('index'))

@app.route('/eliminar/<int:id_prod>')
def borrar(id_prod):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    if verify.verificar_ID(id_prod):
        database.eliminar_producto(id_prod)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
