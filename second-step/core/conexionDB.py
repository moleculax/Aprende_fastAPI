# core/conexionDB.py

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ConectaPostgres:
    HOST = "localhost"
    DATABASE = "db_blog"
    USER = "admin"
    PASSWORD = "admin123"
    PORT = "5432"

    DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    engine = None
    SessionLocal = None

    @classmethod
    def get_engine(cls):
        """
        Obtiene o crea el motor de conexión a la base de datos.

        El motor es un objeto que administra el pool de conexiones.
        Solo se crea una vez (singleton) y se reutiliza.

        Returns:
            Engine: El motor de conexión de SQLAlchemy
        """
        if cls.engine is None:
            # Crea el motor solo si no existe
            cls.engine = create_engine(cls.DATABASE_URL)
        return cls.engine

    @classmethod
    def get_session_factory(cls):
        """
        Obtiene o crea la fábrica de sesiones.

        Una sesión es un objeto que representa una transacción con la BD.
        La get_session_factory permite crear múltiples sesiones a partir del motor.

        Returns:
            sessionmaker: Fábrica de sesiones de SQLAlchemy
        """
        if cls.SessionLocal is None:
            # Crea la fábrica solo si no existe
            cls.SessionLocal = sessionmaker(
                autocommit=False,  # No guarda automáticamente
                autoflush=False,  # No envía cambios automáticamente
                bind=cls.get_engine()  # Asocia la fábrica al motor
            )
        return cls.SessionLocal

    @classmethod
    def ConexionPostgres(cls):
        """
        Crea y retorna una sesión activa de base de datos.

        Esta función es útil cuando necesitas una sesión para operaciones
        específicas que no requieren el contexto de FastAPI.

        Returns:
            Session: Objeto sesión de SQLAlchemy o None si hay error
        """
        try:
            Session = cls.get_session_factory()
            return Session()
        except Exception as e:
            print(f"Error PostgreSQL: {e}")
            return None

    @classmethod
    def VersionPostgres(cls):
        """
        Obtiene la versión de PostgreSQL ejecutando una consulta SQL.

        Esta función demuestra cómo ejecutar SQL puro con SQLAlchemy.

        Returns:
            str: Versión de PostgreSQL o None si hay error
        """
        Session = cls.get_session_factory()
        db = Session()
        try:
            # text() permite ejecutar SQL puro
            result = db.execute(text("SELECT version();"))
            version = result.fetchone()
            return version[0] if version else None
        finally:
            db.close()


# ============================================================
# FUNCIÓN DE DEPENDENCIA PARA FASTAPI
# ============================================================
def get_db():
    """
    Función generadora que actúa como dependencia de FastAPI.

    Esta función usa 'yield' para manejar el ciclo de vida de la sesión:
    1. Crea una sesión al inicio
    2. La entrega (yield) a la ruta de FastAPI
    3. La cierra automáticamente al finalizar la ruta

    Esto garantiza que las sesiones siempre se cierren correctamente,
    incluso si ocurren errores durante la ejecución.

    Yields:
        Session: Sesión activa de SQLAlchemy para usar en la ruta
    """
    Session = ConectaPostgres.get_session_factory()
    db = Session()
    try:
        yield db  # Entrega la sesión a la ruta
    finally:
        db.close()  # Siempre cierra la sesión al finalizar


# ============================================================
# EXPORTAR engine PARA REPOSITORIOS
# ============================================================
engine = ConectaPostgres.get_engine()