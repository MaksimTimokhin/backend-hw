import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='172.18.0.2'))
channel = connection.channel()

channel.queue_declare(queue='emails')

def callback(ch, method, properties, body):
    print(" [x] Received " + body.decode())
    
channel.basic_consume(callback,
                      queue='emails',
                      no_ack=True)

channel.start_consuming()
