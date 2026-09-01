import sqlite3
from sqlite3 import Error
import os

# =========================================================================
# IMPORTAR PARA POSTGRESQL Y MYSQL
# =========================================================================
import psycopg2
from psycopg2 import Error as PostgresError
import mysql.connector
from mysql.connector import Error as MySQLError


# =========================================================================
# CLASE SQLITE
# =========================================================================
class ConectaSQLLITE:
    DATABASE_URL = "db_lite/dataBase.db"

    @classmethod
    def create_connection(cls):
        """Crear conexión a la base de datos SQLite"""
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(cls.DATABASE_URL), exist_ok=True)

        try:
            conn = sqlite3.connect(cls.DATABASE_URL)
            return conn
        except Error as e:
            print(f"Error al conectar a SQLite: {e}")
            return None


# =========================================================================
# CLASE POSTGRESQL
# =========================================================================
class ConectaPOSTGRES:
    @classmethod
    def create_connection(cls):
        """Crear conexión a PostgreSQL"""
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="database",
                user="admin",
                password="admin123",
                port="5432"
            )
            return conn
        except PostgresError as e:
            print(f"Error al conectar a PostgreSQL: {e}")
            return None


# =========================================================================
# CLASE MYSQL
# =========================================================================
class ConectaMYSQL:
    @classmethod
    def create_connection(cls):
        """Crear conexión a MySQL"""
        try:
            conn = mysql.connector.connect(
                host="localhost",
                database="database",
                user="admin",
                password="admin123",
                port="3306"
            )
            return conn
        except MySQLError as e:
            print(f"Error al conectar a MySQL: {e}")
            return None