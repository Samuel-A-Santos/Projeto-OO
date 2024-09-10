from mongoengine import Document, StringField, IntField, EmbeddedDocumentField
from models.Endereco import Endereco

class Cliente(Document):
    nome = StringField(required=True)
    idade = IntField(required=True)
    profissao = StringField(required=True)
    endereco = EmbeddedDocumentField(Endereco, required=True)