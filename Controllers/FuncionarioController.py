from models.Funcionario import Funcionario
from models.Endereco import Endereco
from models.Ponto import Ponto
import datetime
from bson import ObjectId
from collections import defaultdict

def Incluir(funcionario, endereco):
    funcionario.endereco = endereco
    funcionario.save()

def SelecionarById(id):
    try:
        return Funcionario.objects(id=ObjectId(id)).first()
    except:
        return None

def SelecionarByUsername(username):
    try:
        return Funcionario.objects(username=username).first()
    except:
        return None

def Alterar(funcionario, endereco):
    funcionario.endereco = endereco
    funcionario.save()

def Excluir(id):
    try:
        Funcionario.objects(id=ObjectId(id)).delete()
    except:
        pass

def SelecionarTodos():
    return Funcionario.objects()

def RegistrarPontoEntrada(funcionario_id):
    funcionario = SelecionarById(funcionario_id)
    if funcionario:
        hoje = datetime.datetime.utcnow().date()
        ponto_existente = Ponto.objects(funcionario=funcionario, entrada__gte=hoje).first()
        if ponto_existente:
            return None  
        ponto = Ponto(funcionario=funcionario, entrada=datetime.datetime.utcnow())
        ponto.save()
        return ponto
    return None

def RegistrarPontoSaida(funcionario_id):
    funcionario = SelecionarById(funcionario_id)
    if funcionario:
        ponto = Ponto.objects(funcionario=funcionario, saida=None).order_by('-entrada').first()
        if ponto:
            ponto.saida = datetime.datetime.utcnow()
            ponto.save()
            return ponto
    return None

def SelecionarPontos(funcionario_id):
    funcionario = SelecionarById(funcionario_id)
    if funcionario:
        pontos = Ponto.objects(funcionario=funcionario).order_by('-data')
        for ponto in pontos:
            ponto.data_formatada = ponto.data.strftime("%d/%m/%Y - %H:%M:%S")
            ponto.entrada_formatada = ponto.entrada.strftime("%d/%m/%Y - %H:%M:%S") if ponto.entrada else None
            ponto.saida_formatada = ponto.saida.strftime("%d/%m/%Y - %H:%M:%S") if ponto.saida else None
        return pontos
    return []

def AgruparPontosPorDiaMes(funcionario_id):
    funcionario = SelecionarById(funcionario_id)
    if funcionario:
        pontos = Ponto.objects(funcionario=funcionario).order_by('-data')
        pontos_agrupados = defaultdict(list)
        for ponto in pontos:
            chave = ponto.data.strftime("%d/%m/%Y")
            ponto.entrada_formatada = ponto.entrada.strftime("%d/%m/%Y - %H:%M:%S") if ponto.entrada else None
            ponto.saida_formatada = ponto.saida.strftime("%d/%m/%Y - %H:%M:%S") if ponto.saida else None
            pontos_agrupados[chave].append(ponto)
        return pontos_agrupados
    return {}