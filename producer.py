import pika

import time
time.sleep(0.01)  # Ritardo di 10 ms tra i messaggi

print('collegato a rabbit')

params = pika.ConnectionParameters(host="localhost")
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='worker_queue')

print('eseguito!')

i = 0
while True:
    message = str(i)
    i += 1

    channel.basic_publish(exchange='', routing_key='worker_queue', body=message)
    print('messaggio inviato', message)

    if i > 1000:
        break

connection.close()    