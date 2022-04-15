FROM python:3.9 as build

WORKDIR /app

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.13

RUN pip install "poetry==$POETRY_VERSION"
COPY poetry.lock pyproject.toml /app/
COPY Makefile /app/Makefile
COPY thirdweb /app/thirdweb
COPY docs /app/docs
COPY README.md /app/README.md
COPY docs/mkdocs/mkdocs.yml /app/mkdocs/mkdocs.yml

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

RUN poetry shell && cd docs/mkdocs && poetry run mkdocs build

FROM halverneus/static-file-server

WORKDIR /docs

COPY --from=build /app/docs/mkdocs/site /docs/mkdocs/site
ENV FOLDER=/docs/mkdocs/site