from mongoengine import Document, StringField, IntField

class Cliente(Document):
    nome = StringField(required=True)
    idade = IntField(required=True)
    profissao = StringField(required=True)