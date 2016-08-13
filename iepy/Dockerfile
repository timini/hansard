from python:3.4

RUN pip install numpy

RUN pip install iepy

RUN apt-get update && apt-get install -y openjdk-7-jre

ENV JAVAHOME=/usr/bin/java

RUN mkdir /root/.config

RUN iepy --download-third-party-data

COPY ./hansard /hansard

RUN pip install psycopg2

EXPOSE 8001

CMD python /hansard/bin/manage.py runserver 0.0.0.0:8001
