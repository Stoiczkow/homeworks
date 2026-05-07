from datetime import datetime

from sqlalchemy import event, select

from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    department = db.Column(db.String(80), nullable=False)

    bookings = db.relationship("Booking", back_populates="user")


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    bookings = db.relationship("Booking", back_populates="room")


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=False)
    recurrence_rule = db.Column(db.String(20))
    series_id = db.Column(db.String(36))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)

    user = db.relationship("User", back_populates="bookings")
    room = db.relationship("Room", back_populates="bookings")


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    is_read = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = db.relationship("User")


@event.listens_for(Booking, "after_insert")
def create_admin_notification(mapper, connection, booking):
    admin_id = connection.execute(
        select(User.id).where(User.department == "Admin").limit(1)
    ).scalar()

    if not admin_id:
        return

    connection.execute(
        Notification.__table__.insert().values(
            user_id=admin_id,
            message=f"Nowa rezerwacja: {booking.title}",
            is_read=False,
            created_at=datetime.utcnow(),
        )
    )
