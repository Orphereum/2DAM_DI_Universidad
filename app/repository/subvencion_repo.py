from app.data.db import get_connection
from app.models.subvencion import Subvencion

class SubvencionRepository:
    print("subvencion")
    # PARA GENERAR INFORMES
    def obtener_por_proyecto(self, id_proyecto):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
                       SELECT s.id_subvencion, s.nombre_subvencion, ps.importe_asignado
                       FROM subvencion s
                        JOIN proyecto_subvencion ps
                            ON s.id_subvencion = ps.id_subvencion
                        WHERE ps.id_proyecto = ?
                       """, (id_proyecto,))
        
        subvenciones = cursor.fetchall()
        cursor.close()
        conn.close()
        return subvenciones