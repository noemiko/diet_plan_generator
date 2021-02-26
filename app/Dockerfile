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

RUN poetry run pytest

# add and run as non-root user
#RUN adduser -D myuser
#USER myuser

# copy entrypoint.sh
#COPY entrypoint.sh .
#
## copy project

#
## run entrypoint.sh
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
#RUN pip install -r requirements.txt
#COPY . .
## collect static files
#RUN python manage.py collectstatic --noinput
# add and run as non-root user
#RUN adduser -D myuser
#USER myuser

# copy entrypoint.sh
#COPY entrypoint.sh .
#
## copy project

#
## run entrypoint.sh
#RUN apt-get update && apt-get -y dist-upgrade
#RUN apt-get -y install build-essential libssl-dev libffi-dev libblas3 libc6 liblapack3 gcc python3-dev python3-pip cython3
#RUN apt-get -y install python3-numpy python3-scipy
#RUN apt install -y netcat
##RUN /usr/src/app/entrypoint.sh
#FROM main AS testing
#
#RUN apt-get install build-dep python-psycopg2
#
#RUN poetry install
#
#RUN poetry run pytest
