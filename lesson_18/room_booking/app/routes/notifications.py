from flask import Blueprint, jsonify
from app.models import db, Notification

notifications_bp = Blueprint("notifications", __name__, url_prefix="/api/notifications")


@notifications_bp.route("/", methods=["GET"])
def get_notifications():
    notifications = Notification.query.filter_by(is_read=False).order_by(
        Notification.created_at.desc()
    ).all()

    return jsonify({
        "notifications": [n.to_dict() for n in notifications]
    })


@notifications_bp.route("/<int:notification_id>/read", methods=["POST"])
def mark_as_read(notification_id):
    notification = Notification.query.get_or_404(notification_id)
    notification.is_read = True
    db.session.commit()

    return jsonify({"message": "Powiadomienie oznaczone jako przeczytane"})