from time import perf_counter

from flask import Blueprint
from sqlalchemy import event
from sqlalchemy.orm import joinedload

from extensions import db
from models import Booking
from seeds import ensure_sample_data


debug_bp = Blueprint("debug", __name__)


@debug_bp.get("/debug/n-plus-1")
def debug_n_plus_1():
    ensure_sample_data()

    regular = measure_queries(lambda: serialize_bookings(Booking.query.all()))
    optimized = measure_queries(
        lambda: serialize_bookings(
            Booking.query.options(
                joinedload(Booking.room),
                joinedload(Booking.user),
            ).all()
        )
    )

    return {
        "without_optimization": regular,
        "with_joinedload": optimized,
    }


def serialize_bookings(bookings):
    return [
        {
            "title": booking.title,
            "room": booking.room.name,
            "user": booking.user.name,
        }
        for booking in bookings
    ]


def measure_queries(callback):
    counter = {"count": 0}

    def count_query(*args):
        counter["count"] += 1

    event.listen(db.engine, "before_cursor_execute", count_query)
    start_time = perf_counter()
    try:
        rows = callback()
    finally:
        duration = perf_counter() - start_time
        event.remove(db.engine, "before_cursor_execute", count_query)

    return {
        "query_count": counter["count"],
        "duration_ms": round(duration * 1000, 2),
        "items": rows,
    }
