import sqlite3
import os
import sys
import shutil

def _get_db_path():
    # Carpeta persistente del usuario
    if os.name == 'nt':  # Windows
        appdata = os.path.join(os.environ['APPDATA'], 'Gestor-Universidad')
    else:
        appdata = os.path.expanduser('~/.Gestor-Universidad')
    
    os.makedirs(appdata, exist_ok=True)
    user_db = os.path.join(appdata, 'universidad.db')
    
    # Si NO existe BD usuario, copia la inicial empaquetada
    if not os.path.exists(user_db):
        print("Primera ejecucion: Copiando BD inicial...")
        if getattr(sys, 'frozen', False):
            initial_db = os.path.join(sys._MEIPASS, 'app', 'data', 'universidad.db')
        else:
            initial_db = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'app', 'data', 'universidad.db')
        
        shutil.copy2(initial_db, user_db)
        print("BD copiada a:", user_db)
    
    return user_db

def get_connection():
    db_path = _get_db_path()
    print("Usando BD:", db_path)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row 
    return conn
