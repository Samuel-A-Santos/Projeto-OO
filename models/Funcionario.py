from mongoengine import Document, StringField, IntField, EmbeddedDocumentField
from models.Endereco import Endereco

class Funcionario(Document):
    nome = StringField(required=True)
    idade = IntField(required=True)
    profissao = StringField(required=True)
    endereco = EmbeddedDocumentField(Endereco, required=True)
    username = StringField(required=True, unique=True)
    password = StringField(required=True)