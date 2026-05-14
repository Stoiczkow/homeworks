from collections import defaultdict
from datetime import datetime
from io import BytesIO

from flask import Blueprint, jsonify, request, send_file
from PIL import Image as PILImage, ImageDraw
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from sqlalchemy.orm import joinedload

from app.models import Booking


reports_bp = Blueprint('reports', __name__, url_prefix='/api/reports')


@reports_bp.route('/monthly', methods=['GET'])
def monthly_report():
	month = request.args.get('month')
	if not month:
		return jsonify({'error': 'Parametr month jest wymagany w formacie YYYY-MM'}), 400

	try:
		month_start = datetime.strptime(month, '%Y-%m')
	except ValueError:
		return jsonify({'error': 'Niepoprawny format month. Użyj YYYY-MM'}), 400

	if month_start.month == 12:
		next_month = month_start.replace(year=month_start.year + 1, month=1)
	else:
		next_month = month_start.replace(month=month_start.month + 1)

	bookings = Booking.query.options(
		joinedload(Booking.room),
		joinedload(Booking.user),
	).filter(
		Booking.status != 'cancelled',
		Booking.start_time >= month_start,
		Booking.start_time < next_month,
	).order_by(Booking.start_time.asc()).all()

	pdf_buffer = build_monthly_report_pdf(month, bookings)
	pdf_buffer.seek(0)

	return send_file(
		pdf_buffer,
		mimetype='application/pdf',
		as_attachment=True,
		download_name=f'monthly-report-{month}.pdf',
	)


def build_monthly_report_pdf(month, bookings):
	styles = getSampleStyleSheet()
	buffer = BytesIO()
	doc = SimpleDocTemplate(buffer, pagesize=A4, title=f'Raport miesięczny {month}')

	summary = build_summary(bookings)
	room_stats = build_room_stats(bookings)
	user_stats = build_user_stats(bookings)

	story = [
		Paragraph(f'Raport miesięczny rezerwacji: {month}', styles['Title']),
		Spacer(1, 12),
		Paragraph(
			f'Liczba rezerwacji: {summary["total_bookings"]} | '
			f'Łączny czas: {summary["total_hours"]:.1f} h | '
			f'Przychód: {summary["total_revenue"]:.2f} PLN',
			styles['BodyText'],
		),
		Spacer(1, 16),
		Paragraph('Top 10 sal', styles['Heading2']),
		build_rooms_table(room_stats),
		Spacer(1, 16),
		Paragraph('Top 10 użytkowników', styles['Heading2']),
		build_users_table(user_stats),
		Spacer(1, 16),
		Paragraph('Wykres wykorzystania sal', styles['Heading2']),
		build_utilization_chart(room_stats),
	]

	doc.build(story)
	return buffer


def build_summary(bookings):
	return {
		'total_bookings': len(bookings),
		'total_hours': sum(booking.duration_hours for booking in bookings),
		'total_revenue': sum(booking.total_cost for booking in bookings),
	}


def build_room_stats(bookings):
	aggregate = defaultdict(lambda: {'bookings': 0, 'hours': 0.0, 'revenue': 0.0})
	for booking in bookings:
		room_name = booking.room.name if booking.room else 'Brak sali'
		aggregate[room_name]['bookings'] += 1
		aggregate[room_name]['hours'] += booking.duration_hours
		aggregate[room_name]['revenue'] += booking.total_cost

	return [
		{
			'room': room,
			'bookings': values['bookings'],
			'hours': round(values['hours'], 1),
			'revenue': round(values['revenue'], 2),
		}
		for room, values in sorted(
			aggregate.items(),
			key=lambda item: (item[1]['bookings'], item[1]['hours']),
			reverse=True,
		)[:10]
	]


def build_user_stats(bookings):
	aggregate = defaultdict(int)
	for booking in bookings:
		user_name = booking.user.name if booking.user else 'Brak użytkownika'
		aggregate[user_name] += 1

	return [
		{'user': user, 'bookings': count}
		for user, count in sorted(
			aggregate.items(),
			key=lambda item: item[1],
			reverse=True,
		)[:10]
	]


def build_rooms_table(room_stats):
	data = [['Sala', 'Rezerwacje', 'Godziny', 'Przychód (PLN)']]
	for item in room_stats:
		data.append([
			item['room'],
			item['bookings'],
			f"{item['hours']:.1f}",
			f"{item['revenue']:.2f}",
		])

	return styled_table(data, [160, 90, 90, 110])


def build_users_table(user_stats):
	data = [['Użytkownik', 'Rezerwacje']]
	for item in user_stats:
		data.append([item['user'], item['bookings']])

	return styled_table(data, [280, 120])


def styled_table(data, column_widths):
	table = Table(data, colWidths=column_widths, hAlign='LEFT')
	table.setStyle(TableStyle([
		('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0d6efd')),
		('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
		('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#ced4da')),
		('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
		('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
		('ALIGN', (1, 1), (-1, -1), 'CENTER'),
		('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
		('BOTTOMPADDING', (0, 0), (-1, -1), 8),
		('TOPPADDING', (0, 0), (-1, -1), 8),
	]))
	return table


def build_utilization_chart(room_stats):
	chart_buffer = BytesIO()
	chart_image = PILImage.new('RGB', (900, 360), 'white')
	draw = ImageDraw.Draw(chart_image)

	values = [item['hours'] for item in room_stats[:10]] or [0]
	labels = [item['room'] for item in room_stats[:10]] or ['Brak danych']
	max_value = max(values) if max(values) > 0 else 1

	left_margin = 60
	right_margin = 30
	top_margin = 30
	bottom_margin = 90
	chart_height = 360 - top_margin - bottom_margin
	chart_width = 900 - left_margin - right_margin
	bar_width = max(chart_width // (len(values) * 2), 28)
	gap = bar_width

	draw.text((left_margin, 8), 'Godziny rezerwacji per sala', fill='#212529')
	draw.line((left_margin, top_margin, left_margin, top_margin + chart_height), fill='#6c757d', width=2)
	draw.line((left_margin, top_margin + chart_height, left_margin + chart_width, top_margin + chart_height), fill='#6c757d', width=2)

	for index, value in enumerate(values):
		x0 = left_margin + gap // 2 + index * (bar_width + gap)
		x1 = x0 + bar_width
		bar_height = int((value / max_value) * (chart_height - 20)) if max_value else 0
		y0 = top_margin + chart_height - bar_height
		y1 = top_margin + chart_height
		draw.rectangle((x0, y0, x1, y1), fill='#20c997', outline='#0f5132')
		draw.text((x0, y0 - 18), f'{value:.1f}h', fill='#212529')
		draw.text((x0, y1 + 8), labels[index][:12], fill='#212529')

	chart_image.save(chart_buffer, format='PNG')
	chart_buffer.seek(0)
	image = Image(chart_buffer, width=460, height=220)
	image.hAlign = 'LEFT'
	return image