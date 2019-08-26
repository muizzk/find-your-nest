FROM debian:10

RUN apt-get update

RUN apt-get install -y python3 python3-pip libpq-dev
    
RUN pip3 install flask flask-login opencage passlib 

COPY . /app

EXPOSE 5000

WORKDIR /app

CMD python3 main.py
