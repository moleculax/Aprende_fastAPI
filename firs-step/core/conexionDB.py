# core/conexionDB.py

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# ============================================================
# BASE PARA MODELOS
# ============================================================
Base = declarative_base()

# ============================================================
# POSTGRESQL  ESTA SIENDO USADO POR DEFECTO EN ESTE MINI PROYECTO
# ============================================================
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
        if cls.engine is None:
            cls.engine = create_engine(cls.DATABASE_URL)
        return cls.engine

    @classmethod
    def get_session(cls):
        if cls.SessionLocal is None:
            cls.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls.get_engine())
        return cls.SessionLocal()

    @classmethod
    def ConexionPostgres(cls):
        try:
            return cls.get_session()
        except Exception as e:
            print(f"Error PostgreSQL: {e}")
            return None

    @classmethod
    def VersionPostgres(cls):
        session = cls.ConexionPostgres()
        if session:
            try:
                result = session.execute(text("SELECT version();"))
                version = result.fetchone()
                session.close()
                return version[0] if version else None
            except Exception as e:
                print(f"Error: {e}")
                return None
        return None


# ============================================================
# EXPORTAR engine PARA REPOSITORIOS
# ============================================================
engine = ConectaPostgres.get_engine()