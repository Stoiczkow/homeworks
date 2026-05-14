"""
Modele bazy danych dla systemu rezerwacji sal.
"""
from datetime import datetime, timedelta
from typing import Any

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event, insert, select


db = SQLAlchemy()


# TABELA ŁĄCZĄCA: Sale i Wyposażenie (M:N)
room_equipment = db.Table(
	'room_equipment',
	db.Column('room_id', db.Integer, db.ForeignKey('rooms.id'),
			  primary_key=True),
	db.Column('equipment_id', db.Integer, db.ForeignKey('equipment.id'),
			  primary_key=True)
)


class User(db.Model):
	"""Model użytkownika systemu."""
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	name = db.Column(db.String(100), nullable=False)
	department = db.Column(db.String(50))
	is_admin = db.Column(db.Boolean, default=False)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)

	# Relacja 1:N z rezerwacjami
	bookings: Any = db.relationship('Booking', backref='user', lazy='dynamic')

	def __repr__(self):
		return f'<User {self.email}>'

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email,
			'name': self.name,
			'department': self.department,
			'is_admin': self.is_admin
		}


class Equipment(db.Model):
	"""Model wyposażenia sali (projektor, tablica, wideokonferencja itp.)."""
	__tablename__ = 'equipment'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True, nullable=False)
	icon = db.Column(db.String(50))  # np. "projector", "whiteboard"

	def __repr__(self):
		return f'<Equipment {self.name}>'


class Room(db.Model):
	"""Model sali konferencyjnej."""
	__tablename__ = 'rooms'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	capacity = db.Column(db.Integer, nullable=False)
	floor = db.Column(db.Integer, default=0)
	description = db.Column(db.Text)
	is_active = db.Column(db.Boolean, default=True)
	hourly_rate = db.Column(db.Numeric(10, 2), default=0)  # Koszt za godzinę

	# Relacja 1:N z rezerwacjami
	bookings: Any = db.relationship('Booking', backref='room', lazy='dynamic',
								   cascade='all, delete-orphan')

	# Relacja M:N z wyposażeniem
	equipment: Any = db.relationship(
		'Equipment',
		secondary=room_equipment,
		lazy='subquery',
		backref=db.backref('rooms', lazy=True)
	)

	def __repr__(self):
		return f'<Room {self.name} (cap: {self.capacity})>'

	def to_dict(self, include_equipment=True):
		data = {
			'id': self.id,
			'name': self.name,
			'capacity': self.capacity,
			'floor': self.floor,
			'description': self.description,
			'is_active': self.is_active,
			'hourly_rate': float(self.hourly_rate) if self.hourly_rate else 0
		}
		if include_equipment:
			data['equipment'] = [e.name for e in self.equipment]
		return data

	def is_available(self, start_time, end_time, exclude_booking_id=None):
		"""
		Sprawdza, czy sala jest dostępna w podanym przedziale czasowym.

		Args:
			start_time: Początek rezerwacji (datetime)
			end_time: Koniec rezerwacji (datetime)
			exclude_booking_id: ID rezerwacji do pominięcia (przy edycji)

		Returns:
			bool: True jeśli sala jest dostępna
		"""
		query = Booking.query.filter(
			Booking.room_id == self.id,
			Booking.status != 'cancelled',
			# Sprawdzenie nakładania się przedziałów czasowych
			Booking.start_time < end_time,
			Booking.end_time > start_time
		)

		if exclude_booking_id:
			query = query.filter(Booking.id != exclude_booking_id)

		return query.count() == 0


