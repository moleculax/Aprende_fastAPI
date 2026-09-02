import pandas as pd
import os
import json

class BlogData:
    def objetoDatos(self):
        # Leer el JSON generado
        path = "data/archivos/dataBlog.json"

        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            # Si no existe, usar datos iniciales
            return self._datos_iniciales()

    def _datos_iniciales(self):
        data = [
            {
                "id": 1,
                "title": "Introduccion a FastAPI",
                "Content": "FastAPI es un framework web moderno y de alto rendimiento para construir APIs con Python. Esta basado en Starlette para las partes web y Pydantic para las partes de datos. Es uno de los frameworks mas rapidos disponibles, comparable con NodeJS y Go. Ofrece documentacion automatica interactiva, validacion de datos integrada y soporte para asincronia."
            },
            {
                "id": 2,
                "title": "Python: Mejores Practicas",
                "Content": "Escribir codigo Python de calidad implica seguir las guias de estilo PEP 8, usar tipado estatico con mypy, aprovechar las list comprehensions y generadores, manejar excepciones correctamente, y escribir pruebas unitarias con pytest. Ademas, es importante mantener una arquitectura limpia y modular."
            },
            {
                "id": 3,
                "title": "Django vs FastAPI",
                "Content": "Django es el framework web full-stack por excelencia en Python, ideal para aplicaciones grandes con admin integrado, ORM y autenticacion. FastAPI es mas ligero y orientado a APIs, con mayor rendimiento y facilidad para aplicaciones asincronas. La eleccion depende del proyecto: Django para aplicaciones complejas con frontend integrado, FastAPI para APIs puras y microservicios."
            },
            {
                "id": 4,
                "title": "Pydantic: Validacion de Datos",
                "Content": "Pydantic utiliza tipos de Python para validar datos en tiempo de ejecucion. Permite definir modelos con campos tipados, validaciones personalizadas, y serializacion automatica a JSON. Es la base de FastAPI y se usa ampliamente en configuraciones, lectura de variables de entorno y parsing de datos."
            },
            {
                "id": 5,
                "title": "REST API con FastAPI",
                "Content": "Construir una REST API con FastAPI es sencillo: defines rutas con decoradores, usas Pydantic para los modelos de datos, y automaticamente obtienes documentacion interactiva en /docs. Incluye manejo de errores, dependencias, autenticacion JWT, y core a bases de datos con SQLAlchemy o Tortoise-ORM."
            },
            {
                "id": 6,
                "title": "SQLAlchemy ORM Avanzado",
                "Content": "SQLAlchemy es el ORM mas potente de Python. Permite mapear objetos a tablas de base de datos, escribir consultas complejas, y manejar relaciones entre tablas. Incluye soporte para migraciones con Alembic y funciona con multiples bases de datos como PostgreSQL, MySQL y SQLite."
            },
            {
                "id": 7,
                "title": "Autenticacion JWT en APIs",
                "Content": "JWT (JSON Web Tokens) es un estandar para autenticacion en APIs. Se basa en tokens firmados que contienen informacion del usuario y expiran en un tiempo determinado. En FastAPI se integra facilmente con OAuth2PasswordBearer y la libreria python-jose para crear y verificar tokens."
            }
        ]

        return data


# ===================================================================
class CreoDataFrame:

    def dataFrame(self):
        objdatos = BlogData()
        obj = objdatos.objetoDatos()
        df = pd.DataFrame(obj)
        path = "data/archivos/"
        file = "dataBlog.csv"
        os.makedirs(path, exist_ok=True)
        df.to_csv(f'{path}{file}', index=False)
        return df

    def agregarEnDataFrame(self, title, content):
        """Agregar un nuevo post y retornar DataFrame actualizado"""
        objdatos = BlogData()
        data = objdatos.objetoDatos()
        new_id = max([post["id"] for post in data]) + 1 if data else 1
        new_post = {
            "id": new_id,
            "title": title,
            "Content": content
        }
        data.append(new_post)

        df = pd.DataFrame(data)

        path = "data/archivos/"
        file = "dataBlog.csv"
        fileJSON = "dataBlog.json"
        fileHTML = "dataBlog.html"
        os.makedirs(path, exist_ok=True)
        # Genera archivo csv
        df.to_csv(f'{path}{file}', index=False)
        # Genera JSON
        df.to_json(f'{path}{fileJSON}', orient='records',)
        # Genera HTML
        df.to_html(f'{path}{fileHTML}', index=False)

        return df

    def actualizarEnDataFrame(self, post_id, title=None, content=None):
        """Actualizar un post existente por su ID"""
        objdatos = BlogData()
        data = objdatos.objetoDatos()

        for post in data:
            if post["id"] == post_id:
                if title is not None:
                    post["title"] = title
                if content is not None:
                    post["Content"] = content

                df = pd.DataFrame(data)

                path = "data/archivos/"
                file = "dataBlog.csv"
                fileJSON = "dataBlog.json"
                fileHTML = "dataBlog.html"
                os.makedirs(path, exist_ok=True)
                df.to_csv(f'{path}{file}', index=False)
                df.to_json(f'{path}{fileJSON}', orient='records')
                df.to_html(f'{path}{fileHTML}', index=False)

                return df

        print(f"Post con ID {post_id} no encontrado")
        return pd.DataFrame(data)

    def eliminarEnDataFrame(self, post_id):
        """Eliminar un post por su ID"""
        objdatos = BlogData()
        data = objdatos.objetoDatos()

        for i, post in enumerate(data):
            if post["id"] == post_id:
                eliminado = data.pop(i)

                df = pd.DataFrame(data)

                path = "data/archivos/"
                file = "dataBlog.csv"
                fileJSON = "dataBlog.json"
                fileHTML = "dataBlog.html"
                os.makedirs(path, exist_ok=True)
                df.to_csv(f'{path}{file}', index=False)
                df.to_json(f'{path}{fileJSON}', orient='records')
                df.to_html(f'{path}{fileHTML}', index=False)
                print(f" Post con ID {post_id} eliminado")
                return df

        print(f"Post con ID {post_id} no encontrado")
        return pd.DataFrame(data)

    def actualizarCampo(self, post_id, campo, valor):
        """Actualizar un campo específico de un post"""
        objdatos = BlogData()
        data = objdatos.objetoDatos()

        for post in data:
            if post["id"] == post_id:
                if campo in post:
                    post[campo] = valor

                    df = pd.DataFrame(data)

                    path = "data/archivos/"
                    file = "dataBlog.csv"
                    fileHTML = "dataBlog.html"
                    os.makedirs(path, exist_ok=True)
                    df.to_csv(f'{path}{file}', index=False)
                    df.to_html(f'{path}{fileHTML}', index=False)

                    print(f" Campo '{campo}' actualizado para ID {post_id}")
                    return df
                else:
                    print(f" Campo '{campo}' no existe en el post")
                    return pd.DataFrame(data)

        print(f"❌ Post con ID {post_id} no encontrado")
        return pd.DataFrame(data)