from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from mongoengine import connect

uri = "mongodb://localhost:27017"  # Certifique-se de que a URI está correta para o ambiente local

client = None

def conectar_banco():
    global client
    client = MongoClient(uri, server_api=ServerApi('1'))
    connect(host=uri)  # Adicionar esta linha para conectar o MongoEngine
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