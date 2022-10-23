FROM python:3.10

RUN mkdir /app 
COPY . /app

WORKDIR /app

#RUN apt-get install build-essential
RUN pip3 install -U pip poetry gunicorn

RUN poetry config virtualenvs.create false
RUN poetry install --without dev --no-interaction --no-ansi

ENTRYPOINT [ "gunicorn","-w 3", "-k uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:5000",  "avatarapi.main:app" ]
