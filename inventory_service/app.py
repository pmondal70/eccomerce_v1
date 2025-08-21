import pika
import json

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Inventory received: {data}")
    if data['quantity'] <= 10:
        print("Inventory OK")
    else:
        print("Inventory Failed")

def start():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='order_created')
    channel.basic_consume(queue='order_created', on_message_callback=callback, auto_ack=True)
    print("Inventory Service listening...")
    channel.start_consuming()

if __name__ == "__main__":
    start()
