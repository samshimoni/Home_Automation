import json


class Cfg:
    def __init__(self):
        f = open('cfg.json', )
        data = json.load(f)

        rabbit_params = data['rabbitmq']
        flask_params = data['flask']
        music_server_params = data['music_server']

        self.rabbitHost = rabbit_params['host']
        self.rabbitPort = rabbit_params['port']
        self.rabbitExchange = rabbit_params['exchange']
        self.rabbitRoutingKey = rabbit_params['routing_key_format']
        self.rabbitUserName = rabbit_params['username']
        self.rabbitPassword = rabbit_params['password']

        self.flaskAddress = flask_params['host']
        self.flaskPort = flask_params['port']

        self.music_server_host = music_server_params['host']
