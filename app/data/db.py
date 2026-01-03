import sqlite3
import os


# RUTA A LA BASE DE DATOS

def _get_db_path():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "universidad.db")


# CONEXIÓN

def get_connection():
    db_path = _get_db_path()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row 
    return conn
