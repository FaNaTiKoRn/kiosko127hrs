# Proyecto: Kiosco127Hrs
# Autor: José Torres Tortorella (95.704.279)
# Descripción: Sistema de gestión de inventario para una pequeña tienda, desarrollado en Python para el Curso Iniciación a la Programación con Pyhton.
# Instructor: Fede Liquin.
# Tutora: Natalia ThemTham.

## Archivo: makedb.py

"""
Este archivo crea la base de datos SQLite necesaria para la aplicación.
"""

import sqlite3

def crear_base_datos():
    """
    Crea la base de datos y las tablas requeridas si no existen.
    """
    try:
        # Establecer conexión con la base de datos
        conexion = sqlite3.connect("kiosco127hrs.db")
        cursor = conexion.cursor()

        # Creación de la tabla productos
        query = '''
            CREATE TABLE IF NOT EXISTS productos (
                id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                categoria TEXT NOT NULL,
                precio REAL NOT NULL,
                stock INTEGER NOT NULL CHECK(stock >= 0)
            );
        '''
        cursor.execute(query)
        conexion.commit()
        print("Base de datos y tabla 'productos' creadas exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al crear la base de datos: {e}")
    finally:
        if conexion:
            conexion.close()

if __name__ == "__main__":
    crear_base_datos()
