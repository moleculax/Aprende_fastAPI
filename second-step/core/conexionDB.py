# core/conexionDB.py

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# ============================================================
# BASE PARA MODELOS
# ============================================================
Base = declarative_base()
# Crea la clase base para todos los modelos SQLAlchemy
# Todos los modelos (Author, Book, Sale) heredarán de esta clase
# Permite que SQLAlchemy mapee las clases Python a tablas de la base de datos


# ============================================================
# POSTGRESQL  ESTA SIENDO USADO POR DEFECTO EN ESTE MINI PROYECTO
# ============================================================
class ConectaPostgres:
    # ============================================================
    # CONFIGURACIÓN DE LA CONEXIÓN
    # ============================================================
    HOST = "localhost"        # Dirección del servidor PostgreSQL
    DATABASE = "db_blog"      # Nombre de la base de datos
    USER = "admin"            # Usuario para autenticación
    PASSWORD = "admin123"     # Contraseña del usuario
    PORT = "5432"             # Puerto por defecto de PostgreSQL

    DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    # Construye la URL de conexión completa con las credenciales
    # Formato: postgresql://usuario:contraseña@host:puerto/base_datos

    engine = None             # Almacena el motor de conexión (pool de conexiones)
    SessionLocal = None       # Almacena la fábrica de sesiones

    # ============================================================
    # get_engine(): Obtiene o crea el motor de conexión
    # ============================================================
    @classmethod
    def get_engine(cls):
        # cls es la clase ConectaPostgres
        # Si el engine no existe (es None), lo crea
        if cls.engine is None:
            # create_engine() crea un pool de conexiones a la base de datos
            # No abre una conexión inmediatamente, solo la prepara
            cls.engine = create_engine(cls.DATABASE_URL)
        # Retorna el engine (existente o recién creado)
        return cls.engine
        # Uso: ConectaPostgres.get_engine()

    # ============================================================
    # get_session(): Crea una sesión para interactuar con la BD
    # ============================================================
    @classmethod
    def get_session(cls):
        # Si SessionLocal no existe, la crea
        if cls.SessionLocal is None:
            # sessionmaker() crea una fábrica de sesiones
            # bind=cls.get_engine() la vincula al motor de conexión
            cls.SessionLocal = sessionmaker(
                autocommit=False,  # No auto-guardar, requiere commit explícito
                autoflush=False,   # No auto-enviar cambios a la BD
                bind=cls.get_engine()
            )
        # Crea y retorna una nueva sesión (conexión activa a la BD)
        return cls.SessionLocal()
        # Uso: ConectaPostgres.get_session()

    # ============================================================
    # ConexionPostgres(): Conexión segura con manejo de errores
    # ============================================================
    @classmethod
    def ConexionPostgres(cls):
        try:
            # Intenta crear y retornar una sesión
            return cls.get_session()
        except Exception as e:
            # Si falla, imprime el error y retorna None
            print(f"Error PostgreSQL: {e}")
            return None
        # Uso: ConectaPostgres.ConexionPostgres()

    # ============================================================
    # VersionPostgres(): Obtiene la versión de PostgreSQL
    # ============================================================
    @classmethod
    def VersionPostgres(cls):
        # Obtiene una conexión a la BD
        conn = cls.ConexionPostgres()
        # Si la conexión es exitosa
        if conn:
            try:
                # Ejecuta una consulta SQL para obtener la versión
                result = conn.execute(text("SELECT version();"))
                # Obtiene el primer resultado
                version = result.fetchone()
                # Cierra la conexión
                conn.close()
                # Retorna la versión (primer elemento de la tupla)
                return version[0] if version else None
            except Exception as e:
                # Si falla, imprime el error y retorna None
                print(f"Error: {e}")
                return None
        # Si no hay conexión, retorna None
        return None
        # Uso: ConectaPostgres.VersionPostgres()


# ============================================================
# EXPORTAR engine PARA REPOSITORIOS
# ============================================================
engine = ConectaPostgres.get_engine()
# Crea el motor de conexión al importar este archivo
# Los repositorios pueden usar este engine directamente
# Ejemplo: from core.conexionDB import engine
# Uso: with engine.connect() as conn: ...