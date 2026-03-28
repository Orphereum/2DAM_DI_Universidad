import sqlite3

from app.data.db import get_connection
from app.models.asignatura import Asignatura


class AsignaturaRepository:

    # -------------------------
    # CONSULTAS
    # -------------------------
    def find_all_by_grado(self, id_grado):
        print("BUSCANDO EN BD PARA GRADO:", id_grado)

        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT id_asignatura, nombre, creditos, curso,
                       cuatrimestre, obligatoria, grado_fk
                FROM asignatura
                WHERE grado_fk = ?
            """, (id_grado,))

            rows = cursor.fetchall()
            print("RESULTADOS EN BD:", len(rows))

        return [self._row_to_model(row) for row in rows]

    def find_by_id(self, id_asignatura):
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT id_asignatura, nombre, creditos, curso,
                       cuatrimestre, obligatoria, grado_fk
                FROM asignatura
                WHERE id_asignatura = ?
            """, (id_asignatura,))

            row = cursor.fetchone()

        return self._row_to_model(row) if row else None

    # -------------------------
    # INSERT
    # -------------------------
    import sqlite3

    def insert(self, asignatura):
     try:
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO asignatura
                (nombre, creditos, curso, cuatrimestre, obligatoria, grado_fk)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                asignatura.nombre,
                asignatura.creditos,
                asignatura.curso,
                asignatura.cuatrimestre,
                asignatura.obligatoria,
                asignatura.grado_fk
            ))

            conn.commit()
            asignatura.id_asignatura = cursor.lastrowid

            return asignatura

     except sqlite3.IntegrityError:
        raise ValueError("La asignatura ya existe (duplicada)")

    # -------------------------
    # UPDATE
    # -------------------------
    def update(self, asignatura: Asignatura):
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE asignatura SET
                    nombre = ?,
                    creditos = ?,
                    curso = ?,
                    cuatrimestre = ?,
                    obligatoria = ?,
                    grado_fk = ?
                WHERE id_asignatura = ?
            """, (
                asignatura.nombre,
                asignatura.creditos,
                asignatura.curso,
                asignatura.cuatrimestre,
                asignatura.obligatoria,
                asignatura.grado_fk,
                asignatura.id_asignatura
            ))

        print("UPDATE OK ID:", asignatura.id_asignatura)
        return asignatura

    # -------------------------
    # DELETE
    # -------------------------
    def delete(self, id_asignatura):
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM asignatura WHERE id_asignatura = ?",
                (id_asignatura,)
            )

        print("DELETE OK ID:", id_asignatura)
        return True

    # -------------------------
    # UTILIDAD PRIVADA
    # -------------------------
    def _row_to_model(self, row):
        return Asignatura(
            id_asignatura=row["id_asignatura"],
            nombre=row["nombre"],
            creditos=row["creditos"],
            curso=row["curso"],
            cuatrimestre=row["cuatrimestre"],
            obligatoria=bool(row["obligatoria"]),
            grado_fk=row["grado_fk"]
        )
    
    
    def find_filtradas(self, id_grado, curso, cuatrimestre, tipo):
     query = """
        SELECT id_asignatura, nombre, creditos, curso,
               cuatrimestre, obligatoria, grado_fk
        FROM asignatura
        WHERE grado_fk = ?
     """

     params = [id_grado]

    # FILTRO CURSO
     if curso != "Todos":
        query += " AND curso = ?"
        params.append(int(curso))

    # FILTRO CUATRIMESTRE
     if cuatrimestre != "Todos":
        query += " AND cuatrimestre = ?"
        params.append(int(cuatrimestre))

    # FILTRO TIPO (🔥 CORRECTO)
     if tipo is not None:
        query += " AND obligatoria = ?"
        params.append(tipo)

     with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()

     return [self._row_to_model(row) for row in rows]