from flask import Flask
from config import config
from app.models import db

from app.routes.rooms import rooms_bp
from app.routes.bookings import bookings_bp
from app.routes.dashboard import dashboard_bp
from app.routes.notifications import notifications_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(config["development"])

    db.init_app(app)

    app.register_blueprint(rooms_bp)
    app.register_blueprint(bookings_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(notifications_bp)

    @app.route("/test-db")
    def test_db():
        try:
            db.session.execute(db.text("SELECT 1"))
            return {"message": "Połączenie OK!"}, 200
        except Exception as e:
            return {"error": str(e)}, 500

    return app