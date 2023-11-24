FROM python:3.11.2-slim

WORKDIR /app
COPY . /app

ENV DJANGO_ENV production

RUN apt-get update -y && apt-get upgrade -y
RUN python -m venv .venv && ./.venv/bin/pip install poetry
RUN ./.venv/bin/poetry install --no-interaction
