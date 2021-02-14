# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
# collect static files
#RUN python manage.py collectstatic --noinput
# add and run as non-root user
RUN adduser -D myuser
USER myuser

# copy entrypoint.sh
#COPY entrypoint.sh .
#
## copy project

#
## run entrypoint.sh
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
