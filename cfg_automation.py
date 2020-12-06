import json


class Cfg:
    def __init__(self):
        f = open('cfg.json', )
        data = json.load(f)

        rabbit_params = data['rabbitmq']
        flask_params = data['flask']

        telegram_params = data['telegram']
        sensibu_params = data['sensibu']
        camera_params = data['camera']

        self.rabbitHost = rabbit_params['host']
        self.rabbitPort = rabbit_params['port']
        self.rabbitExchange = rabbit_params['exchange']
        self.rabbitRoutingKey = rabbit_params['routing_key_format']
        self.rabbitUserName = rabbit_params['username']
        self.rabbitPassword = rabbit_params['password']

        self.flaskAddress = flask_params['host']
        self.flaskPort = flask_params['port']

        self.sensibuUri = sensibu_params['uri']
        self.sensibuToken = sensibu_params['token']

        self.telegramToken = telegram_params['token']

        self.cameraScript = camera_params['camera_capture_script']
        self.camera_photos_dir = camera_params['camera_photos_dir']
