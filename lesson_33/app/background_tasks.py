# Zadanie 15 – Background Tasks
# Do API książek dodaj:
# Po utworzeniu książki: background task wysyła "email" (log do pliku)
# (challenge)
# Po usunięciu: background task aktualizuje statystyki
# CREATE - tworzenie ksiazki

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def write_to_log_file(book_name: str):
    with open("logs.txt", "a") as f:
        f.write(f"Book {book_name} added!\n")

async def log_book_deleted(book_name: str):
    logger.info(f"Book {book_name} deleted!")