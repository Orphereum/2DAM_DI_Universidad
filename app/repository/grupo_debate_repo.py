from app.data.db import get_connection
from app.models.grupo_debate import GrupoDebate


class GrupoDebateRepository:

    def obtener_todos(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM grupo_debate")

        datos = cursor.fetchall()

        conn.close()

        return datos

    def crear_grupo(
        self,
        nombre,
        tema_principal,
        descripcion,
        fecha_inicio,
        estado
    ):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO grupo_debate
            (
                nombre,
                tema_principal,
                descripcion,
                fecha_inicio,
                estado
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            nombre,
            tema_principal,
            descripcion,
            fecha_inicio,
            estado
        ))

        conn.commit()

        nuevo_id = cursor.lastrowid

        conn.close()

        return nuevo_id

    def actualizar_grupo(
        self,
        id_grupo,
        nombre,
        tema_principal,
        descripcion,
        fecha_inicio,
        estado
    ):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE grupo_debate
            SET nombre=?,
                tema_principal=?,
                descripcion=?,
                fecha_inicio=?,
                estado=?
            WHERE id_grupo=?
        """, (
            nombre,
            tema_principal,
            descripcion,
            fecha_inicio,
            estado,
            id_grupo
        ))

        conn.commit()

        conn.close()

    def eliminar_grupo(self, id_grupo):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM grupo_debate
            WHERE id_grupo=?
        """, (id_grupo,))

        conn.commit()

        conn.close()