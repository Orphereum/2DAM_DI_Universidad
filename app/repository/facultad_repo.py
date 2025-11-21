import sqlite3
from app.data.db import get_connection
from app.models.facultad import Facultad

class FacultadRepo:
    def create_facultad(self, facultad):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO facultad (id_universidad, id_profesor, nombre, telefono, email)
            VALUES (?, ?, ?, ?, ?)
        """, (facultad.id_universidad, facultad.id_profesor, facultad.nombre, facultad.telefono, facultad.email))
        conn.commit()
        conn.close()