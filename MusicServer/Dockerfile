FROM python:3
RUN apt-get update

RUN apt install python3-pip -y

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


EXPOSE 80
EXPOSE 8000

CMD ["python3", "app.py"]
