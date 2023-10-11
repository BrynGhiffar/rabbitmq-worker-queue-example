import pika, sys
from pika.spec import PERSISTENT_DELIVERY_MODE

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host = 'host.docker.internal', port=5672)
)

channel = connection.channel()
channel.queue_declare(queue = "task_queue", durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=PERSISTENT_DELIVERY_MODE
    )
)
print(f" [x] sent {message}")
connection.close()