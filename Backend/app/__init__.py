from flask import Flask
from flask_cors import CORS
from config import Config
from .routes.controller_bp import usuario_bp, servidor_bp, canal_bp, chat_bp
from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    CORS(app, supports_credentials=True)
    app.config.from_object(
        Config
    )
    DatabaseConnection.set_config(app.config)
    app.register_blueprint(usuario_bp, url_prefix = '/usuarios')
    app.register_blueprint(servidor_bp, url_prefix = '/servidores')
    app.register_blueprint(canal_bp, url_prefix = '/canal')
    app.register_blueprint(chat_bp, url_prefix = '/chat')
    return app