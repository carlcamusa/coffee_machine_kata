# set base image (host OS)
FROM python:3.8-slim

RUN apt-get update && apt-get install -y --no-install-recommends git && apt-get clean && rm -rf /var/lib/apt/lists/*

# set the working directory in the container
WORKDIR /code

# install dependencies
ENV POETRY_VIRTUALENVS_CREATE false
RUN pip3 install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install

# copy the content of the local directory to the working directory
COPY . .