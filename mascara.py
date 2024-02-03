from flask import Flask, request, render_template_string # Importar Flask para crear la aplicación web,  y request para manejar solicitudes HTTP y render_template_string para renderizar plantillas
import sqlite3

app = Flask(__name__) # Crear una aplicación de Flask

# Ruta para la página de inicio
@app.route('/') # Decorador para indicar la ruta de la página
def index():
    """
    Página de inicio con un formulario para realizar búsquedas en el censo.
    """
    return render_template_string('''
        <h1>Búsqueda en el Censo</h1>
        <form action="/buscar" method="post">
            <label for="tipo">Buscar por:</label>
            <select name="tipo" id="tipo">
                <option value="numero">Número</option>
                <option value="nombre">Nombre</option>
            </select>
            <label for="valor">Valor:</label>
            <input type="text" name="valor" id="valor" required>
            <button type="submit">Buscar</button>
        </form>
    ''')