import services.database as db
from app import create_app

print("Inicializando a conexão com o banco de dados...")
db.conectar_banco()  

print("Criando a aplicação Flask...")
app = create_app()

if __name__ == "__main__":
    print("Iniciando o servidor Flask...")
    app.run(host="0.0.0.0", port=5000, debug=True)