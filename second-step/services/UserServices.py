# services/UserServices.py

from repositories.UsersRepositories import GetUsers


class ServicesUsers:
    getUser = GetUsers()

    def UsuariosFull(self):
        lista = self.getUser.getAllUsers()
        Usuarios = []
        for u in lista:
            users = {
                "id_users": u.id_users,
                "usuario": u.usuario,
                "password": u.password,
                "email": u.email,
                "last_login": u.last_login,
                "created_at": u.created_at,
                "updated_at": u.updated_at
            }
            Usuarios.append(users)

        return Usuarios