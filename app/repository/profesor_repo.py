from app.data.db import get_connection
from app.models.profesor import Profesor


class ProfesorRepository:

    #obtenemos todos los profesores
    def find_all(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_profesor, nombre, correo, telefono, titulo, id_departamento, jefe_dtp
            FROM profesor
            ORDER BY nombre
        """)

        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_model(row) for row in rows]

   
    def find_by_id(self, id_profesor): #encontrar un profesor por id
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_profesor, nombre, correo, telefono, titulo, id_departamento, jefe_dtp
            FROM profesor
            WHERE id_profesor = ?
        """, (id_profesor,))

        row = cursor.fetchone()
        conn.close()
        return self._row_to_model(row) if row else None

    # se obtiene profesores por departamento
    def find_by_departamento(self, id_departamento):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_profesor, nombre, correo, telefono, titulo, id_departamento, jefe_dtp
            FROM profesor
            WHERE id_departamento = ?
            ORDER BY nombre
        """, (id_departamento,))

        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_model(row) for row in rows]

    #  nuevo profesor
    def insert(self, profesor: Profesor):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO profesor (nombre, correo, telefono, titulo, id_departamento, jefe_dtp)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            profesor.nombre,
            profesor.correo,
            profesor.telefono,
            profesor.titulo,
            profesor.id_departamento,
            1 if profesor.jefe_dtp else 0
        ))

        conn.commit()
        profesor.id = cursor.lastrowid
        conn.close()
        return profesor

    # update d profesor existente
    def update(self, profesor: Profesor):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE profesor SET
                nombre = ?,
                correo = ?,
                telefono = ?,
                titulo = ?,
                id_departamento = ?,
                jefe_dtp = ?
            WHERE id_profesor = ?
        """, (
            profesor.nombre,
            profesor.correo,
            profesor.telefono,
            profesor.titulo,
            profesor.id_departamento,
            1 if profesor.jefe_dtp else 0,
            profesor.id
        ))

        conn.commit()
        conn.close()
        return profesor

    # se elimina un profesor por ID
    def delete(self, id_profesor):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM profesor WHERE id_profesor = ?",
            (id_profesor,)
        )

        conn.commit()
        conn.close()
        return True

    # esto para desmarcar jefes del departamento
    def desmarcar_jefes_del_departamento(self, id_departamento):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE profesor
            SET jefe_dtp = 0
            WHERE id_departamento = ?
        """, (id_departamento,))

        conn.commit()
        conn.close()
        return True

    # convertimos una fila en objeto profesor
    def _row_to_model(self, row):
        return Profesor(
            id=row[0],
            nombre=row[1],
            correo=row[2],
            telefono=row[3],
            titulo=row[4],
            id_departamento=row[5],
            jefe_dtp=bool(row[6])
        )
