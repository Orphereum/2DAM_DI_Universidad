from app.data.db import get_connection
from app.models.grupoInv import GrupoInvestigacion

class GrupoInvRepository:
    
    def cargar_lista_gruposInv(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT g.id_grupo, g.nombre FROM grupo_investigacion g")
        datos = cursor.fetchall()
        cursor.close()
        return datos
    