from calendar import monthrange
from datetime import datetime, timedelta
from io import BytesIO

from flask import Blueprint, request, send_file
from PIL import Image as PILImage, ImageDraw
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from sqlalchemy import func
from sqlalchemy.orm import joinedload

from extensions import db
from models import Booking, Room, User
from seeds import ensure_sample_data


reports_bp = Blueprint("reports", __name__)


@reports_bp.get("/api/reports/monthly")
def monthly_report():
    ensure_sample_data()

    month_value = request.args.get("month")
    try:
        month_start = datetime.strptime(month_value, "%Y-%m")
    except (TypeError, ValueError):
        return {"error": "Podaj month w formacie YYYY-MM"}, 400

    last_day = monthrange(month_start.year, month_start.month)[1]
    month_end = month_start.replace(day=last_day) + timedelta(days=1)

    bookings = (
        Booking.query.options(joinedload(Booking.room), joinedload(Booking.user))
        .filter(
            Booking.start_time >= month_start,
            Booking.start_time < month_end,
        )
        .all()
    )

    total_hours = sum(
        (booking.end_time - booking.start_time).total_seconds() / 3600
        for booking in bookings
    )
    revenue = total_hours * 100

    top_rooms = top_room_rows(month_start, month_end)
    top_users = top_user_rows(month_start, month_end)
    pdf = build_monthly_pdf(
        month_value,
        len(bookings),
        total_hours,
        revenue,
        top_rooms,
        top_users,
    )

    return send_file(
        pdf,
        mimetype="application/pdf",
        as_attachment=True,
        download_name=f"monthly-report-{month_value}.pdf",
    )


def top_room_rows(month_start, month_end):
    return (
        db.session.query(Room.name, func.count(Booking.id))
        .join(Booking, Booking.room_id == Room.id)
        .filter(
            Booking.start_time >= month_start,
            Booking.start_time < month_end,
        )
        .group_by(Room.name)
        .order_by(func.count(Booking.id).desc())
        .limit(10)
        .all()
    )


def top_user_rows(month_start, month_end):
    return (
        db.session.query(User.name, func.count(Booking.id))
        .join(Booking, Booking.user_id == User.id)
        .filter(
            Booking.start_time >= month_start,
            Booking.start_time < month_end,
        )
        .group_by(User.name)
        .order_by(func.count(Booking.id).desc())
        .limit(10)
        .all()
    )


def build_monthly_pdf(month, booking_count, total_hours, revenue, top_rooms, top_users):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = [
        Paragraph(f"Raport miesieczny: {month}", styles["Title"]),
        Spacer(1, 16),
        Paragraph("Podsumowanie", styles["Heading2"]),
        build_table(
            [
                ["Liczba rezerwacji", booking_count],
                ["Laczny czas", f"{total_hours:.1f} h"],
                ["Przychod", f"{revenue:.2f} PLN"],
            ]
        ),
        Spacer(1, 16),
        Paragraph("Top 10 sal", styles["Heading2"]),
        build_table([["Sala", "Rezerwacje"], *top_rooms]),
        Spacer(1, 16),
        Paragraph("Top 10 uzytkownikow", styles["Heading2"]),
        build_table([["Uzytkownik", "Rezerwacje"], *top_users]),
        Spacer(1, 16),
        Paragraph("Wykres wykorzystania sal", styles["Heading2"]),
        build_usage_chart(top_rooms),
    ]

    doc.build(story)
    buffer.seek(0)
    return buffer


def build_table(rows):
    if len(rows) == 1:
        rows.append(["Brak danych", 0])

    table = Table(rows, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dbeafe")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("PADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table


def build_usage_chart(top_rooms):
    names = [row[0] for row in top_rooms] or ["Brak danych"]
    counts = [row[1] for row in top_rooms] or [0]

    width = 840
    height = 360
    image = PILImage.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    left = 70
    right = 30
    top = 35
    bottom = 90
    chart_width = width - left - right
    chart_height = height - top - bottom
    max_count = max(counts) or 1
    bar_gap = 14
    bar_width = max(20, (chart_width - bar_gap * (len(counts) - 1)) // len(counts))

    draw.line((left, top, left, top + chart_height), fill="#6b7280", width=2)
    draw.line(
        (left, top + chart_height, width - right, top + chart_height),
        fill="#6b7280",
        width=2,
    )

    for index, count in enumerate(counts):
        x = left + index * (bar_width + bar_gap)
        bar_height = int((count / max_count) * chart_height)
        y = top + chart_height - bar_height
        draw.rectangle((x, y, x + bar_width, top + chart_height), fill="#2563eb")
        draw.text((x, y - 18), str(count), fill="#111827")
        draw.text((x, top + chart_height + 8), names[index][:12], fill="#111827")

    image_buffer = BytesIO()
    image.save(image_buffer, format="PNG")
    image_buffer.seek(0)
    return Image(image_buffer, width=420, height=180)
