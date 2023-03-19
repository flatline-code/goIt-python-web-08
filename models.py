from mongoengine import Document, CASCADE
from mongoengine.fields import ListField, StringField, ReferenceField, BooleanField


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()

class Contact(Document):
    fullname = StringField()
    email = StringField()
    recievedMessage = BooleanField(default=False)
    address = StringField()