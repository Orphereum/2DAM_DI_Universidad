from app.data.db import get_connection


class PublicacionRepository:
    def __init__(self):
        self._ensure_tables()

    def _ensure_tables(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS grupo_debate (
                id_grupo INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                tema_principal TEXT,
                descripcion TEXT,
                fecha_inicio TEXT,
                estado TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publicacion (
                id_publicacion INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                fecha_publicacion TEXT,
                tipo TEXT,
                id_grupoDebate INTEGER,
                FOREIGN KEY (id_grupoDebate) REFERENCES grupo_debate(id_grupo)
            )
        """)

        conn.commit()
        conn.close()

    def obtener_todos(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                p.id_publicacion,
                p.titulo,
                p.descripcion,
                p.fecha_publicacion,
                p.tipo,
                p.id_grupoDebate,
                COALESCE(g.nombre, 'Sin grupo') AS grupo_debate
            FROM publicacion p
            LEFT JOIN grupo_debate g
                ON p.id_grupoDebate = g.id_grupo
            ORDER BY p.fecha_publicacion DESC, p.titulo ASC
        """)

        datos = cursor.fetchall()
        conn.close()
        return datos

    def obtener_grupos_debate(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_grupo, nombre
            FROM grupo_debate
            ORDER BY nombre ASC
        """)

        datos = cursor.fetchall()
        conn.close()
        return datos

    def existe_grupo_debate(self, id_grupo):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT 1 FROM grupo_debate WHERE id_grupo = ?",
            (id_grupo,)
        )

        existe = cursor.fetchone() is not None
        conn.close()
        return existe

    def crear_publicacion(
        self,
        titulo,
        descripcion,
        fecha_publicacion,
        tipo,
        id_grupoDebate=None
    ):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO publicacion (
                titulo,
                descripcion,
                fecha_publicacion,
                tipo,
                id_grupoDebate
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            titulo,
            descripcion,
            fecha_publicacion,
            tipo,
            id_grupoDebate
        ))

        nuevo_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return nuevo_id

    def actualizar_publicacion(
        self,
        id_publicacion,
        titulo,
        descripcion,
        fecha_publicacion,
        tipo,
        id_grupoDebate=None
    ):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE publicacion
            SET titulo = ?,
                descripcion = ?,
                fecha_publicacion = ?,
                tipo = ?,
                id_grupoDebate = ?
            WHERE id_publicacion = ?
        """, (
            titulo,
            descripcion,
            fecha_publicacion,
            tipo,
            id_grupoDebate,
            id_publicacion
        ))

        conn.commit()
        conn.close()

    def eliminar_publicacion(self, id_publicacion):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM publicacion WHERE id_publicacion = ?",
            (id_publicacion,)
        )

        conn.commit()
        conn.close()
