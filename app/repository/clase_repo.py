from app.data.db import get_connection
from app.models.clase import Clase

class ClaseRepository:
    
    def find_all(self):
        """Obtiene todas las clases (o podrías filtrar por edificio)"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_clase, nombre, capacidad, id_edificio FROM clase")
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_model(row) for row in rows]

    def find_by_id(self, id_clase):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_clase, nombre, capacidad, id_edificio FROM clase WHERE id_clase = ?", (id_clase,))
        row = cursor.fetchone()
        conn.close()
        return self._row_to_model(row) if row else None

    def insert(self, clase: Clase):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO clase (nombre, capacidad, id_edificio)
            VALUES (?, ?, ?)
        """, clase.to_tuple())
        conn.commit()
        clase.id_clase = cursor.lastrowid
        conn.close()
        return clase

    def update(self, clase: Clase):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE clase SET nombre = ?, capacidad = ?, id_edificio = ?
            WHERE id_clase = ?
        """, (clase.nombre, clase.capacidad, clase.id_edificio, clase.id_clase))
        conn.commit()
        conn.close()
        return clase

    def delete(self, id_clase):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clase WHERE id_clase = ?", (id_clase,))
        conn.commit()
        conn.close()
        return True

    def _row_to_model(self, row):
        return Clase(id_clase=row[0], nombre=row[1], capacidad=row[2], id_edificio=row[3])