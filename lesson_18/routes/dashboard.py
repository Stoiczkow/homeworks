from datetime import datetime, timedelta

from flask import Blueprint, render_template
from sqlalchemy import func

from extensions import db
from models import Booking, User
from seeds import ensure_sample_data


dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.get("/dashboard")
def dashboard():
    ensure_sample_data()

    department_rows = (
        db.session.query(User.department, func.count(Booking.id))
        .join(Booking, Booking.user_id == User.id)
        .group_by(User.department)
        .order_by(User.department)
        .all()
    )

    heatmap_rows = (
        db.session.query(
            func.extract("dow", Booking.start_time),
            func.extract("hour", Booking.start_time),
            func.count(Booking.id),
        )
        .group_by(
            func.extract("dow", Booking.start_time),
            func.extract("hour", Booking.start_time),
        )
        .all()
    )

    thirty_days_ago = datetime.utcnow().date() - timedelta(days=29)
    trend_rows = (
        db.session.query(
            func.date(Booking.start_time),
            func.count(Booking.id),
        )
        .filter(func.date(Booking.start_time) >= thirty_days_ago)
        .group_by(func.date(Booking.start_time))
        .order_by(func.date(Booking.start_time))
        .all()
    )

    return render_template(
        "dashboard.html",
        department_labels=[row[0] for row in department_rows],
        department_counts=[row[1] for row in department_rows],
        heatmap=build_heatmap(heatmap_rows),
        hours=list(range(8, 19)),
        day_names=["Nd", "Pn", "Wt", "Sr", "Cz", "Pt", "So"],
        trend_labels=[str(row[0]) for row in trend_rows],
        trend_counts=[row[1] for row in trend_rows],
    )


def build_heatmap(rows):
    heatmap = {
        day: {hour: 0 for hour in range(8, 19)}
        for day in range(7)
    }

    for day, hour, count in rows:
        day = int(day)
        hour = int(hour)
        if hour in heatmap[day]:
            heatmap[day][hour] = count

    return heatmap