class Booking(db.Model):
	"""Model rezerwacji sali."""
	__tablename__ = 'bookings'

	room: Any
	user: Any

	id = db.Column(db.Integer, primary_key=True)
	room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'),
						nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
						nullable=False)

	title = db.Column(db.String(200), nullable=False)
	description = db.Column(db.Text)

	start_time = db.Column(db.DateTime, nullable=False)
	end_time = db.Column(db.DateTime, nullable=False)

	status = db.Column(
		db.String(20),
		default='confirmed',
		nullable=False
	)  # confirmed, cancelled, completed
	recurrence_rule = db.Column(db.String(20))
	series_id = db.Column(db.String(36), index=True)

	attendees_count = db.Column(db.Integer, default=1)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow,
						   onupdate=datetime.utcnow)

	# Indeks dla szybkiego wyszukiwania
	__table_args__ = (
		db.Index('idx_booking_room_time', 'room_id', 'start_time', 'end_time'),
	)

	def __repr__(self):
		return f'<Booking {self.title} ({self.start_time})>'

	@property
	def duration_hours(self):
		"""Czas trwania rezerwacji w godzinach."""
		delta = self.end_time - self.start_time
		return delta.total_seconds() / 3600

	@property
	def total_cost(self):
		"""Całkowity koszt rezerwacji."""
		if self.room and self.room.hourly_rate:
			return float(self.room.hourly_rate) * self.duration_hours
		return 0

	def to_dict(self, include_room=False, include_user=False):
		data = {
			'id': self.id,
			'title': self.title,
			'description': self.description,
			'start_time': self.start_time.isoformat(),
			'end_time': self.end_time.isoformat(),
			'status': self.status,
			'recurrence_rule': self.recurrence_rule,
			'series_id': self.series_id,
			'attendees_count': self.attendees_count,
			'duration_hours': round(self.duration_hours, 2),
			'total_cost': round(self.total_cost, 2)
		}
		if include_room:
			data['room'] = self.room.to_dict(include_equipment=False)
		if include_user:
			data['user'] = self.user.to_dict()
		return data


