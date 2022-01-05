FROM python:3.8-slim

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    gdal-bin \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    gcc \
    libc-dev \
    bash \
    git \
    binutils \
    libproj-dev \
    && pip3 install --upgrade pip


ENV LIBRARY_PATH=/lib:/usr/lib

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt
