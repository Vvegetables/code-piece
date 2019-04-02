import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
#发送一条信息
channel.basic_publish(exchange="",
                      routing_key="hello",
                      body="Hello World")
print(" [x] Sent 'Hello World!'")
connection.close()