from app.data.db import get_connection
from app.models.asignatura import Asignatura


class AsignaturaRepository:

    #Funcion para leer sql
    def find_all_by_grado(self, id_grado):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_asignatura, nombre, creditos, curso,
                   cuatrimestre, obligatoria, grado_fk
            FROM asignatura
            WHERE grado_fk = ?
        """, (id_grado,))

        rows = cursor.fetchall()
        conn.close()

        return [self._row_to_model(row) for row in rows]

    def find_by_id(self, id_asignatura):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_asignatura, nombre, creditos, curso,
                   cuatrimestre, obligatoria, grado_fk
            FROM asignatura
            WHERE id_asignatura = ?
        """, (id_asignatura,))

        row = cursor.fetchone()
        conn.close()

        return self._row_to_model(row) if row else None

    # Funcion para insertar sql
    def insert(self, asignatura: Asignatura):
        conn = get_connection()
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
        conn.close()

        return asignatura

    # Funcion de actualizar 
    def update(self, asignatura: Asignatura):
        conn = get_connection()
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

        conn.commit()
        conn.close()
        return asignatura

    # Funcion para borrar
    def delete(self, id_asignatura):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM asignatura WHERE id_asignatura = ?",
            (id_asignatura,)
        )

        conn.commit()
        conn.close()
        return True

    # Funcion intermediaria encargada de convertir una fila sql (Tupla) en un objeto de el dominio Asignatura
    def _row_to_model(self, row):
        return Asignatura(
            id_asignatura=row[0],
            nombre=row[1],
            creditos=row[2],
            curso=row[3],
            cuatrimestre=row[4],
            obligatoria=bool(row[5]),
            grado_fk=row[6]
        )
