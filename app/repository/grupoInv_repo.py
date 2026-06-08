from app.data.db import get_connection
from app.models.grupoInv import GrupoInvestigacion
import sqlite3


class GrupoInvRepository:

    # -------------------------
    # CONSULTAS
    # -------------------------
    def find_all(self):
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT id_grupo, nombre
                FROM grupo_investigacion
            """)

            rows = cursor.fetchall()

        return [self._row_to_model(row) for row in rows]

    def find_by_id(self, id_grupo):
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT id_grupo, nombre
                FROM grupo_investigacion
                WHERE id_grupo = ?
            """, (id_grupo,))

            row = cursor.fetchone()

        return self._row_to_model(row) if row else None

    # -------------------------
    # INSERT
    # -------------------------
    def insert(self, grupo: GrupoInvestigacion):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()

                cursor.execute("""
                    INSERT INTO grupo_investigacion (nombre)
                    VALUES (?)
                """, (grupo.nombre,))

                conn.commit()
                grupo.id_grupo = cursor.lastrowid

                return grupo

        except sqlite3.IntegrityError:
            raise ValueError("El grupo de investigación ya existe (duplicado)")

    # -------------------------
    # UPDATE
    # -------------------------
    def update(self, grupo: GrupoInvestigacion):
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE grupo_investigacion SET
                    nombre = ?
                WHERE id_grupo = ?
            """, (
                grupo.nombre,
                grupo.id_grupo
            ))

        print("UPDATE OK ID:", grupo.id_grupo)
        return grupo

    # -------------------------
    # DELETE
    # -------------------------
    def delete(self, id_grupo):
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM grupo_investigacion WHERE id_grupo = ?",
                (id_grupo,)
            )

        print("DELETE OK ID:", id_grupo)
        return True

    # -------------------------
    # UTILIDAD PRIVADA
    # -------------------------
    def _row_to_model(self, row):
        return GrupoInvestigacion(
            id_grupo=row["id_grupo"],
            nombre=row["nombre"]
        )
  
    