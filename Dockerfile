FROM python:3.12.0-slim

WORKDIR /app
COPY . /app

RUN apt-get update -y && apt-get upgrade -y
RUN python -m venv .venv && ./.venv/bin/pip install poetry
RUN ./.venv/bin/poetry install --no-interaction
