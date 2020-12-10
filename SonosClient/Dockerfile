FROM python:3
RUN apt-get update

WORKDIR /usr/src/app

COPY sonos.py /usr/src/app
COPY cfg.json /usr/src/app
COPY cfg_sonos.py /usr/src/app
COPY logger.py /usr/src/app
COPY device.py /usr/src/app
COPY app.py /usr/src/app


RUN pip3 install --user app \
Flask==1.1.2 \
soco==0.20 \
python-logging-rabbitmq==2.0.0 \
requests~=2.22.0


EXPOSE 8000

CMD python3 app.py
