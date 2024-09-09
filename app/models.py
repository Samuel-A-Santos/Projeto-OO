from mongoengine import Document, StringField, IntField

class Usuario(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

class Cliente(Document):
    nome = StringField(required=True)
    idade = IntField(required=True)
    profissao = StringField(required=True)