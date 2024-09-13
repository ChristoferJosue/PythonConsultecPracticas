# db_manager.py
import sqlite3
import json

DB_FILE = "colaboradores.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS colaboradores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            correo TEXT,
            contraseña TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(correo, contrasena):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO colaboradores (correo, contraseña) VALUES (?, ?)', (correo, contrasena))
    conn.commit()
    conn.close()


def obtener_usuarios():
    conexion = sqlite3.connect('colaboradores.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM colaboradores")
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()
    return usuarios