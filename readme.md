# RabbitMQ Worker Queue Example
You can install RabbitMQ on your localhost (not DevContainer) with
```
docker run -d -p 5672:5672 rabbitmq
```
You can send new messages by running
```
python new_task.py <message>
```
You can start the worker with:
```
python worker.py
```