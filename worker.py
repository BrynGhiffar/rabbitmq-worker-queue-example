import pika, time
from pika.channel import Channel
from pika.spec import Basic, BasicProperties
from pika.adapters.blocking_connection import BlockingChannel


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="host.docker.internal", port=5672)
)

channel: BlockingChannel = connection.channel()

channel.queue_declare('task_queue', durable=True)

print("Waiting for messages")

def callback(ch: Channel, method: Basic.Deliver, properties: BasicProperties, body: bytes):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count = 1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()