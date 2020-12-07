FROM python:3
RUN apt-get update
 
WORKDIR /usr/src/app

COPY telegram_bot.py /usr/src/app
COPY cfg.json /usr/src/app
COPY cfg_automation.py /usr/src/app
COPY logger.py /usr/src/app

RUN pip3 install --user app legofy==1.0.0 \
telegram==0.0.1 \
python_telegram_bot==13.1 \
requests==2.18.4 \
python-logging-rabbitmq==2.0.0


CMD python3 telegram_bot.py


