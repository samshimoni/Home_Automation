import json


class Cfg:
    def __init__(self):
        f = open('cfg.json', )
        data = json.load(f)

        rabbit_params = data['rabbitmq']
        flask_params = data['flask']
        music_server_params = data['music_server']

        self.rabbit_host = rabbit_params['host']
        self.rabbit_port = rabbit_params['port']
        self.rabbit_exchange = rabbit_params['exchange']
        self.rabbit_routing_key = rabbit_params['routing_key_format']
        self.rabbit_username = rabbit_params['username']
        self.rabbit_password = rabbit_params['password']

        self.flask_host = flask_params['host']
        self.flask_port = flask_params['port']

        self.music_server_host = music_server_params['host']
        self.music_server_port = music_server_params['port']