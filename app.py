from flask import Flask
from routes import register_routes

def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app

APP = create_app()

if __name__ == "__main__":
    APP.run(host="127.0.0.1", port=5000)
