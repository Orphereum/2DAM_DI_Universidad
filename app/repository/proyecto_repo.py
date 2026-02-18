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

    
        