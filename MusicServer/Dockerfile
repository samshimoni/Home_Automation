FROM ubuntu:latest

RUN apt-get update
RUN apt-get install curl -y
RUN apt-get install vim -y
RUN apt install python3-pip -y

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install apache2 -y

WORKDIR /usr/src/app

COPY app.py /usr/src/app
COPY cfg.json /usr/src/app
COPY cfg_automation.py /usr/src/app
COPY logger.py /usr/src/app
COPY music_server.py /usr/src/app
COPY device.py /usr/src/app

RUN pip3 install --user app \
Flask==1.1.2 \
python-logging-rabbitmq==2.0.0

COPY music /var/www/html/music/

EXPOSE 80
EXPOSE 8000

CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
CMD ["service", "apache2", "start"]
CMD ["python3", "app.py"]
