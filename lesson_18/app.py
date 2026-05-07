from flask import Flask

from config import config
from extensions import db
from routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(config["default"])

    db.init_app(app)
    register_routes(app)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
