FROM python:3.13-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia todo el contenido del proyecto de forma masiva
COPY . /code

EXPOSE 8000

CMD ["fastapi", "run", "main.py", "--port", "8000"]
