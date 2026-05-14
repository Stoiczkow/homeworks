from celery import chain
from celery.result import AsyncResult
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import EmailNotificationForm, MultiplyForm, UpdateLastLoginForm, UploadImageForm
from .models import EmailNotification, GeneratedCsvReport, LogEntry, ScrapedPageTitle, UploadedImage
from .tasks import (
	classify_uploaded_image,
	count_users,
	flaky_url_check,
	generate_random_number,
	generate_users_csv,
	hello_world,
	log_timestamp,
	multiply,
	multiply_by_ten,
	scrape_example_title,
	send_email_notification,
	save_chain_result,
	simulate_video_processing,
	tracked_progress_task,
	update_user_last_login,
)


def _build_dashboard_context(**overrides):
	context = {
		'multiply_form': MultiplyForm(),
		'email_form': EmailNotificationForm(),
		'upload_form': UploadImageForm(),
		'update_last_login_form': UpdateLastLoginForm(),
		'recent_notifications': EmailNotification.objects.all()[:5],
		'recent_logs': LogEntry.objects.all()[:6],
		'recent_titles': ScrapedPageTitle.objects.all()[:5],
		'recent_reports': GeneratedCsvReport.objects.all()[:5],
		'recent_images': UploadedImage.objects.all()[:5],
		'users': User.objects.order_by('username')[:10],
	}
	context.update(overrides)
	return context


def dashboard_view(request):
	return render(request, 'task_center/dashboard.html', _build_dashboard_context())


def hello_world_view(request):
	if request.method == 'POST':
		task = hello_world.delay()
		messages.success(request, f'Zadanie hello_world zostało uruchomione. Task ID: {task.id}')
	return redirect('dashboard')


def multiply_view(request):
	if request.method == 'POST':
		form = MultiplyForm(request.POST)
		if form.is_valid():
			task = multiply.delay(form.cleaned_data['a'], form.cleaned_data['b'])
			result_text = f' Wynik: {task.result}.' if task.ready() else ''
			messages.success(request, f'Zadanie multiply dodano do kolejki. Task ID: {task.id}.{result_text}')
			return redirect('dashboard')
		return render(request, 'task_center/dashboard.html', _build_dashboard_context(multiply_form=form))
	return redirect('dashboard')


def log_timestamp_view(request):
	if request.method == 'POST':
		task = log_timestamp.delay()
		messages.success(request, f'Dodano zadanie log_timestamp. Task ID: {task.id}')
	return redirect('dashboard')


def count_users_view(request):
	if request.method == 'POST':
		task = count_users.delay()
		result_text = f' Liczba użytkowników: {task.result}.' if task.ready() else ''
		messages.success(request, f'Dodano zadanie count_users. Task ID: {task.id}.{result_text}')
	return redirect('dashboard')


def update_last_login_view(request):
	if request.method == 'POST':
		form = UpdateLastLoginForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data['user']
			task = update_user_last_login.delay(user.id)
			messages.success(request, f'Zlecono aktualizację last_login dla {user.username}. Task ID: {task.id}')
			return redirect('dashboard')
		return render(request, 'task_center/dashboard.html', _build_dashboard_context(update_last_login_form=form))
	return redirect('dashboard')


def video_processing_view(request):
	if request.method == 'POST':
		task = simulate_video_processing.delay(15)
		messages.success(request, f'Przetwarzanie wideo rozpoczęte! Task ID: {task.id}')
	return redirect('dashboard')


def email_notification_view(request):
	if request.method == 'POST':
		form = EmailNotificationForm(request.POST)
		if form.is_valid():
			notification = form.save()
			task = send_email_notification.delay(notification.id)
			messages.success(request, f'Powiadomienie mailowe zostało zapisane i wysłane do kolejki. Task ID: {task.id}')
			return redirect('dashboard')
		return render(request, 'task_center/dashboard.html', _build_dashboard_context(email_form=form))
	return redirect('dashboard')


def scrape_example_view(request):
	if request.method == 'POST':
		task = scrape_example_title.delay()
		messages.success(request, f'Zadanie scrapingu zostało uruchomione. Task ID: {task.id}')
	return redirect('dashboard')


def start_progress_view(request):
	if request.method == 'POST':
		task = tracked_progress_task.delay()
		status_url = reverse('task-status', args=[task.id])
		messages.success(request, f'Zadanie śledzenia postępu ruszyło. Task ID: {task.id}. Status: {status_url}')
	return redirect('dashboard')


def task_status_view(request, task_id):
	result = AsyncResult(task_id)
	payload = {
		'task_id': task_id,
		'state': result.state,
	}

	if result.state == 'PROGRESS' and isinstance(result.info, dict):
		payload['progress'] = result.info
	elif result.state == 'SUCCESS':
		payload['result'] = result.result
	elif result.state == 'FAILURE':
		payload['error'] = str(result.result)
	elif result.info is not None:
		payload['meta'] = str(result.info)

	return JsonResponse(payload)


def start_csv_report_view(request):
	if request.method == 'POST':
		report = GeneratedCsvReport.objects.create()
		task = generate_users_csv.delay(report.id)
		report.task_id = task.id
		report.save(update_fields=['task_id'])
		status_url = reverse('csv-report-status', args=[task.id])
		messages.success(request, f'Generowanie raportu CSV rozpoczęte. Task ID: {task.id}. Status: {status_url}')
	return redirect('dashboard')


def csv_report_status_view(request, task_id):
	result = AsyncResult(task_id)
	report = GeneratedCsvReport.objects.filter(task_id=task_id).first()
	payload = {
		'task_id': task_id,
		'state': result.state,
	}

	if result.state == 'SUCCESS':
		payload['result'] = result.result
	if report and report.report_file:
		payload['download_url'] = request.build_absolute_uri(report.report_file.url)
		payload['report_id'] = report.id

	return JsonResponse(payload)


def upload_image_view(request):
	if request.method == 'POST':
		form = UploadImageForm(request.POST, request.FILES)
		if form.is_valid():
			image = form.save()
			task = classify_uploaded_image.delay(image.id)
			messages.success(request, f'Obraz został zapisany i przekazany do klasyfikacji. Task ID: {task.id}')
			return redirect('dashboard')
		return render(request, 'task_center/dashboard.html', _build_dashboard_context(upload_form=form))
	return redirect('dashboard')


def retry_demo_view(request):
	if request.method == 'POST':
		task = flaky_url_check.delay('https://nieistniejacy-adres-przyklad.invalid')
		messages.info(request, f'Uruchomiono zadanie z ponawianiem prób. Task ID: {task.id}')
	return redirect('dashboard')


def start_chain_view(request):
	if request.method == 'POST':
		chain_result = chain(generate_random_number.s(), multiply_by_ten.s(), save_chain_result.s()).apply_async()
		messages.success(request, f'Łańcuch zadań został uruchomiony. Task ID: {chain_result.id}')
	return redirect('dashboard')
