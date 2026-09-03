from sqlalchemy.orm import Session
from core.conexionDB import engine
from models.Book import Book


# ========== LIBROS DE AUTORES =========================
class LibrosDeAutores:
    def obtener_todos(self):
        with Session(engine) as session:
            return session.query(Book).all()

    def obtener_por_id(self, book_id: int):
        with Session(engine) as session:
            return session.query(Book).filter(Book.id_book == book_id).first()

    def crear(self, title: str, publication_date: str, id_author: int):
        with Session(engine) as session:
            book = Book(title=title, publication_date=publication_date, id_author=id_author)
            session.add(book)
            session.commit()
            session.refresh(book)
            lastInsert = book.id_book
            return book

    def actualizar(self, book_id: int, title: str = None, publication_date: str = None, id_author: int = None):
        with Session(engine) as session:
            book = session.query(Book).filter(Book.id_book == book_id).first()
            if book:
                if title:
                    book.title = title
                if publication_date:
                    book.publication_date = publication_date
                if id_author:
                    book.id_author = id_author
                session.commit()
                session.refresh(book)
            return book

    def eliminar(self, book_id: int):
        with Session(engine) as session:
            book = session.query(Book).filter(Book.id_book == book_id).first()
            if book:
                session.delete(book)
                session.commit()
                return True
            return False
