# Home_Automation

rabbitmq:
  1. docker run -d -it --name rabbit --hostname rabbit -p 30000:5672 -p 30001:15672 rabbitmq:management
  2. ./initRabbit.py in order to create logging exchange and queue.


ELK:
  1. 
    a.git clone https://github.com/deviantony/docker-elk (for x86) 
    b.git clone https://github.com/stefanwalther/rpi-docker-elk.git (for Arm)
    
    
  2. enter logstash.conf and add rabbitmq pipe:
    
    input {
    rabbitmq {
        port => 30000
        host => "yourIpAddress"
	  queue => "logs"
        durable => true
	  exchange => "logs"
	  key => "logs-api-1"
      }
    }
  
  3. enter docker-elk and docker-compose up
  

TelegramBot:
  1. change the flask_server id addres in the cfg.json
  2. docker build -t telegram_bot ${TELEGRAM_BOT_DIR} 
  3. docker run -d -it ${name of the container}
  
 MusicServer:
  a. You need to Have apache service running at your Linux Sever.
  1. cd MusicServer
  2. docker build -t music_server .
  3. docker run -d -it -v /var/www/html/music/:/var/www/html/music --network host music_server

 
 PlantWatering:
 1. run app.py or use auto_water.py
 2. in linux systems : use "cronteb -e" => '30 12 * * 1 wget http://localhost:8000/plant/auto_water'
 


