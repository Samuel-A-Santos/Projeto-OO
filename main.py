import services.database as db
from app import create_app

db.conectar_banco()  # Certifique-se de que a conexão com o banco de dados é inicializada

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)