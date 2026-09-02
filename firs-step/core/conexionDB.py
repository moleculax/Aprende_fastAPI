import os
import sqlite3
from sqlite3 import Error
import psycopg2
from psycopg2 import Error as PostgresError
import mysql.connector
from mysql.connector import Error as MySQLError


class ConectaSQLite:

    @classmethod
    def ConexionLite(cls):
        try:
            os.makedirs("db_lite", exist_ok=True)
            conn = sqlite3.connect("db_lite/db_blog.db")
            conn.row_factory = sqlite3.Row
            return conn
        except Error as e:
            print(e)
            return None

    @classmethod
    def VersionLite(cls):
        conn = cls.ConexionLite()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT sqlite_version();")
            version = cursor.fetchone()
            conn.close()
            return version[0]
        return None


class ConectaPostgres:

    @classmethod
    def ConexionPostgres(cls):
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="db_blog",
                user="admin",
                password="admin123",
                port="5432"
            )
            return conn
        except PostgresError as e:
            print(e)
            return None

    @classmethod
    def VersionPostgres(cls):
        conn = cls.ConexionPostgres()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            conn.close()
            return version[0]
        return None


class ConectaMySQL:

    @classmethod
    def ConexionMySQL(cls):
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
            print(e)
            return None

    @classmethod
    def VersionMySQL(cls):
        conn = cls.ConexionMySQL()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT VERSION();")
            version = cursor.fetchone()
            conn.close()
            return version[0]
        return None