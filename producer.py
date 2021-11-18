import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = {'id': 1, 'name': 'name1'}
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=json.dumps(message),
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()
