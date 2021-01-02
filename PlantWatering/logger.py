import logging
from python_logging_rabbitmq import RabbitMQHandler
from cfg_watering import Cfg


class Logger:
    def __init__(self, service_name):
        self.cfg = Cfg()
        self.logger = logging.getLogger(service_name)
        self.logger.setLevel(logging.DEBUG)

        rabbit = RabbitMQHandler(host=self.cfg.rabbitHost,
                                 port=self.cfg.rabbitPort,
                                 exchange=self.cfg.rabbitExchange,
                                 routing_key_format=self.cfg.rabbitRoutingKey,
                                 username=self.cfg.rabbitUserName,
                                 password=self.cfg.rabbitPassword)

        self.logger.addHandler(rabbit)
        formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(message)s')
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)