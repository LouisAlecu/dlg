from flask import Flask
from config import ProductionConfig
from views import total_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)
    app.register_blueprint(total_blueprint)

    return app
