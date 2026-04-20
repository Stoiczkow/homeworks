from flask import Flask
from sqlalchemy import event
from app.models import db
from app.routes.rooms import rooms_bp
from app.routes.bookings import bookings_bp
from app.routes.dashboard import dashboard_bp
from config import config

query_counter = {"count": 0}

def create_app():
    app = Flask(__name__)
    app.config.from_object(config["development"])

    db.init_app(app)

    with app.app_context():
        @event.listens_for(db.engine, "before_cursor_execute")
        def count_queries(conn, cursor, statement, parameters, context, executemany):
            query_counter["count"] += 1

    app.config["QUERY_COUNTER"] = query_counter

    app.register_blueprint(rooms_bp)
    app.register_blueprint(bookings_bp)
    app.register_blueprint(dashboard_bp)

    return app