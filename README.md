# Home_Automation

run:

rabbitmq:
  1. docker run -d -it --name rabbit --hostname rabbit -p 30000:5672 -p 30001:15672 rabbitmq:management
  2. run init_rabbit.py in order to create logging exchange and queue.

ELK:
  1. git clone https://github.com/deviantony/docker-elk
  2. enter docker-elk and docker-compose up
  
TelegramBot:
  1. change the flask_server id addres in the cfg.json
  2. docker build -t telegram_bot ${TELEGRAM_BOT_DIR} 
  3. docker run ${name of the container}
  
 MusicServer:
  1. cd MusicServer
  2. docker build -t music_server .
  3. docker run  --network host music_server
  4. docker exec -it music_server bash
  5. service apache2 start
  
 PlantWatering:
 1. run app.py or use auto_water.py
 2. in linux systems : use "cronteb -e" => '30 12 * * 1 wget http://localhost:8000/plant/auto_water'


