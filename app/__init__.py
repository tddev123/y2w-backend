from flask import Flask
from .routes.download import download_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(download_bp, url_prefix="/api")
    return app
