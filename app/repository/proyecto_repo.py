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

    # PARA GENERAR INFORMES
    def obtener_por_id(self, id_proyecto):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
                       SELECT p.id_proyecto, p.nombre, p.descripcion
                       FROM proyecto p
                       WHERE p.id_proyecto = ?
                       """, (id_proyecto,))
        
        proyecto = cursor.fetchone()
        cursor.close()
        conn.close()
        return proyecto         
        
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
    
    def obtener_subvenciones(self, id_proyecto):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
                    SELECT s.nombre_subvencion, ps.importe_asignado
                    FROM subvencion s
                    JOIN proyecto_subvencion ps
                        ON s.id_subvencion = ps.id_subvencion
                    WHERE ps.id_proyecto = ?
                    ORDER BY s.nombre_subvencion
                       """, (id_proyecto,))
        datos = cursor.fetchall()
        conn.close()
        return datos

    def crear_proyecto(self, nombre, descripcion, id_grupo):
        conn = get_connection()
        cursor = conn.cursor()
        
        # ----------
        # creamos nuevo poryecto y cogemos el ultimo id, que es el último creado
        cursor.execute("""
                       INSERT INTO proyecto (nombre, descripcion) 
                       VALUES (?,?)
                       """, (nombre, descripcion))
        nuevo_id_proyecto = cursor.lastrowid
        
        # ----------
        # creamos relacion entre nuevo proyecto y el grupoInv seleccionado
        cursor.execute("""
                       INSERT INTO grupoInv_proyecto (id_grupo, id_proyecto, fecha_inicio)
                       VALUES (?,?, DATE('now'))
                       """, (id_grupo, nuevo_id_proyecto)) # PONER FEHCA INICION Y ALOMEJOR TMB LA DE FIN
        conn.commit()
        cursor.close()
        
        return nuevo_id_proyecto
    
    # busca los proyectos asociados al grupo y los devuelve
    def obtener_por_grupo(self, id_grupo):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT p.id_proyecto, p.nombre, p.descripcion
            FROM proyecto p
            JOIN grupoInv_proyecto gp 
                ON p.id_proyecto = gp.id_proyecto
            WHERE gp.id_grupo = ?
        """, (id_grupo,))

        datos = cursor.fetchall()
        conn.close()
        return datos
    
    def actualizar_proyecto(self, id_proyecto, nombre, descripcion):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
                       UPDATE proyecto
                       SET nombre = ?, descripcion = ?
                       WHERE id_proyecto = ?
                       """, (nombre, descripcion, id_proyecto))
        
        conn.commit()
        conn.close()
    
    def eliminar_proyecto(self, id_proyecto):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
                       DELETE FROM proyecto 
                       WHERE id_proyecto = ?
                       """, (id_proyecto,)) # cuando va solo UNA VARIABLE se escribe despues de esta ',' para que interprete que es un TUPLA y no un tipo (int), por ejemplo 
        
        conn.commit()
        conn.close()