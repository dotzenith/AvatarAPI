FROM python:3.10

RUN mkdir /app 
COPY . /app

WORKDIR /app

# Upgrade pip, install poetry and gunicorn
RUN pip3 install -U pip poetry gunicorn

# Already in a container, venv largely not needed
RUN poetry config virtualenvs.create false

# Install the package and dependencies without ansi output
RUN poetry install --without dev --no-interaction --no-ansi

# Run gunicorn with special workers
ENTRYPOINT [ "gunicorn","-w 3", "-k uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:5000",  "avatarapi.main:app" ]
