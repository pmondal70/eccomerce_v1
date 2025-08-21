import pika
import json

def publish_order_created(order_id, item_id, quantity):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='order_created')
    event = {"order_id": order_id, "item_id": item_id, "quantity": quantity}
    channel.basic_publish(exchange='', routing_key='order_created', body=json.dumps(event))
    connection.close()
