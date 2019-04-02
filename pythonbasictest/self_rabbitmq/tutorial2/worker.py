import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)
print(" [*] Waiting for messages. To exit press CTRL+C")

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag) #auto_ack=False需要手动表示消息已经处理完

#消息或者任务公平分派
channel.basic_qos(prefetch_count=1)
#配置消费者
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()