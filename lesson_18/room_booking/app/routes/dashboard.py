from flask import Blueprint, render_template, jsonify, request, send_file
from datetime import datetime, timedelta
from sqlalchemy import func, desc
from sqlalchemy.orm import joinedload
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from app.models import db, Room, Booking, User, get_booking_statistics

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/dashboard')
def dashboard():
    stats = {
        'total_rooms': Room.query.filter_by(is_active=True).count(),
        'total_users': User.query.count(),
        'total_bookings': Booking.query.filter_by(status='confirmed').count(),
        'bookings_today': Booking.query.filter(
            func.date(Booking.start_time) == datetime.today().date(),
            Booking.status == 'confirmed'
        ).count()
    }

    now = datetime.now()
    upcoming = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).filter(
        Booking.start_time >= now,
        Booking.start_time <= now + timedelta(hours=24),
        Booking.status == 'confirmed'
    ).order_by(Booking.start_time).limit(10).all()

    top_users = db.session.query(
        User.name,
        func.count(Booking.id).label('booking_count')
    ).join(Booking).filter(
        Booking.status != 'cancelled'
    ).group_by(User.id).order_by(desc('booking_count')).limit(5).all()

    month_ago = now - timedelta(days=30)
    room_utilization = []
    active_rooms = Room.query.filter_by(is_active=True).all()

    for room in active_rooms:
        total_hours = db.session.query(
            func.sum(
                func.extract('epoch', Booking.end_time - Booking.start_time) / 3600
            )
        ).filter(
            Booking.room_id == room.id,
            Booking.start_time >= month_ago,
            Booking.status != 'cancelled'
        ).scalar() or 0

        max_hours = 176
        utilization = (total_hours / max_hours) * 100

        room_utilization.append({
            'room': room.name,
            'hours': round(total_hours, 1),
            'utilization': round(utilization, 1)
        })

    room_utilization.sort(key=lambda x: x['utilization'], reverse=True)

    return render_template(
        'dashboard.html',
        stats=stats,
        upcoming=upcoming,
        top_users=top_users,
        room_utilization=room_utilization
    )


@dashboard_bp.route('/api/dashboard/stats')
def api_stats():
    stats = get_booking_statistics()
    return jsonify(stats)


@dashboard_bp.route('/api/dashboard/extended-stats')
def extended_stats():
    now = datetime.now()
    month_ago = now - timedelta(days=30)

    department_stats = db.session.query(
        User.department,
        func.count(Booking.id).label("count")
    ).join(Booking).filter(
        Booking.status != "cancelled"
    ).group_by(User.department).all()

    heatmap_raw = db.session.query(
        func.extract('dow', Booking.start_time).label('weekday'),
        func.extract('hour', Booking.start_time).label('hour'),
        func.count(Booking.id).label('count')
    ).filter(
        Booking.status != "cancelled"
    ).group_by('weekday', 'hour').order_by('weekday', 'hour').all()

    weekdays = ['Nd', 'Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'Sb']
    heatmap = [
        {
            "day": weekdays[int(row.weekday)],
            "hour": int(row.hour),
            "count": row.count
        }
        for row in heatmap_raw
    ]

    trend_raw = db.session.query(
        func.date(Booking.start_time).label("day"),
        func.count(Booking.id).label("count")
    ).filter(
        Booking.start_time >= month_ago,
        Booking.status != "cancelled"
    ).group_by(func.date(Booking.start_time)).order_by(func.date(Booking.start_time)).all()

    trend = [
        {
            "day": str(row.day),
            "count": row.count
        }
        for row in trend_raw
    ]

    return jsonify({
        "department_distribution": [
            {"department": row.department or "Brak", "count": row.count}
            for row in department_stats
        ],
        "heatmap": heatmap,
        "trend_last_30_days": trend
    })


@dashboard_bp.route('/api/reports/monthly', methods=['GET'])
def monthly_report():
    month = request.args.get("month")

    if not month:
        return jsonify({"error": "Podaj parametr month=YYYY-MM"}), 400

    try:
        year, month_num = map(int, month.split("-"))
    except ValueError:
        return jsonify({"error": "Format miesiąca musi być YYYY-MM"}), 400

    start_date = datetime(year, month_num, 1)
    if month_num == 12:
        end_date = datetime(year + 1, 1, 1)
    else:
        end_date = datetime(year, month_num + 1, 1)

    bookings = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).filter(
        Booking.start_time >= start_date,
        Booking.start_time < end_date,
        Booking.status != 'cancelled'
    ).all()

    total_bookings = len(bookings)
    total_hours = sum(booking.duration_hours for booking in bookings)
    total_revenue = sum(booking.total_cost for booking in bookings)

    top_rooms = db.session.query(
        Room.name,
        func.count(Booking.id).label("booking_count")
    ).join(Booking).filter(
        Booking.start_time >= start_date,
        Booking.start_time < end_date,
        Booking.status != 'cancelled'
    ).group_by(Room.name).order_by(desc("booking_count")).limit(10).all()

    top_users = db.session.query(
        User.name,
        func.count(Booking.id).label("booking_count")
    ).join(Booking).filter(
        Booking.start_time >= start_date,
        Booking.start_time < end_date,
        Booking.status != 'cancelled'
    ).group_by(User.name).order_by(desc("booking_count")).limit(10).all()

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 50

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, f"Raport miesięczny rezerwacji - {month}")
    y -= 40

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, y, "Podsumowanie")
    y -= 25

    pdf.setFont("Helvetica", 11)
    pdf.drawString(60, y, f"Liczba rezerwacji: {total_bookings}")
    y -= 18
    pdf.drawString(60, y, f"Łączny czas: {round(total_hours, 2)} h")
    y -= 18
    pdf.drawString(60, y, f"Przychód: {round(total_revenue, 2)} PLN")
    y -= 35

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, y, "Top 10 sal")
    y -= 25

    pdf.setFont("Helvetica", 11)
    if top_rooms:
        for index, room in enumerate(top_rooms, start=1):
            pdf.drawString(
                60,
                y,
                f"{index}. {room.name} - {room.booking_count} rezerwacji"
            )
            y -= 18

            if y < 80:
                pdf.showPage()
                y = height - 50
                pdf.setFont("Helvetica", 11)
    else:
        pdf.drawString(60, y, "Brak danych")
        y -= 18

    y -= 20

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, y, "Top 10 użytkowników")
    y -= 25

    pdf.setFont("Helvetica", 11)
    if top_users:
        for index, user in enumerate(top_users, start=1):
            pdf.drawString(
                60,
                y,
                f"{index}. {user.name} - {user.booking_count} rezerwacji"
            )
            y -= 18

            if y < 80:
                pdf.showPage()
                y = height - 50
                pdf.setFont("Helvetica", 11)
    else:
        pdf.drawString(60, y, "Brak danych")
        y -= 18

    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"raport_{month}.pdf",
        mimetype="application/pdf"
    )