class Notification(db.Model):
	"""Model powiadomienia użytkownika."""
	__tablename__ = 'notifications'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	message = db.Column(db.Text, nullable=False)
	is_read = db.Column(db.Boolean, default=False, nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

	user: Any = db.relationship(
		'User',
		backref=db.backref('notifications', lazy='dynamic', cascade='all, delete-orphan')
	)

	def to_dict(self):
		return {
			'id': self.id,
			'user_id': self.user_id,
			'message': self.message,
			'is_read': self.is_read,
			'created_at': self.created_at.isoformat()
		}


@event.listens_for(Booking, 'after_insert')
def create_admin_booking_notifications(mapper, connection, target):
	admin_ids = connection.execute(
		select(User.id).where(User.is_admin.is_(True))
	).scalars().all()

	if not admin_ids:
		return

	room_name = connection.execute(
		select(Room.name).where(Room.id == target.room_id)
	).scalar_one_or_none() or f'Sala #{target.room_id}'

	message = (
		f'Nowa rezerwacja: "{target.title}" dla sali {room_name} '
		f'od {target.start_time.strftime("%Y-%m-%d %H:%M")}. '
		f'Użytkownik ID: {target.user_id}.'
	)

	connection.execute(
		insert(Notification),
		[
			{
				'user_id': admin_id,
				'message': message,
				'is_read': False,
				'created_at': datetime.utcnow(),
			}
			for admin_id in admin_ids
		]
	)


def create_due_reminder_notifications(reference_time=None):
	"""Tworzy przypomnienia dla rezerwacji rozpoczynających się w ciągu godziny."""
	from sqlalchemy.orm import joinedload

	reference_time = reference_time or datetime.now()
	deadline = reference_time + timedelta(hours=1)

	due_bookings = Booking.query.options(joinedload(Booking.room)).filter(
		Booking.status == 'confirmed',
		Booking.start_time >= reference_time,
		Booking.start_time <= deadline,
	).all()

	created_notifications = 0
	for booking in due_bookings:
		room_name = booking.room.name if booking.room else f'Sala #{booking.room_id}'
		message = (
			f'Przypomnienie: rezerwacja "{booking.title}" w sali {room_name} '
			f'zaczyna się o {booking.start_time.strftime("%Y-%m-%d %H:%M")}. '
		)

		exists = Notification.query.filter_by(
			user_id=booking.user_id,
			message=message,
		).first()
		if exists:
			continue

		notification = Notification()
		notification.user_id = booking.user_id
		notification.message = message
		db.session.add(notification)
		created_notifications += 1

	if created_notifications:
		db.session.commit()

	return created_notifications


# === FUNKCJE POMOCNICZE ===

def find_available_rooms(start_time, end_time, min_capacity=1,
						 required_equipment=None):
	"""
	Znajdź dostępne sale spełniające kryteria.

	Args:
		start_time: Początek (datetime)
		end_time: Koniec (datetime)
		min_capacity: Minimalna pojemność
		required_equipment: Lista nazw wymaganego wyposażenia

	Returns:
		Lista dostępnych sal
	"""
	from sqlalchemy.orm import joinedload

	# Podstawowe zapytanie z eager loading
	query = Room.query.options(
		joinedload(Room.equipment)
	).filter(
		Room.is_active == True,
		Room.capacity >= min_capacity
	)

	# Filtruj po wyposażeniu
	if required_equipment:
		for eq_name in required_equipment:
			query = query.filter(
				Room.equipment.any(Equipment.name == eq_name)
			)

	# Pobierz kandydatów
	candidate_rooms = query.all()

	# Sprawdź dostępność każdej sali
	available = []
	for room in candidate_rooms:
		if room.is_available(start_time, end_time):
			available.append(room)

	return available


def get_booking_statistics(start_date=None, end_date=None):
	"""
	Pobierz statystyki rezerwacji.

	Returns:
		dict: Słownik ze statystykami
	"""
	from collections import defaultdict
	from datetime import datetime, time, timedelta
	from sqlalchemy.orm import joinedload

	base_query = db.session.query(Booking).filter(
		Booking.status != 'cancelled'
	)

	if start_date:
		base_query = base_query.filter(Booking.start_time >= start_date)
	if end_date:
		base_query = base_query.filter(Booking.end_time <= end_date)

	bookings = base_query.options(
		joinedload(Booking.room),
		joinedload(Booking.user)
	).all()

	weekdays = ['Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'Sb', 'Nd']
	room_aggregate = defaultdict(lambda: {'bookings': 0, 'hours': 0.0})
	weekday_aggregate = defaultdict(int)
	department_aggregate = defaultdict(int)

	trend_end = datetime.now().date()
	trend_start = trend_end - timedelta(days=29)
	trend_aggregate = {
		(trend_start + timedelta(days=offset)).isoformat(): 0
		for offset in range(30)
	}

	heatmap_days = weekdays
	heatmap_hours = list(range(24))
	heatmap_matrix = [
		[0 for _ in heatmap_hours]
		for _ in heatmap_days
	]

	for booking in bookings:
		duration_hours = booking.duration_hours
		room_name = booking.room.name if booking.room else 'Brak sali'
		room_aggregate[room_name]['bookings'] += 1
		room_aggregate[room_name]['hours'] += duration_hours

		weekday_index = booking.start_time.weekday()
		weekday_aggregate[weekdays[weekday_index]] += 1

		department_name = None
		if booking.user and booking.user.department:
			department_name = booking.user.department
		department_aggregate[department_name or 'Brak działu'] += 1

		booking_day = booking.start_time.date().isoformat()
		if booking_day in trend_aggregate:
			trend_aggregate[booking_day] += 1

		# Wypełnij heatmapę dla każdej godziny zajętej przez rezerwację.
		current_slot = booking.start_time.replace(minute=0, second=0, microsecond=0)
		end_slot = booking.end_time
		while current_slot < end_slot:
			heatmap_matrix[current_slot.weekday()][current_slot.hour] += 1
			current_slot += timedelta(hours=1)

	return {
		'total_bookings': len(bookings),
		'room_stats': [
			{
				'room': room,
				'bookings': values['bookings'],
				'hours': round(values['hours'], 1)
			}
			for room, values in sorted(
				room_aggregate.items(),
				key=lambda item: item[1]['bookings'],
				reverse=True
			)
		],
		'weekday_stats': [
			{
				'day': day,
				'count': weekday_aggregate[day]
			}
			for day in weekdays
		],
		'department_stats': [
			{
				'department': department,
				'count': count
			}
			for department, count in sorted(
				department_aggregate.items(),
				key=lambda item: item[1],
				reverse=True
			)
		],
		'daily_trend': [
			{
				'date': date_key,
				'count': count
			}
			for date_key, count in trend_aggregate.items()
		],
		'heatmap': {
			'days': heatmap_days,
			'hours': heatmap_hours,
			'values': heatmap_matrix,
		}
	}
