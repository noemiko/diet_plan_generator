# pull official base image
FROM python:3.9.2 as main

# set work directory
WORKDIR /app
ADD . /app

# set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install dependencies
RUN pip install --upgrade pip
RUN pip install poetry
ENV PATH="${PATH}:/root/.poetry/bin"

COPY . .
RUN poetry export -f requirements.txt -o requirements.txt

RUN pip install -r requirements.txt
# collect static files
RUN python manage.py collectstatic --noinput

FROM main AS testing

RUN poetry install

RUN poetry run pytest -k 'not django_db'