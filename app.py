from flask import Flask
from .routes.download import download_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(download_bp, url_prefix="/api")
    return app

# Create the app instance
app = create_app()

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
