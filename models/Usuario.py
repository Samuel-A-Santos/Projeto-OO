from mongoengine import Document, StringField

class Usuario(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)