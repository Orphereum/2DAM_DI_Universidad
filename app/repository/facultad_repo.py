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
    
    def get_facultad_by_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM facultad WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Facultad(id=row[0], id_universidad=row[1], id_profesor=row[2], nombre=row[3], telefono=row[4], email=row[5])
        return None

    def update_facultad(self, facultad):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE facultad
            SET id_universidad = ?, id_profesor = ?, nombre = ?, telefono = ?, email = ?
            WHERE id = ?
        """, (facultad.id_universidad, facultad.id_profesor, facultad.nombre, facultad.telefono, facultad.email, facultad.id))
        conn.commit()
        conn.close()
    
    def delete_facultad(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM facultad WHERE id = ?", (id,))
        conn.commit()
        conn.close()
    
    def get_all_facultades(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM facultad")
        rows = cursor.fetchall()
        conn.close()
        return [Facultad(id=row[0], id_universidad=row[1], id_profesor=row[2], nombre=row[3], telefono=row[4], email=row[5]) for row in rows]
    
    def get_facultades_by_universidad(self, id_universidad):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM facultad WHERE id_universidad = ?", (id_universidad,))
        rows = cursor.fetchall()
        conn.close()
        return [Facultad(id=row[0], id_universidad=row[1], id_profesor=row[2], nombre=row[3], telefono=row[4], email=row[5]) for row in rows]
    
    
    