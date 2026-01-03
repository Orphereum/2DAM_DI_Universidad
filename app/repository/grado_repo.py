import sqlite3
from data.db import get_connection
from models.grado import Grado


class GradoRepository:

    # CONSULTAS

    def find_all_by_facultad(self, id_facultad):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_grado, nombre, codigo, duracion_anios,
                   creditos_totales, tipo, estado, fecha_creacion, id_facultad
            FROM grado
            WHERE id_facultad = ?
        """, (id_facultad,))

        rows = cursor.fetchall()
        conn.close()

        grados = []
        for row in rows:
            grados.append(self._row_to_grado(row))

        return grados

    def find_by_id(self, id_grado):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_grado, nombre, codigo, duracion_anios,
                   creditos_totales, tipo, estado, fecha_creacion, id_facultad
            FROM grado
            WHERE id_grado = ?
        """, (id_grado,))

        row = cursor.fetchone()
        conn.close()

        if row:
            return self._row_to_grado(row)
        return None


    # INSERT

    def insert(self, grado: Grado):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO grado (
                nombre, codigo, duracion_anios,
                creditos_totales, tipo, estado,
                fecha_creacion, id_facultad
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            grado.nombre,
            grado.codigo,
            grado.duracion_anios,
            grado.creditos_totales,
            grado.tipo,
            grado.estado,
            grado.fecha_creacion,
            grado.id_facultad
        ))

        conn.commit()
        grado.id_grado = cursor.lastrowid
        conn.close()

        return grado

    
    # UPDATE

    def update(self, grado: Grado):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE grado SET
                nombre = ?,
                codigo = ?,
                duracion_anios = ?,
                creditos_totales = ?,
                tipo = ?,
                estado = ?,
                fecha_creacion = ?,
                id_facultad = ?
            WHERE id_grado = ?
        """, (
            grado.nombre,
            grado.codigo,
            grado.duracion_anios,
            grado.creditos_totales,
            grado.tipo,
            grado.estado,
            grado.fecha_creacion,
            grado.id_facultad,
            grado.id_grado
        ))

        conn.commit()
        conn.close()

        return grado


    # DELETE


    def delete(self, id_grado):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM grado WHERE id_grado = ?",
            (id_grado,)
        )

        conn.commit()
        conn.close()

        return True

  
    # UTILIDAD PRIVADA

    def _row_to_grado(self, row):
        return Grado(
            id_grado=row[0],
            nombre=row[1],
            codigo=row[2],
            duracion_anios=row[3],
            creditos_totales=row[4],
            tipo=row[5],
            estado=row[6],
            fecha_creacion=row[7],
            id_facultad=row[8]
        )
