import json


class Cfg:
    def __init__(self):
        f = open('./cfg.json', )
        data = json.load(f)

        rabbit_params = data['rabbitmq']
        flask_params = data['flask']
        plant_params = data['Plant']
        mail_params = data['Mail']

        self.rabbitHost = rabbit_params['host']
        self.rabbitPort = rabbit_params['port']
        self.rabbitExchange = rabbit_params['exchange']
        self.rabbitExchangeType = rabbit_params['exchange_type']
        self.rabbitQueue = rabbit_params['queue']
        self.rabbitRoutingKey = rabbit_params['routing_key_format']
        self.rabbitUserName = rabbit_params['username']
        self.rabbitPassword = rabbit_params['password']

        self.flaskAddress = flask_params['host']
        self.flaskPort = flask_params['port']

        self.pumpPin = plant_params['pump_pin']
        self.waterSensorPin = plant_params['water_sensor_pin']
        self.waterDelay = plant_params['delay']

        self.subject = mail_params['subject']
        self.frm = mail_params['from']
        self.to = mail_params['to']
        self.userName = mail_params['username']
        self.password = mail_params['password']


