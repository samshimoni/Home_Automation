import logging
from python_logging_rabbitmq import RabbitMQHandler
from cfg_sonos import Cfg


class Logger:
    def __init__(self, service_name):
        self.cfg = Cfg()
        self.logger = logging.getLogger(service_name)
        self.logger.setLevel(logging.DEBUG)

        rabbit = RabbitMQHandler(host=self.cfg.rabbit_host,
                                 port=self.cfg.rabbit_port,
                                 exchange=self.cfg.rabbit_exchange,
                                 routing_key_format=self.cfg.rabbit_routing_key,
                                 username=self.cfg.rabbit_username,
                                 password=self.cfg.rabbit_password)

        self.logger.addHandler(rabbit)
        formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(message)s')
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
