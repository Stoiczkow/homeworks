from datetime import datetime
from uuid import uuid4

from dateutil.relativedelta import relativedelta
from dateutil.rrule import WEEKLY, rrule
from flask import Blueprint, request

from extensions import db
from models import Booking, Room, User
from seeds import ensure_sample_data


bookings_bp = Blueprint("bookings", __name__)


@bookings_bp.post("/api/bookings/recurring")
def create_recurring_bookings():
    ensure_sample_data()

    data = request.get_json() or {}
    title = data.get("title")
    user_id = data.get("user_id")
    room_id = data.get("room_id")
    recurrence_rule = data.get("recurrence_rule", "WEEKLY")
    months = int(data.get("months", 3))

    if not title or not user_id or not room_id:
        return {"error": "Wymagane pola: title, user_id, room_id"}, 400

    try:
        start_time = datetime.fromisoformat(data["start_time"])
        end_time = datetime.fromisoformat(data["end_time"])
    except (KeyError, ValueError):
        return {"error": "Podaj start_time i end_time w formacie ISO"}, 400

    if end_time <= start_time:
        return {"error": "end_time musi być później niż start_time"}, 400

    interval = {"WEEKLY": 1, "BIWEEKLY": 2}.get(recurrence_rule)
    if not interval:
        return {"error": "recurrence_rule musi być WEEKLY albo BIWEEKLY"}, 400

    if not User.query.get(user_id) or not Room.query.get(room_id):
        return {"error": "Nie znaleziono użytkownika albo sali"}, 404

    duration = end_time - start_time
    starts = list(
        rrule(
            WEEKLY,
            interval=interval,
            dtstart=start_time,
            until=start_time + relativedelta(months=months),
        )
    )

    conflicts = find_conflicts(room_id, starts, duration)
    if conflicts:
        return {"error": "Konflikt rezerwacji", "conflicts": conflicts}, 409

    series_id = str(uuid4())
    bookings = [
        Booking(
            title=title,
            start_time=start,
            end_time=start + duration,
            recurrence_rule=recurrence_rule,
            series_id=series_id,
            user_id=user_id,
            room_id=room_id,
        )
        for start in starts
    ]

    db.session.add_all(bookings)
    db.session.commit()

    return {
        "series_id": series_id,
        "bookings": [serialize_booking(booking) for booking in bookings],
    }, 201


@bookings_bp.delete("/api/bookings/<int:booking_id>")
def cancel_booking(booking_id):
    ensure_sample_data()

    booking = Booking.query.get_or_404(booking_id)
    db.session.delete(booking)
    db.session.commit()

    return {"deleted": 1, "booking_id": booking_id}


@bookings_bp.delete("/api/bookings/series/<series_id>")
def cancel_booking_series(series_id):
    ensure_sample_data()

    bookings = Booking.query.filter_by(series_id=series_id).all()
    deleted_count = len(bookings)

    for booking in bookings:
        db.session.delete(booking)

    db.session.commit()

    return {"deleted": deleted_count, "series_id": series_id}


def find_conflicts(room_id, starts, duration):
    conflicts = []

    for start in starts:
        end = start + duration
        booking = (
            Booking.query
            .filter(
                Booking.room_id == room_id,
                Booking.start_time < end,
                Booking.end_time > start,
            )
            .first()
        )

        if booking:
            conflicts.append(
                {
                    "start_time": start.isoformat(),
                    "end_time": end.isoformat(),
                    "booking_id": booking.id,
                    "title": booking.title,
                }
            )

    return conflicts


def serialize_booking(booking):
    return {
        "id": booking.id,
        "title": booking.title,
        "start_time": booking.start_time.isoformat(),
        "end_time": booking.end_time.isoformat(),
        "room_id": booking.room_id,
        "user_id": booking.user_id,
        "recurrence_rule": booking.recurrence_rule,
        "series_id": booking.series_id,
    }
