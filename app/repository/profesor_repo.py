from app.data.db import get_connection
from app.models.profesor import Profesor


class ProfesorRepository:

    # obtenemos todos los profesores
    def find_all(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_profesor, nombre, correo, telefono, titulo, id_departamento, jefe_dtp
            FROM profesor
            ORDER BY nombre
        """)

        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_model(row) for row in rows]

    # encontrar un profesor por id
    def find_by_id(self, id_profesor):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_profesor, nombre, correo, telefono, titulo, id_departamento, jefe_dtp
            FROM profesor
            WHERE id_profesor = ?
        """, (id_profesor,))

        row = cursor.fetchone()
        conn.close()
        return self._row_to_model(row) if row else None

    # se obtiene profesores por departamento
    def find_by_departamento(self, id_departamento):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_profesor, nombre, correo, telefono, titulo, id_departamento, jefe_dtp
            FROM profesor
            WHERE id_departamento = ?
            ORDER BY nombre
        """, (id_departamento,))

        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_model(row) for row in rows]

    # nuevo profesor
    def insert(self, profesor: Profesor):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO profesor (nombre, correo, telefono, titulo, id_departamento, jefe_dtp)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            profesor.nombre,
            profesor.correo,
            profesor.telefono,
            profesor.titulo,
            profesor.id_departamento,
            1 if profesor.jefe_dtp else 0
        ))

        conn.commit()
        profesor.id = cursor.lastrowid
        conn.close()
        return profesor

    # update de profesor existente
    def update(self, profesor: Profesor):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE profesor SET
                nombre = ?,
                correo = ?,
                telefono = ?,
                titulo = ?,
                id_departamento = ?,
                jefe_dtp = ?
            WHERE id_profesor = ?
        """, (
            profesor.nombre,
            profesor.correo,
            profesor.telefono,
            profesor.titulo,
            profesor.id_departamento,
            1 if profesor.jefe_dtp else 0,
            profesor.id
        ))

        conn.commit()
        conn.close()
        return profesor

    # se elimina un profesor por ID
    def delete(self, id_profesor):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM profesor WHERE id_profesor = ?",
            (id_profesor,)
        )

        conn.commit()
        conn.close()
        return True

    # esto para desmarcar jefes del departamento (lo puedes dejar aunque no lo uses)
    def desmarcar_jefes_del_departamento(self, id_departamento):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE profesor
            SET jefe_dtp = 0
            WHERE id_departamento = ?
        """, (id_departamento,))

        conn.commit()
        conn.close()
        return True

    # convertimos una fila en objeto profesor
    def _row_to_model(self, row):
        return Profesor(
            id=row[0],
            nombre=row[1],
            correo=row[2],
            telefono=row[3],
            titulo=row[4],
            id_departamento=row[5],
            jefe_dtp=bool(row[6])
        )
    
    def find_all_with_asignaturas(self):
        conn = get_connection()
        cursor = conn.cursor()

        # Miramos si existe alguna tabla N:N
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tablas = [t[0] for t in cursor.fetchall()]

        tabla_relacion = None

        if "profesor_asignatura" in tablas:
            tabla_relacion = "profesor_asignatura"
        elif "asignatura_profesor" in tablas:
            tabla_relacion = "asignatura_profesor"

        # Si NO existe tabla N:N, generamos profesores sin asignaturas
        if tabla_relacion is None:
            cursor.execute("""
                SELECT id_profesor, nombre, correo, telefono, titulo, id_departamento, jefe_dtp
                FROM profesor
                ORDER BY nombre
            """)

            rows = cursor.fetchall()
            conn.close()

            profesores = []

            for row in rows:
                profesores.append(Profesor(
                    id=row[0],
                    nombre=row[1],
                    correo=row[2],
                    telefono=row[3],
                    titulo=row[4],
                    id_departamento=row[5],
                    jefe_dtp=bool(row[6]),
                    asignaturas=[]
                ))

            return profesores

        # Si existe tabla N:N, usamos la relación real
        cursor.execute(f"""
            SELECT 
                p.id_profesor,
                p.nombre,
                p.correo,
                p.telefono,
                p.titulo,
                p.id_departamento,
                p.jefe_dtp,
                a.nombre
            FROM profesor p
            LEFT JOIN {tabla_relacion} pa 
                ON p.id_profesor = pa.id_profesor
            LEFT JOIN asignatura a 
                ON pa.id_asignatura = a.id_asignatura
            ORDER BY p.nombre, a.nombre
        """)

        rows = cursor.fetchall()
        conn.close()

        profesores = {}

        for row in rows:
            id_profesor = row[0]

            if id_profesor not in profesores:
                profesores[id_profesor] = Profesor(
                    id=row[0],
                    nombre=row[1],
                    correo=row[2],
                    telefono=row[3],
                    titulo=row[4],
                    id_departamento=row[5],
                    jefe_dtp=bool(row[6]),
                    asignaturas=[]
                )

            if row[7]:
                profesores[id_profesor].asignaturas.append(row[7])

        return list(profesores.values())
    

    def debug_tablas(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tablas = cursor.fetchall()

        print("======= TABLAS EN LA BD =======")
        for tabla in tablas:
            print(tabla[0])
        print("===============================")

        conn.close()