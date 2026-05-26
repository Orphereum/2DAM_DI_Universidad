from app.data.db import get_connection
from app.models.premio_excelencia import PremioExcelencia

class PremioRepository:
    def find_all(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_premio, nombre_premio, descripcion_premio FROM premio_excelencia")
            rows = cursor.fetchall()
        return [PremioExcelencia(*row) for row in rows]

    def find_by_id(self, id_premio):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_premio, nombre_premio, descripcion_premio FROM premio_excelencia WHERE id_premio = ?",
                (id_premio,)
            )
            row = cursor.fetchone()
        return PremioExcelencia(*row) if row else None

    def insert(self, premio):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO premio_excelencia (nombre_premio, descripcion_premio) VALUES (?, ?)",
                (premio.nombre_premio, premio.descripcion_premio)
            )
            conn.commit()
            premio.id_premio = cursor.lastrowid
        return premio

    def update(self, premio):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE premio_excelencia SET nombre_premio = ?, descripcion_premio = ? WHERE id_premio = ?",
                (premio.nombre_premio, premio.descripcion_premio, premio.id_premio)
            )
            conn.commit()
        return premio

    def delete(self, id_premio):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM premio_excelencia WHERE id_premio = ?",
                (id_premio,)
            )
            conn.commit()
        return True