from mongoengine import Document, DateTimeField, ReferenceField
from models.Funcionario import Funcionario
import datetime

class Ponto(Document):
    funcionario = ReferenceField(Funcionario, required=True)
    data = DateTimeField(default=datetime.datetime.utcnow, required=True)
    entrada = DateTimeField()
    saida = DateTimeField()