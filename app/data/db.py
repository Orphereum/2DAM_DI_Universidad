import sqlite3
import os


# RUTA A LA BASE DE DATOS (app/universidad.db)

def _get_db_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))  
    # __file__ ya está dentro de app/
    db_path = os.path.join(base_dir, "universidad.db")
    return db_path


# CONEXIÓN

def get_connection():
    db_path = _get_db_path()
    print("Usando BD:", db_path)

    # 🚨 Si no existe, NO queremos que la cree
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"No existe la base de datos en: {db_path}")

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn
