import pika
import json

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Notification: {data}")

def start():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    for queue in ['order_created', 'inventory_updated', 'payment_successful']:
        channel.queue_declare(queue=queue)
        channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
    print("Notification Service listening...")
    channel.start_consuming()

if __name__ == "__main__":
    start()
