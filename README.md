# Home_Automation

run:

rabbitmq:
  1. docker run -d -it --name rabbit --hostname rabbit -p 30000:5672 -p 30001:15672 rabbitmq:management

ELK:
  1. git clone https://github.com/deviantony/docker-elk
  2. enter docker-elk and docker-compose up
  
TelegramBot:
  1. change the flask_server id addres in the cfg.json
  2. docker build ${PATH} 
  3. docker run ${name of the container}


