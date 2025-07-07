

# 1. Importar gestión de claves y SQLite
from flask import Flask, request, render_template_string
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# 2. Crear aplicación Flask en puerto 5800
app = Flask(__name__)

# 3. Crear base de datos y tabla de usuarios
def init_db():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# 4. Ruta principal para registrar usuarios
@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = ""
    if request.method == "POST":
        nombre = request.form["nombre"]
        password = request.form["password"]
        password_hash = generate_password_hash(password)

        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)", (nombre, password_hash))
        conn.commit()
        conn.close()
        mensaje = "Usuario registrado exitosamente."

    return render_template_string('''
        <h2>Registro de usuarios</h2>
        <form method="post">
            Nombre: <input type="text" name="nombre"><br>
            Contraseña: <input type="password" name="password"><br>
            <input type="submit" value="Registrar">
        </form>
        <p>{{ mensaje }}</p>
    ''', mensaje=mensaje)

# 5. Ruta para validación de usuarios
@app.route("/login", methods=["GET", "POST"])
def login():
    mensaje = ""
    if request.method == "POST":
        nombre = request.form["nombre"]
        password = request.form["password"]

        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM usuarios WHERE nombre = ?", (nombre,))
        resultado = cursor.fetchone()
        conn.close()

        if resultado and check_password_hash(resultado[0], password):
            mensaje = "Acceso concedido."
        else:
            mensaje = "Usuario o contraseña incorrectos."

    return render_template_string('''
        <h2>Login de usuarios</h2>
        <form method="post">
            Nombre: <input type="text" name="nombre"><br>
            Contraseña: <input type="password" name="password"><br>
            <input type="submit" value="Ingresar">
        </form>
        <p>{{ mensaje }}</p>
    ''', mensaje=mensaje)

# 6. Ejecutar la app en el puerto 5800
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5800)
