FROM python:3.12

# set environment variables
ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONPATH=/usr/src/app

RUN mkdir -p $PYTHONPATH
RUN mkdir -p $PYTHONPATH/staticfiles
RUN mkdir -p $PYTHONPATH/media

# where the code lives
WORKDIR $PYTHONPATH

RUN apt-get update && apt-get upgrade -y && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev \
  # curl
  curl \
  # translations
  gettext \
  # uuid generator
  uuid-runtime

# install pip/setuptools
RUN pip install --upgrade pip
RUN pip install setuptools

# install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "/root/.local/bin:$PATH"

# copy poetry files
COPY pyproject.toml poetry.lock ./
# disable virtualenv creation by poetry
ENV POETRY_VIRTUALENVS_CREATE=false
# install dependencies
RUN poetry install --no-dev --no-root

# install app
COPY . .
p
