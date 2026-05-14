from time import perf_counter

from flask import Blueprint, jsonify
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import joinedload

from app.models import Booking


debug_bp = Blueprint('debug', __name__, url_prefix='/debug')

_query_counter = {'count': 0}


@event.listens_for(Engine, 'before_cursor_execute')
def count_queries(conn, cursor, statement, parameters, context, executemany):
    _query_counter['count'] += 1


def measure_strategy(query_factory):
    _query_counter['count'] = 0
    started_at = perf_counter()

    bookings = query_factory()
    payload = [
        {
            'title': booking.title,
            'room_name': booking.room.name,
            'user_name': booking.user.name,
        }
        for booking in bookings
    ]

    elapsed_ms = round((perf_counter() - started_at) * 1000, 3)
    return {
        'queries': _query_counter['count'],
        'duration_ms': elapsed_ms,
        'rows': len(payload),
        'sample': payload[:10],
    }


@debug_bp.route('/n-plus-1')
def debug_n_plus_one():
    naive = measure_strategy(
        lambda: Booking.query.order_by(Booking.start_time.desc()).all()
    )

    optimized = measure_strategy(
        lambda: Booking.query.options(
            joinedload(Booking.room),
            joinedload(Booking.user),
        ).order_by(Booking.start_time.desc()).all()
    )

    return jsonify({
        'endpoint': '/debug/n-plus-1',
        'naive': naive,
        'optimized': optimized,
        'comparison': {
            'queries_saved': naive['queries'] - optimized['queries'],
            'duration_ms_saved': round(
                naive['duration_ms'] - optimized['duration_ms'],
                3,
            ),
        },
    })