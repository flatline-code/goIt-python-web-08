import pika
import connect

from models import Contact

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='contacts_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    def callback(ch, method, properties, body):
        contact_id = body.decode()
        print(f" [x] Received {contact_id}")
        contact = Contact.objects(id=contact_id)
        contact.update(recievedMessage=True)
        print(f" [x] Done: {method.delivery_tag}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='contacts_queue', on_message_callback=callback)
    channel.start_consuming()

if __name__ == '__main__':
    main()    