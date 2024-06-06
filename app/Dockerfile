# Pull de la imagen base oficial
FROM python:3.9.6-alpine

# setup del directorio de trabajo
WORKDIR /code
COPY . .

# Configuración de las variables de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

ENTRYPOINT python main.py

