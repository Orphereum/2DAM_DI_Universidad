from app.data.db import get_connection
from app.models.edificio import Edificio


class EdificioRepository:

    #Obtiene todos los edificios de la base de datos
    def find_all(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_edificio, nombre, id_facultad
            FROM edificio
            ORDER BY nombre
        """)

        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_model(row) for row in rows]



    #Busca un edificio por su ID
    def find_by_id(self, id_edificio):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_edificio, nombre, id_facultad
            FROM edificio
            WHERE id_edificio = ?
        """, (id_edificio,))

        row = cursor.fetchone()
        conn.close()
        return self._row_to_model(row) if row else None



    #Obtiene todos los edificios de una facultad
    def find_by_facultad(self, id_facultad):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_edificio, nombre, id_facultad
            FROM edificio
            WHERE id_facultad = ?
            ORDER BY nombre
        """, (id_facultad,))

        rows = cursor.fetchall()
        conn.close()

        return [self._row_to_model(row) for row in rows]



    #Inserta un nuevo edificio en la base de datos
    def insert(self, edificio: Edificio):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO edificio (nombre, id_facultad)
            VALUES (?, ?)
        """, (
            edificio.nombre,
            edificio.id_facultad
        ))

        conn.commit()
        edificio.id = cursor.lastrowid
        conn.close()

        return edificio



    #Actualiza un edificio existente
    def update(self, edificio: Edificio):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE edificio SET
                nombre = ?,
                id_facultad = ?
            WHERE id_edificio = ?
        """, (
            edificio.nombre,
            edificio.id_facultad,
            edificio.id
        ))

        conn.commit()
        conn.close()
        return edificio



    #Elimina un edificio por su ID
    def delete(self, id_edificio):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM edificio WHERE id_edificio = ?",
            (id_edificio,)
        )

        conn.commit()
        conn.close()
        return True



    #Convierte una fila de la base de datos en un objeto Edificio
    def _row_to_model(self, row):
        return Edificio(
            id=row[0],
            nombre=row[1],
            id_facultad=row[2]
        )