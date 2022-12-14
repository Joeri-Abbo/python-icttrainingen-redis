FROM python:3.11.0-alpine3.15

RUN apk add mariadb-dev gcc libc-dev

RUN python -m pip install --upgrade pip
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

WORKDIR /usr/src/app