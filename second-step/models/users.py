# models/users.py

from sqlalchemy import Column, Integer, String, DateTime, func, Table, MetaData
from core.conexionDB import Base


class Users(Base):
    __tablename__ = "users"

    id_users = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    last_login = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

