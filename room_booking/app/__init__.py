"""
Fabryka aplikacji Flask.
"""
from flask import Flask
from config import config
from app.models import db


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from app.routes.bookings import bookings_bp
    from app.routes.dashboard import dashboard_bp

    app.register_blueprint(bookings_bp)
    app.register_blueprint(dashboard_bp)

    @app.route('/')
    def index():
        return '<h1>System Rezerwacji Sal Konferencyjnych</h1><p>Przejdź do /dashboard</p>'

    return app
