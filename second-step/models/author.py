# models/author.py

from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func
from core.conexionDB import Base


class Author(Base):
    __tablename__ = "author"

    id_author = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())