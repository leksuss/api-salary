FROM python:3.12

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock /code/

RUN poetry install --no-root --no-cache

COPY . /code/

CMD ["poetry", "run", "uvicorn", "app.main:fastapi_app", "--host", "0.0.0.0", "--port", "80"]