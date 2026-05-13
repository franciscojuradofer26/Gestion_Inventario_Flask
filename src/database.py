import os
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# src/ -> subir un nivel -> data/inventario.db
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_DB_PATH = os.path.join(_BASE_DIR, "..", "data", "inventario.db")

def conectar():
    os.makedirs(os.path.dirname(_DB_PATH), exist_ok=True)
    return sqlite3.connect(_DB_PATH)

def inicializar_DB():
    con = conectar()
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS productos(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, cantidad INT)")
    cur.execute("CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre_usu TEXT UNIQUE, contrasena TEXT)")
    con.commit()
    con.close()

def insertar_producto(nombre, cantidad):
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO productos(nombre, cantidad) VALUES(?,?)", (nombre, cantidad))
        con.commit()
    except sqlite3.Error as e:
        print(f"Error al insertar el producto: {e}")
    finally:
        con.close()

def productos():
    try:
        con = conectar()
        cur = con.cursor()
        lista = cur.execute("SELECT * FROM productos").fetchall()
        return lista
    except sqlite3.Error as e:
        print(f"Error al extraer los productos: {e}")
        return []
    finally:
        con.close()

def eliminar_producto(id):
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("DELETE FROM productos WHERE id=?", (id,))
        con.commit()
    except sqlite3.Error as e:
        print(f"Error al eliminar el producto: {e}")
    finally:
        con.close()

def registrar_usuario(username, password):
    try:
        con = conectar()
        cur = con.cursor()
        hash_pwd = generate_password_hash(password)
        cur.execute("INSERT INTO usuarios(nombre_usu, contrasena) VALUES(?,?)", (username, hash_pwd))
        con.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        con.close()

def verificar_login(username, password):
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT contrasena FROM usuarios WHERE nombre_usu=?", (username,))
        resultado = cur.fetchone()
        if resultado:
            return check_password_hash(resultado[0], password)
        return False
    except sqlite3.Error as e:
        print(f"Error al verificar el login: {e}")
        return False
    finally:
        con.close()
