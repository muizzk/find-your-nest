FROM debian:10

RUN apt-get update

RUN apt-get install -y python3 python3-pip libpq-dev 

RUN pip3 install flask

COPY . /app

EXPOSE 8080

WORKDIR /app

CMD bash
