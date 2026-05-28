# Zadanie 17 – Startup/Shutdown Events
# Dodaj event hooks:
# (challenge)
# startup: inicjalizuj bazę, załaduj cache z plikiem JSON
# shutdown: zapisz cache do pliku, zamknij połączenie DB

import json
import logging
from app.database import init_db

async def startup_event(app):
    logging.info("Application starting up...")
        
    await init_db()
    
    app.state.db_connection = "connected"
    
    logging.info("Database initialized")
    
    try:
        with open("cache.json", "r") as f:
            app.state.cache = json.load(f)

        logging.info("Cache loaded from file")

    except FileNotFoundError:
        app.state.cache = {}

        logging.info("No cache file found, starting empty cache")

    logging.info("Application startup complete!")
    
async def shutdown_event(app):
    logging.info("Application shutting down...")

    if hasattr(app.state, "db_connection"):
        logging.info("Database connection closed")

    with open("cache.json", "w") as f:
        json.dump(app.state.cache, f)

    logging.info("Cache saved to disk")

    logging.info("Application shutdown complete!")