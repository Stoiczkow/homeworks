from datetime import datetime

from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload

from app.models import db, Booking, Room, User, find_available_rooms

bookings_bp = Blueprint('bookings', __name__, url_prefix='/api/bookings')


@bookings_bp.route('/', methods=['GET'])
def get_bookings():
    query = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    )

    if room_id := request.args.get('room_id'):
        query = query.filter(Booking.room_id == room_id)
    if user_id := request.args.get('user_id'):
        query = query.filter(Booking.user_id == user_id)
    if date_str := request.args.get('date'):
        date = datetime.strptime(date_str, '%Y-%m-%d')
        query = query.filter(db.func.date(Booking.start_time) == date.date())
    if status := request.args.get('status'):
        query = query.filter(Booking.status == status)

    query = query.order_by(Booking.start_time.desc())

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    pagination = query.paginate(page=page, per_page=per_page)

    return jsonify({
        'bookings': [b.to_dict(include_room=True, include_user=True) for b in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    })


@bookings_bp.route('/', methods=['POST'])
def create_booking():
    data = request.get_json()

    required = ['room_id', 'user_id', 'title', 'start_time', 'end_time']
    for field in required:
        if field not in data:
            return jsonify({'error': f'Brak wymaganego pola: {field}'}), 400

    try:
        start_time = datetime.fromisoformat(data['start_time'])
        end_time = datetime.fromisoformat(data['end_time'])
    except ValueError:
        return jsonify({'error': 'Niepoprawny format daty. Uzyj ISO format.'}), 400

    if start_time >= end_time:
        return jsonify({'error': 'Czas rozpoczecia musi byc przed czasem zakonczenia'}), 400
    if start_time < datetime.now():
        return jsonify({'error': 'Nie mozna rezerwowac w przeszlosci'}), 400

    room = Room.query.get(data['room_id'])
    if not room:
        return jsonify({'error': 'Sala nie istnieje'}), 404
    if not room.is_active:
        return jsonify({'error': 'Sala jest nieaktywna'}), 400

    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({'error': 'Uzytkownik nie istnieje'}), 404

    if not room.is_available(start_time, end_time):
        return jsonify({'error': 'Sala jest juz zarezerwowana w tym czasie'}), 409

    attendees = data.get('attendees_count', 1)
    if attendees > room.capacity:
        return jsonify({'error': f'Zbyt wielu uczestnikow. Pojemnosc sali: {room.capacity}'}), 400

    try:
        booking = Booking(
            room_id=room.id,
            user_id=user.id,
            title=data['title'],
            description=data.get('description'),
            start_time=start_time,
            end_time=end_time,
            attendees_count=attendees
        )
        db.session.add(booking)
        db.session.commit()
        return jsonify({'message': 'Rezerwacja utworzona', 'booking': booking.to_dict(include_room=True)}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Blad tworzenia rezerwacji: {str(e)}'}), 500


@bookings_bp.route('/<int:booking_id>', methods=['DELETE'])
def cancel_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)

    if booking.status == 'cancelled':
        return jsonify({'error': 'Rezerwacja juz anulowana'}), 400
    if booking.start_time < datetime.now():
        return jsonify({'error': 'Nie mozna anulowac przeszlej rezerwacji'}), 400

    try:
        booking.status = 'cancelled'
        db.session.commit()
        return jsonify({'message': 'Rezerwacja anulowana'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bookings_bp.route('/available-rooms', methods=['GET'])
def find_available():
    try:
        start_time = datetime.fromisoformat(request.args['start_time'])
        end_time = datetime.fromisoformat(request.args['end_time'])
    except (KeyError, ValueError):
        return jsonify({'error': 'Wymagane: start_time i end_time w formacie ISO'}), 400

    capacity = request.args.get('capacity', 1, type=int)
    equipment = None
    if eq_param := request.args.get('equipment'):
        equipment = [e.strip() for e in eq_param.split(',')]

    rooms = find_available_rooms(start_time, end_time, capacity, equipment)

    return jsonify({
        'available_rooms': [r.to_dict() for r in rooms],
        'search_criteria': {
            'start_time': start_time.isoformat(),
            'end_time': end_time.isoformat(),
            'min_capacity': capacity,
            'required_equipment': equipment
        }
    })
