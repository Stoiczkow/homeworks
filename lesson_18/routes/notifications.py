from datetime import datetime, timedelta

from flask import Blueprint, request

from extensions import db
from models import Booking, Notification
from seeds import ensure_sample_data


notifications_bp = Blueprint("notifications", __name__)


@notifications_bp.get("/api/notifications")
def get_notifications():
    ensure_sample_data()
    create_booking_reminders()

    query = Notification.query.filter_by(is_read=False)
    user_id = request.args.get("user_id", type=int)
    if user_id:
        query = query.filter_by(user_id=user_id)

    notifications = query.order_by(Notification.created_at.desc()).all()
    return [serialize_notification(notification) for notification in notifications]


@notifications_bp.post("/api/notifications/<int:notification_id>/read")
def mark_notification_as_read(notification_id):
    ensure_sample_data()

    notification = Notification.query.get_or_404(notification_id)
    notification.is_read = True
    db.session.commit()

    return serialize_notification(notification)


def create_booking_reminders():
    now = datetime.utcnow()
    reminder_start = now + timedelta(minutes=55)
    reminder_end = now + timedelta(minutes=65)

    bookings = (
        Booking.query
        .filter(Booking.start_time.between(reminder_start, reminder_end))
        .all()
    )

    created = False
    for booking in bookings:
        message = f"Przypomnienie: rezerwacja '{booking.title}' za 1h"
        exists = Notification.query.filter_by(
            user_id=booking.user_id,
            message=message,
        ).first()

        if not exists:
            db.session.add(Notification(user_id=booking.user_id, message=message))
            created = True

    if created:
        db.session.commit()


def serialize_notification(notification):
    return {
        "id": notification.id,
        "user_id": notification.user_id,
        "message": notification.message,
        "is_read": notification.is_read,
        "created_at": notification.created_at.isoformat(),
    }
