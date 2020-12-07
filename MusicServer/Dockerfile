FROM ubuntu:latest

#install all the tools you might want to use in your container
RUN apt-get update
RUN apt-get install curl -y
RUN apt-get install vim -y
RUN apt install python3-pip -y

#the following ARG turns off the questions normally asked for location and timezone for Apache
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install apache2 -y


#change working directory to root of apache webhost
WORKDIR /usr/src/app

COPY app.py /usr/src/app
COPY cfg.json /usr/src/app
COPY cfg_automation.py /usr/src/app
COPY logger.py /usr/src/app
COPY music_server.py /usr/src/app
COPY device.py /usr/src/app
COPY device.py /usr/src/app

RUN pip3 install --user app Flask==1.1.2 \
python-logging-rabbitmq==2.0.0

COPY music /var/www/html/music/

EXPOSE 80
EXPOSE 8000

CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
CMD ["service", "apache2", "start"]
CMD ["python3", "app.py"]
