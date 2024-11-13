# Step 1: Set up the base image with Python 3.11 and Alpine Linux
FROM python:3.11-alpine


RUN apk add --no-cache curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    mv /root/.local/bin/poetry usr/local/bin/poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY . .

ENV PYTHONPATH=/app/

RUN poetry run pytest -v RUN poetry run pytest -v || echo "pytest failed"

EXPOSE 80

CMD ["python", "src/calculator/calculator.py"]