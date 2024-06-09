FROM python:3.12

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml ../poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY .. .

CMD ["uvicorn", "bochka.main:app", "--host", "0.0.0.0", "--port", "8000"]