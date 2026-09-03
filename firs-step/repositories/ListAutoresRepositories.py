# repositories/ListaAutoresRepositories.py

from sqlalchemy.orm import Session
from core.conexionDB import engine
from models.author import Author


class Autores:
    def obtener_todos(self):
        with Session(engine) as session:
            return session.query(Author).all()

    def obtener_por_id(self, author_id: int):
        with Session(engine) as session:
            return session.query(Author).filter(Author.id_author == author_id).first()

    def crear(self, name: str, birth_date: str):
        with Session(engine) as session:
            author = Author(name=name, birth_date=birth_date)
            session.add(author)
            session.commit()
            session.refresh(author)
            return author

    def actualizar(self, author_id: int, name: str = None, birth_date: str = None):
        with Session(engine) as session:
            author = session.query(Author).filter(Author.id_author == author_id).first()
            if author:
                if name:
                    author.name = name
                if birth_date:
                    author.birth_date = birth_date
                session.commit()
                session.refresh(author)
            return author

    def eliminar(self, author_id: int):
        with Session(engine) as session:
            author = session.query(Author).filter(Author.id_author == author_id).first()
            if author:
                session.delete(author)
                session.commit()
                return True
            return False