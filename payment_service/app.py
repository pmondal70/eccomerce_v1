import pika
import json

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Payment received: {data}")
    print("Payment successful")

def start():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='inventory_updated')
    channel.basic_consume(queue='inventory_updated', on_message_callback=callback, auto_ack=True)
    print("Payment Service listening...")
    channel.start_consuming()

if __name__ == "__main__":
    start()
