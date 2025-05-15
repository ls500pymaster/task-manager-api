FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry

ENV POETRY_HTTP_TIMEOUT=200 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root --only main,dev \
 && mkdir -p /app/staticfiles

COPY . /app/

ENV DJANGO_SECRET_KEY=secret-for-docker-build
RUN python manage.py collectstatic --noinput
EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
