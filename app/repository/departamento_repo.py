# app/data/departamento_repo.py

import sqlite3
from app.data.db import get_connection
from app.models.departamento import Departamento


class DepartamentoRepository:

    
    # CONSULTAS
    
    def find_all(self) -> list:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT d.id_departamento,
                       d.nombre,
                       d.id_facultad,
                       f.nombre AS facultad
                FROM departamento d
                JOIN facultad f ON d.id_facultad = f.id_facultad
                ORDER BY f.nombre, d.nombre
            """)
            rows = cursor.fetchall()
        return [self._row_to_model(row) for row in rows]

    def find_by_id(self, id_departamento: int):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT d.id_departamento,
                       d.nombre,
                       d.id_facultad,
                       f.nombre AS facultad
                FROM departamento d
                JOIN facultad f ON d.id_facultad = f.id_facultad
                WHERE d.id_departamento = ?
            """, (id_departamento,))
            row = cursor.fetchone()
        return self._row_to_model(row) if row else None

    def find_all_by_facultad(self, id_facultad: int) -> list:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT d.id_departamento,
                       d.nombre,
                       d.id_facultad,
                       f.nombre AS facultad
                FROM departamento d
                JOIN facultad f ON d.id_facultad = f.id_facultad
                WHERE d.id_facultad = ?
                ORDER BY d.nombre
            """, (id_facultad,))
            rows = cursor.fetchall()
        return [self._row_to_model(row) for row in rows]

    def find_all_facultades(self) -> list:
        """Devuelve lista de tuplas (id_facultad, nombre) para poblar el comboBox."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id_facultad, nombre
                FROM facultad
                ORDER BY nombre
            """)
            rows = cursor.fetchall()
        return [(row["id_facultad"], row["nombre"]) for row in rows]

    
    # INSERT
    
    def insert(self, departamento: Departamento) -> Departamento:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO departamento (nombre, id_facultad)
                    VALUES (?, ?)
                """, (departamento.nombre, departamento.id_facultad))
                conn.commit()
                departamento.id_departamento = cursor.lastrowid
            return departamento
        except sqlite3.IntegrityError:
            raise ValueError("El departamento ya existe o la facultad indicada no es válida")

    
    # UPDATE
    
    def update(self, departamento: Departamento) -> Departamento:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE departamento
                SET nombre     = ?,
                    id_facultad = ?
                WHERE id_departamento = ?
            """, (
                departamento.nombre,
                departamento.id_facultad,
                departamento.id_departamento
            ))
            conn.commit()
        print("UPDATE OK ID:", departamento.id_departamento)
        return departamento

    
    # DELETE
    
    def delete(self, id_departamento: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM departamento WHERE id_departamento = ?",
                (id_departamento,)
            )
            conn.commit()
        print("DELETE OK ID:", id_departamento)
        return True

    
    # UTILIDAD PRIVADA
    
    def _row_to_model(self, row) -> Departamento:
        return Departamento(
            id_departamento=row["id_departamento"],
            nombre=row["nombre"],
            id_facultad=row["id_facultad"],
            facultad=row["facultad"]
        )