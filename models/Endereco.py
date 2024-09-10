from mongoengine import EmbeddedDocument, StringField

class Endereco(EmbeddedDocument):
    rua = StringField(required=True)
    cidade = StringField(required=True)
    estado = StringField(required=True)
    cep = StringField(required=True)