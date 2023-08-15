FROM python:3.10

RUN apt-get update && apt-get install -y python3-gdal gdal-bin

ENV PYTHONUNBUFFERED 1
ENV APP_HOME /heaven


WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME/
RUN pip install -r requirements.txt

RUN adduser --disabled-password admin-user
USER admin-user
