import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#sender 和 receiver之间的通信通道
channel = connection.channel()
#申明一个消息队列
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

#配置woker
channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()