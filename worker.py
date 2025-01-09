import pika
import time

# Ritardo di 10 ms tra i messaggi
time.sleep(0.01)

print('Collegato a RabbitMQ')

# Parametri di connessione
params = pika.ConnectionParameters(host="localhost")
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Dichiarazione della coda
channel.queue_declare(queue='worker_queue')

print('Eseguito!')

# Callback per gestire i messaggi ricevuti
def callback(ch, method, properties, body):
    print('Ricevuto:', body)

# Configura il consumo dalla coda
channel.basic_consume(
    queue='worker_queue', 
    on_message_callback=callback, 
    auto_ack=True
)

# Avvia il consumo
print('In attesa di messaggi...')
channel.start_consuming()
