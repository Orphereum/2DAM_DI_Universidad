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

    def obtener_todos(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM subvencion")
        datos = cursor.fetchall()

        conn.close()
        return datos

    def crear_subvencion(self, nombre, importe_min, importe_max, fecha_inicio, fecha_fin, estado):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO subvencion (nombre_subvencion, importe_minimo, importe_maximo, fecha_inicio, fecha_final, estado_subvencion)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre, importe_min, importe_max, fecha_inicio, fecha_fin, estado))

        conn.commit()
        nuevo_id = cursor.lastrowid
        conn.close()

        return nuevo_id

    def actualizar_subvencion(self, id_subvencion, nombre, importe_min, importe_max, fecha_inicio, fecha_fin, estado):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE subvencion
            SET nombre_subvencion=?, importe_minimo=?, importe_maximo=?, fecha_inicio=?, fecha_final=?, estado_subvencion=?
            WHERE id_subvencion=?
        """, (nombre, importe_min, importe_max, fecha_inicio, fecha_fin, estado, id_subvencion))

        conn.commit()
        conn.close()

    def eliminar_subvencion(self, id_subvencion):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM subvencion WHERE id_subvencion=?", (id_subvencion,))

        conn.commit()
        conn.close()
