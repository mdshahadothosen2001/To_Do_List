FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./backend/requirements/development.txt /app/backend/requirements/

RUN pip install --no-cache-dir -r backend/requirements/development.txt

COPY . /app

RUN python /app/backend/manage.py collectstatic --noinput --settings=config.settings.dev_settings
