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
from fastapi.middleware.cors import CORSMiddleware
from app.routes.download import router

app = FastAPI()

# Define allowed origins (Update with your frontend domain in production)
origins = [
    "http://localhost:3000",  # Allow local frontend for development
    "https://yourfrontenddomain.com",  # Allow production frontend
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Include router
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Hello World"}

