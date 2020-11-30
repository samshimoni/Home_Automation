import logging

from python_logging_rabbitmq import RabbitMQHandler

logger = logging.getLogger('my_service')
logger.setLevel(logging.DEBUG)

rabbit = RabbitMQHandler(host='localhost',
                         port=30000,
                         exchange='logs',
                         routing_key_format='logs-api-1',
                         username='guest',
                         password='guest')
logger.addHandler(rabbit)

formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)


