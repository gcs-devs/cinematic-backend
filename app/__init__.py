import os
from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
import logging

mongo = PyMongo()

def create_app(config=None):
    app = Flask(__name__)
    CORS(app)
    if config:
        app.config.from_object(config)

    # Configurar a URI do MongoDB e API Key usando variáveis de ambiente
    app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://mongo:27017/cinematic_db")
    app.config["API_KEY"] = os.getenv("API_KEY")

    # Logar a chave da API para verificação (remova em produção)
    print(f"API_KEY: {app.config['API_KEY']}")

    # Configurar logs
    logging.basicConfig(level=logging.INFO)
    app.logger.setLevel(logging.INFO)

    try:
        # Inicializar a extensão Flask-PyMongo
        mongo.init_app(app)
        app.logger.info("Conectado ao MongoDB com sucesso")
    except Exception as e:
        app.logger.error(f"Erro ao conectar com o MongoDB: {e}")
        raise

    # Importar e registrar blueprints
    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

def get_db():
    return mongo.db

