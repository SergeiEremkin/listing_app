FROM python:3.10.6
ENV POETRY_VIRTUALENVS_CREATE=false
WORKDIR /listing_app
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VERSION="1.5.1"
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${POETRY_HOME}/venv/bin:${PATH}"
COPY poetry.* pyproject.toml /listing_app/
RUN poetry install
COPY . /listing_app
EXPOSE 8000
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait
#CMD ["./docker-entrypoint.sh"]