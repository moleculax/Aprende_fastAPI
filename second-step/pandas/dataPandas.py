import pandas as pd
import os
import json

from sqlalchemy import func


# ===================================================================
class GeneraDataFrame:
    def UsersDataFrame(self, obj):
        """ Crear un DataFrame a partir de un objeto de datos"""
        df = pd.DataFrame(obj)
        path = "data/archivos/"
        file = "Users.csv"
        os.makedirs(path, exist_ok=True)
        df.to_csv(f'{path}{file}', index=False)
        return df

    def AuthorDataFrame(self, obj):
        """ Crear un DataFrame a partir de un objeto de datos"""
        df = pd.DataFrame(obj)
        path = "data/archivos/"
        file = "Author.csv"
        os.makedirs(path, exist_ok=True)
        df.to_csv(f'{path}{file}', index=False)
        return df

    def BookDataFrame(self,obj):
        """Crear un DataFrame a partir de un objeto de datos"""
        df = pd.DataFrame(obj)
        path = "data/archivos/"
        file = "Book.csv"
        os.makedirs(path, exist_ok=True)
        df.to_csv(f'{path}{file}', index=False)
        return df

    class TratarDatosDataFrame:
        pass
    # def agregarEnDataFrame(self, content):
    #     """Agregar un nuevo post y retornar DataFrame actualizado"""
    #     new_id = max([content["id_book"] for book in data]) + 1 if data else 1
    #     Libros = {
    #         "id_book": book.id_book,
    #         "title": book.title,
    #         "publication_date": book.publication_date,
    #         "pages": book.pages,
    #         "isbn": book.isbn,
    #         "price": book.price,
    #         "author_id": book.author_id,
    #         "created_at": func.now(),
    #         "updated_at": func.now(),
    #     }
    #     data.append(libros)
    #
    #     df = pd.DataFrame(data)
    #
    #     path = "data/archivos/"
    #     file = "Book.csv"
    #     fileJSON = "Book.json"
    #     fileHTML = "Book.html"
    #     os.makedirs(path, exist_ok=True)
    #     # Genera archivo csv
    #     df.to_csv(f'{path}{file}', index=False)
    #     # Genera JSON
    #     df.to_json(f'{path}{fileJSON}', orient='records',)
    #     # Genera HTML
    #     df.to_html(f'{path}{fileHTML}', index=False)
    #
    #     return df

    # def actualizarEnDataFrame(self, post_id, title=None, content=None):
    #     """Actualizar un post existente por su ID"""
    #     objdatos = BlogData()
    #     data = objdatos.objetoDatos()
    #
    #     for post in data:
    #         if post["id"] == post_id:
    #             if title is not None:
    #                 post["title"] = title
    #             if content is not None:
    #                 post["Content"] = content
    #
    #             df = pd.DataFrame(data)
    #
    #             path = "data/archivos/"
    #             file = "dataBlog.csv"
    #             fileJSON = "dataBlog.json"
    #             fileHTML = "dataBlog.html"
    #             os.makedirs(path, exist_ok=True)
    #             df.to_csv(f'{path}{file}', index=False)
    #             df.to_json(f'{path}{fileJSON}', orient='records')
    #             df.to_html(f'{path}{fileHTML}', index=False)
    #
    #             return df
    #
    #     print(f"Post con ID {post_id} no encontrado")
    #     return pd.DataFrame(data)

    # def eliminarEnDataFrame(self, post_id):
    #     """Eliminar un post por su ID"""
    #     objdatos = BlogData()
    #     data = objdatos.objetoDatos()
    #
    #     for i, post in enumerate(data):
    #         if post["id"] == post_id:
    #             eliminado = data.pop(i)
    #
    #             df = pd.DataFrame(data)
    #
    #             path = "data/archivos/"
    #             file = "dataBlog.csv"
    #             fileJSON = "dataBlog.json"
    #             fileHTML = "dataBlog.html"
    #             os.makedirs(path, exist_ok=True)
    #             df.to_csv(f'{path}{file}', index=False)
    #             df.to_json(f'{path}{fileJSON}', orient='records')
    #             df.to_html(f'{path}{fileHTML}', index=False)
    #             print(f" Post con ID {post_id} eliminado")
    #             return df
    #
    #     print(f"Post con ID {post_id} no encontrado")
    #     return pd.DataFrame(data)
    #
    # def actualizarCampo(self, post_id, campo, valor):
    #     """Actualizar un campo específico de un post"""
    #     objdatos = BlogData()
    #     data = objdatos.objetoDatos()
    #
    #     for post in data:
    #         if post["id"] == post_id:
    #             if campo in post:
    #                 post[campo] = valor
    #
    #                 df = pd.DataFrame(data)
    #
    #                 path = "data/archivos/"
    #                 file = "dataBlog.csv"
    #                 fileHTML = "dataBlog.html"
    #                 os.makedirs(path, exist_ok=True)
    #                 df.to_csv(f'{path}{file}', index=False)
    #                 df.to_html(f'{path}{fileHTML}', index=False)
    #
    #                 print(f" Campo '{campo}' actualizado para ID {post_id}")
    #                 return df
    #             else:
    #                 print(f" Campo '{campo}' no existe en el post")
    #                 return pd.DataFrame(data)
    #
    #     print(f"❌ Post con ID {post_id} no encontrado")
    #     return pd.DataFrame(data)