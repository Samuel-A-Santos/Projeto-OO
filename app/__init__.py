from flask import Flask
from app.routes import init_routes

def create_app():
    app = Flask(__name__)
    app.secret_key = 'sua_chave_secreta_aqui'
    init_routes(app)
    return app