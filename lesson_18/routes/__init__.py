from routes.bookings import bookings_bp
from routes.dashboard import dashboard_bp
from routes.debug import debug_bp
from routes.main import main_bp
from routes.notifications import notifications_bp
from routes.reports import reports_bp


def register_routes(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(debug_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(notifications_bp)
    app.register_blueprint(bookings_bp)
    app.register_blueprint(reports_bp)
