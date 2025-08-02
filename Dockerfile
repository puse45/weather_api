## start from an official image
#FROM python:3.8
#
#MAINTAINER Pius Musyoki
#
## Python Domain
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## arbitrary location choice: you can change the directory
#RUN mkdir -p /backend
#WORKDIR /backend
#
## install dependencies
#RUN pip install --upgrade pip
#COPY ./requirements.txt /requirements.txt
#RUN pip install -r /requirements.txt
#
## copy our project code
#COPY . /backend
#RUN chmod a+x /backend/entrypoint.sh
#RUN chmod a+x /backend/wait-for-it.sh
#
## define the default command to run when starting the container
#ENTRYPOINT ["/backend/entrypoint.sh"]

FROM python:3.8-slim

MAINTAINER Pius Musyoki

# Install system dependencies
RUN apt-get update && \
    apt-get install -y netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=project.settings.rancher

RUN mkdir -p /backend
WORKDIR /backend

# Install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy project
COPY . /backend

# Set up entrypoint
COPY rancher-entrypoint.sh /backend
RUN chmod +x /backend/rancher-entrypoint.sh

ENTRYPOINT ["/backend/rancher-entrypoint.sh"]
