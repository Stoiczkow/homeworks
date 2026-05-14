from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify
from sqlalchemy import text

from app.models import db


def create_app():
	load_dotenv(Path(__file__).resolve().parent.parent / '.env')

	app = Flask(__name__)
	app.config.from_object('config.Config')

	db.init_app(app)

	from app.routes.bookings import bookings_bp
	from app.routes.dashboard import dashboard_bp
	from app.routes.debug import debug_bp
	from app.routes.notifications import notifications_bp
	from app.routes.reports import reports_bp

	app.register_blueprint(bookings_bp)
	app.register_blueprint(dashboard_bp)
	app.register_blueprint(debug_bp)
	app.register_blueprint(notifications_bp)
	app.register_blueprint(reports_bp)

	@app.route('/')
	def index():
		return jsonify({
			'app': 'room_booking',
			'status': 'ok',
			'dashboard': '/dashboard'
		})

	@app.route('/test-db')
	def test_db():
		try:
			db.session.execute(text('SELECT 1'))
			return jsonify({
				'message': 'Połączenie OK!',
				'database_uri': app.config['SQLALCHEMY_DATABASE_URI']
			})
		except Exception as exc:
			return jsonify({
				'message': 'Błąd połączenia z bazą',
				'error': str(exc)
			}), 500

	return app
