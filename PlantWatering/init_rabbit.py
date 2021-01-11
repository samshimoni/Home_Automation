import pika
import cfg_watering

'''
    this script simply initiate the queue exchange and bind them together 
'''

cfg = cfg_watering.Cfg()

connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.rabbitHost, port=cfg.rabbitPort))

channel = connection.channel()

channel.queue_declare(queue=cfg.rabbitQueue, durable=True)

channel.exchange_declare(exchange=cfg.rabbitExchange, exchange_type=cfg.rabbitExchangeType)

channel.queue_bind(exchange=cfg.rabbitExchange, queue=cfg.rabbitQueue, routing_key=cfg.rabbitRoutingKey)
