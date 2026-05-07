from datetime import datetime, timedelta

from sqlalchemy import text

from extensions import db
from models import Booking, Room, User


def ensure_sample_data():
    db.create_all()
    ensure_booking_columns()

    admin = User.query.filter_by(department="Admin").first()
    if not admin:
        admin = User(name="Admin", department="Admin")
        db.session.add(admin)
        db.session.commit()

    if Booking.query.first():
        return

    users = [
        User(name="Anna Kowalska", department="HR"),
        User(name="Piotr Nowak", department="IT"),
        User(name="Maria Zielinska", department="Marketing"),
    ]
    rooms = [
        Room(name="Sala A"),
        Room(name="Sala B"),
        Room(name="Sala C"),
    ]

    db.session.add_all(users + rooms)
    db.session.flush()

    now = datetime.utcnow().replace(minute=0, second=0, microsecond=0)
    bookings = []
    for index in range(6):
        start_time = now + timedelta(days=index, hours=index % 3)
        bookings.append(
            Booking(
                title=f"Spotkanie {index + 1}",
                start_time=start_time,
                end_time=start_time + timedelta(hours=1),
                user=users[index % len(users)],
                room=rooms[index % len(rooms)],
            )
        )

    db.session.add_all(bookings)
    db.session.commit()


def ensure_booking_columns():
    db.session.execute(
        text("ALTER TABLE booking ADD COLUMN IF NOT EXISTS recurrence_rule VARCHAR(20)")
    )
    db.session.execute(
        text("ALTER TABLE booking ADD COLUMN IF NOT EXISTS series_id VARCHAR(36)")
    )
    db.session.commit()
