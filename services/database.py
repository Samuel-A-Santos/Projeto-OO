from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from mongoengine import connect
import os

uri = os.getenv("MONGO_URI", "mongodb://mongo:27017")

client = None

def conectar_banco():
    global client
    client = MongoClient(uri, server_api=ServerApi('1'))
    connect(host=uri, alias='default')  # Adicione o alias 'default' para a conexão padrão
    print("Conexão com o banco de dados inicializada.")

def testar_conexao():
    try:
        client.admin.command('ping')
        print("Conexão bem-sucedida! Você está conectado ao MongoDB.")
        return True
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return False

if __name__ == "__main__":
    conectar_banco()
    testar_conexao()