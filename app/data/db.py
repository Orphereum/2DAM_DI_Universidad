import sqlite3
import os
import sys

def _get_db_path():
    print("DEBUG: sys.frozen =", getattr(sys, 'frozen', False))
    
    if getattr(sys, 'frozen', False):  # EXE
        base_dir = sys._MEIPASS
        print("DEBUG EXE: base_dir =", base_dir)
    else:  # DESARROLLO
        # DESDE app/data/db.py -> subir 3 niveles a RAÍZ proyecto
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        print("DEBUG DEV: base_dir =", base_dir)
    
    db_path = os.path.join(base_dir, "app", "data", "universidad.db")
    print("DEBUG: db_path =", db_path)
    return db_path

def get_connection():
    db_path = _get_db_path()
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"BD no encontrada: {db_path}")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row 
    return conn
