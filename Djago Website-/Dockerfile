# use python:3.7-slim image as base image
#put the files that do not change on the top
FROM python:3.7-slim as production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

# RUN apt-get update && \
#     apt-get install -y \
#     bash \
#     build-essential \
#     gcc \
#     libffi-dev \
#     musl-dev \
#     openssl \
#     postgresql \
#     libpq-dev

COPY requirements/prod.txt ./requirements/prod.txt
RUN pip install -r ./requirements/prod.txt

COPY manage.py ./manage.py
COPY djangoWebsite ./djangoWebsite
#port
EXPOSE 8000

FROM production as development

COPY requirements/dev.txt ./requirements/dev.txt
RUN pip install -r ./requirements/dev.txt

COPY . .