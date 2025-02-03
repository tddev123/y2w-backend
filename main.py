# from flask import Flask

# from app.routes.download import download_bp


# def create_app():
#     app = Flask(__name__)
#     app.register_blueprint(download_bp, url_prefix="/api")
#     return app


# # Create the app instance
# app = create_app()

# # If running under Gunicorn, it will find the app object here
# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=6000)
from fastapi import FastAPI

from app.routes.download import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Hello World"}
