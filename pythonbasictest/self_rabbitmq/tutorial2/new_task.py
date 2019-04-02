import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)
channel = connection.channel()

#durable=True 表示消息可持久化，服务断开时，会将未处理的消息保存在本地
channel.queue_declare(queue="task_queue", durable=True)

message = " ".join(sys.argv[1:]) or "Hello World"
channel.basic_publish(
    exchange="",
    routing_key="task_queue",
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2, #make message persistent
    )
)

print(" [x] Sent %r" % message)
connection.close()