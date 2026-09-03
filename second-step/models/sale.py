# models/sale.py

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.conexionDB import Base


class Sale(Base):
    __tablename__ = "sale"

    id_sale = Column(Integer, primary_key=True, index=True)
    id_book = Column(Integer, ForeignKey("book.id_book", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL(10, 2), nullable=False)
    sale_date = Column(Date, nullable=False, default=func.current_date())
    total_amount = Column(DECIMAL(10, 2))  # Generado por la DB
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relaciones
    book = relationship("Book", backref="sales")