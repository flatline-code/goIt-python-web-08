import pika
import faker
import connect

from models import Contact


fake = faker.Faker()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='send_messeges', exchange_type='direct')
channel.queue_declare(queue='contacts_queue', durable=True)
channel.queue_bind(exchange='send_messeges', queue='contacts_queue')

def main():
    for _ in range(10):
        add_contact = Contact(
            fullname=fake.name(),
            email=fake.email(),
            address=fake.address(),
        )
        add_contact.save()

    contacts = Contact.objects()

    for contact in contacts:
        channel.basic_publish(
            exchange='send_messeges',
            routing_key='contacts_queue',
            body=f"{contact.id}".encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print('contacts created')
    connection.close()

if __name__ == '__main__':
    main()