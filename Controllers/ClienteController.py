from models.Cliente import Cliente

def Incluir(cliente):
    cliente.save()

def SelecionarById(id):
    return Cliente.objects(id=id).first()

def Alterar(cliente):
    cliente.save()

def Excluir(id):
    Cliente.objects(id=id).delete()

def SelecionarTodos():
    return Cliente.objects()