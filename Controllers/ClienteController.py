from models.Cliente import Cliente
from models.Endereco import Endereco

def Incluir(cliente, endereco):
    cliente.endereco = endereco
    cliente.save()

def SelecionarById(id):
    return Cliente.objects(id=id).first()

def Alterar(cliente, endereco):
    cliente.endereco = endereco
    cliente.save()

def Excluir(id):
    Cliente.objects(id=id).delete()

def SelecionarTodos():
    return Cliente.objects()