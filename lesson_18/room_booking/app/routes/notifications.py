from flask import Blueprint, jsonify, request

from app.models import Notification, create_due_reminder_notifications, db


notifications_bp = Blueprint(
	'notifications',
	__name__,
	url_prefix='/api/notifications',
)


@notifications_bp.route('', methods=['GET'])
@notifications_bp.route('/', methods=['GET'])
def get_notifications():
	create_due_reminder_notifications()

	query = Notification.query.filter_by(is_read=False).order_by(
		Notification.created_at.desc()
	)

	if user_id := request.args.get('user_id', type=int):
		query = query.filter(Notification.user_id == user_id)

	notifications = query.all()
	return jsonify({
		'notifications': [notification.to_dict() for notification in notifications],
		'total': len(notifications),
	})


@notifications_bp.route('/<int:notification_id>/read', methods=['POST'])
def mark_notification_read(notification_id):
	notification = Notification.query.get_or_404(notification_id)
	notification.is_read = True
	db.session.commit()

	return jsonify({
		'message': 'Powiadomienie oznaczone jako przeczytane',
		'notification': notification.to_dict(),
	})