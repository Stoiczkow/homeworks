from flask import Blueprint
from sqlalchemy import text

from extensions import db


main_bp = Blueprint("main", __name__)


@main_bp.get("/")
def index():
    return "Flask + PostgreSQL działa!"


@main_bp.get("/test-db")
def test_db():
    try:
        db.session.execute(text("SELECT 1"))
        return "Połączenie OK!"
    except Exception as error:
        return f"Błąd połączenia: {error}", 500
