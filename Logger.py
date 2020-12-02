import logging
import json
from python_logging_rabbitmq import RabbitMQHandler


class Logger:
    def __init__(self, service_name):

        f = open('cfg.json',)
        data = json.load(f)
        self.name = service_name
        self.logger = logging.getLogger(service_name)
        self.logger.setLevel(logging.DEBUG)

        rabbit_params = data['rabbitmq']
        rabbit = RabbitMQHandler(host=rabbit_params['host'],
                                 port=rabbit_params['port'],
                                 exchange=rabbit_params['exchange'],
                                 routing_key_format=rabbit_params['routing_key_format'],
                                 username=rabbit_params['username'],
                                 password=rabbit_params['password'])

        self.logger.addHandler(rabbit)
        formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(message)s')
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)