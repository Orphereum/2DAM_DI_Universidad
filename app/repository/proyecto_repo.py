from app.data.db import get_connection
from app.models.proyecto import Proyecto

class ProyectoRepository:    
    
    def obtener_todos(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM proyecto ORDER BY nombre ASC")
        datos = cursor.fetchall()
        cursor.close()
        return datos

    def obtener_por_grupo(self, id_grupo):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT p.id_proyecto, p.nombre, p.descripcion
            FROM proyecto p
            JOIN grupoInv_proyecto gp
                ON p.id_proyecto = gp.id_proyecto
            WHERE gp.id_grupo = ?
            ORDER BY p.nombre
        """, (id_grupo,))

        datos = cursor.fetchall()
        conn.close()
        return datos
        