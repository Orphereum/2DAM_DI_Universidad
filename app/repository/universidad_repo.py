# app/repository/universidad_repo.py
from app.data.db import get_connection

class UniversidadRepository:
    
    def obtener_todas(self):
        """Recupera la lista de todas las universidades registradas en orden alfabético."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_universidad, nombre FROM universidad ORDER BY nombre ASC")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return datos

    def obtener_por_id(self, id_universidad):
        """Busca una única universidad por su identificador único."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_universidad, nombre 
            FROM universidad 
            WHERE id_universidad = ?
        """, (id_universidad,))
        universidad = cursor.fetchone()
        cursor.close()
        conn.close()
        return universidad

    def crear_universidad(self, nombre):
        """Inserta una nueva universidad en el sistema."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO universidad (nombre) 
            VALUES (?)
        """, (nombre,))
        nuevo_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return nuevo_id

    def actualizar_universidad(self, id_universidad, nombre):
        """Modifica el nombre de una universidad existente."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE universidad 
            SET nombre = ? 
            WHERE id_universidad = ?
        """, (nombre, id_universidad))
        conn.commit()
        cursor.close()
        conn.close()

    def eliminar_universidad(self, id_universidad):
        """
        Elimina de la base de datos una universidad.
        Nota: Al igual que indicas en tu código, al ir solo una variable ponemos la ','
        después de id_universidad para forzar la estructura de tupla en Python.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM universidad 
            WHERE id_universidad = ?
        """, (id_universidad,))
        conn.commit()
        cursor.close()
        conn.close()

    def obtener_facultades_por_universidad(self, id_universidad):
        """Recupera las facultades vinculadas de forma relacional a una universidad."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_facultad, nombre, telefono, email
            FROM facultad
            WHERE id_universidad = ?
            ORDER BY nombre ASC
        """, (id_universidad,))
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return datos

    # ==========================================================
    # MÉTODO ESPECIALIZADO PARA EL REPORTE PDF DE JAIME PONCE
    # ==========================================================
    def obtener_todo_para_reporte(self):
        """
        Construye la estructura jerárquica exacta mapeando universidades 
        y coleccionando sus facultades para alimentar al Generador de Informes.
        """
        # 1. Obtenemos todas las universidades
        universidades_db = self.obtener_todas()
        estructura_reporte = []
        
        # 2. Mapeamos cada una buscando sus dependencias relacionales
        for univ in universidades_db:
            # Soportamos tanto acceso por clave (dict) como por índice (tupla) según config del cursor
            try:
                id_u = univ["id_universidad"]
                nom_u = univ["nombre"]
            except TypeError:
                id_u = univ[0]
                nom_u = univ[1]
                
            facultades_db = self.obtener_facultades_por_universidad(id_u)
            lista_facultades = []
            
            for fac in facultades_db:
                try:
                    lista_facultades.append({
                        "id_facultad": fac["id_facultad"],
                        "nombre": fac["nombre"],
                        "telefono": fac["telefono"]
                    })
                except TypeError:
                    lista_facultades.append({
                        "id_facultad": fac[0],
                        "nombre": fac[1],
                        "telefono": fac[2]
                    })
            
            # Formateamos el diccionario final que procesará ReportLab
            estructura_reporte.append({
                "nombre": nom_u,
                "facultades": lista_facultades
            })
            
        return estructura_reporte