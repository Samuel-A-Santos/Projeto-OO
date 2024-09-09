from flask import Flask
from services.database import conectar_banco

def create_app():
    app = Flask(__name__)
    conectar_banco()

    with app.app_context():
        from .routes import init_routes
        init_routes(app)
        
    return app