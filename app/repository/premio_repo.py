from app.data.db import get_connection
from app.models.premio_excelencia import PremioExcelencia

class PremioRepository:
    def find_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_premio, nombre_premio, descripcion_premio FROM premio_excelencia")
        rows = cursor.fetchall()
        conn.close()
        return [PremioExcelencia(*row) for row in rows]
    
    # ... Implementar insert, update y delete similares a asignatura_repo.py