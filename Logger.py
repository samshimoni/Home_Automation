import logging
import json

from python_logging_rabbitmq import RabbitMQHandler


class Logger:
    def __init__(self, service_name):
        f = open('cfg.json',)
        data = json.load(f)
        print(data['Logger'])
        self.name = service_name
        self.logger = logging.getLogger('hello')
        self.logger.setLevel(logging.DEBUG)

        rabbit = RabbitMQHandler(host='localhost',
                                 port=[0],
                                 exchange='logs',
                                 routing_key_format='logs-api-1',
                                 username='guest',
                                 password='guest')

        self.logger.addHandler(rabbit)

        formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(message)s')
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)


logger = Logger('logger')