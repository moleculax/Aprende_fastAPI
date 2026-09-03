from sqlalchemy import Column, Integer, DateTime, String, Date, ForeignKey, func
from sqlalchemy.orm import relationship

from core.conexionDB import Base


class Book(Base):
    __tablename__ = "book"

    id_book = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    publication_date = Column(Date, nullable=False)
    pages = Column(Integer, nullable=False)  # ✅ Agregar pages
    isbn = Column(String(100), nullable=False)  # ✅ Agregar isbn
    price = Column(Integer, nullable=False)  # ✅ Agregar price (o DECIMAL)
    author_id = Column(Integer, ForeignKey("author.id_author", ondelete="CASCADE"), nullable=False)  # ✅ Cambiar a author_id
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relaciones
    author = relationship("Author", backref="books")