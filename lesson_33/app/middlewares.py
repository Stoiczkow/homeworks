# Zadanie 16 – Middleware Logging
# Stwórz middleware który:
# (challenge)
# Loguje wszystkie requesty (metoda, path, czas)
# Dodaje header X-Request-ID do każdego response
# Zapisuje logi do pliku requests.log

from fastapi import Request
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="requests.log"
)

logger = logging.getLogger(__name__)


async def log_requests_and_add_headers(request: Request, call_next):
    start_time = time.time()

    logger.info(
        f"START {request.method} {request.url.path}"
    )

    response = await call_next(request)

    process_time = time.time() - start_time

    request_id = str(id(request))

    response.headers["X-Request-ID"] = request_id

    logger.info(
        f"END {request.method} {request.url.path} "
        f"completed in {process_time:.3f}s "
        f"request_id={request_id}"
    )

    return response