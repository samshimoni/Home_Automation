import json


class Cfg:
    def __init__(self):
        f = open('cfg.json', )
        data = json.load(f)

        rabbit_params = data['rabbitmq']
        flask_params = data['flask']
        plant_params = data['plant']
        telegram_params = data['telegram']
        sonos_params = data['sonos']

        self.rabbitHost = rabbit_params['host']
        self.rabbitPort = rabbit_params['port']
        self.rabbitExchange = rabbit_params['exchange']
        self.rabbitRoutingKey = rabbit_params['routing_key_format']
        self.rabbitUserName = rabbit_params['username']
        self.rabbitPassword = rabbit_params['password']

        self.flaskAddress = flask_params['host']
        self.flaskPort = flask_params['port']

        self.plantAddress = plant_params['host']
        self.plantPort = plant_params['port']

        self.sonosAddress = sonos_params['host']
        self.sonosPort = sonos_params['port']

        self.telegramToken = telegram_params['token']