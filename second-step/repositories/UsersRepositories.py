# repositories/UsersRepositories.py

from models.users import Users
from core.conexionDB import engine
from sqlalchemy.orm import Session


class GetUsers:
    # TODOS LOS USUARIOS
    def getAllUsers(self):
        with Session(engine) as session:
            usuarios = session.query(Users).all()
            return usuarios

    # BUSCO USUARIO POR NOMBRE DE USUARIO
    def getUsersPorUsuario(self, usuario: str):
        with Session(engine) as session:
            usuario = session.query(Users).filter(Users.usuario == usuario).first()
            return usuario

    # USUARIOS POR ID
    def getUsersPorID(self, id_users: int):
        with Session(engine) as session:
            usuario = session.query(Users).filter(Users.id_users == id_users).first()
            return usuario

    # USUARIOS POR EMAIL
    def getUserPorMail(self, email: str):
        with Session(engine) as session:
            usuario = session.query(Users).filter(Users.email == email).first()
            return usuario


class PostUsers:
    # CREO USUARIOS
    def postUser(self, user: Users):
        with Session(engine) as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user


class PutUsers:
    # ACTUALIZA USUARIOS
    def updateUser(self, user_data: dict):
        with Session(engine) as session:
            # ✅ Extraer id del JSON
            id_users = user_data.get("id_users")
            if not id_users:
                return None

            user = session.query(Users).filter(Users.id_users == id_users).first()
            if user:
                # ✅ Extraer y actualizar campos del JSON
                if "usuario" in user_data:
                    user.usuario = user_data["usuario"]
                if "password" in user_data:
                    user.password = user_data["password"]
                if "email" in user_data:
                    user.email = user_data["email"]

                session.commit()
                session.refresh(user)
                return user
            return None


class DeleteUsers:
    # ELIMINA USUARIOS
    def deleteUser(self, id_users: int):
        with Session(engine) as session:
            user = session.query(Users).filter(Users.id_users == id_users).first()
            if user:
                session.delete(user)
                session.commit()
                return True
            return False