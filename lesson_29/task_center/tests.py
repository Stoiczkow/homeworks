import io
from unittest.mock import Mock, patch

from PIL import Image

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import EmailNotification, GeneratedCsvReport, ScrapedPageTitle, UploadedImage
from .tasks import classify_uploaded_image, generate_users_csv, multiply, scrape_example_title, send_email_notification


class TaskCenterTests(TestCase):
    def _make_test_image(self):
        image_bytes = io.BytesIO()
        image = Image.new('RGB', (20, 10), color='red')
        image.save(image_bytes, format='PNG')
        image_bytes.seek(0)
        return SimpleUploadedFile('test.png', image_bytes.read(), content_type='image/png')

    def test_dashboard_returns_200(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Centrum zadań Celery')

    def test_multiply_task_returns_product(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_send_email_notification_marks_model_as_sent(self):
        notification = EmailNotification.objects.create(
            recipient_email='test@example.com',
            subject='Temat',
            body='Treść',
        )
        send_email_notification(notification.id)
        notification.refresh_from_db()
        self.assertIsNotNone(notification.sent_at)

    @patch('task_center.tasks.requests.get')
    def test_scrape_task_saves_title(self, mock_get):
        mock_response = Mock()
        mock_response.text = '<html><head><title>Przykładowa strona</title></head></html>'
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = scrape_example_title('https://example.com')

        self.assertEqual(result, 'Przykładowa strona')
        self.assertTrue(ScrapedPageTitle.objects.filter(title='Przykładowa strona').exists())

    def test_csv_report_and_image_classification_tasks(self):
        User.objects.create_user(username='anna', email='anna@example.com', password='Haslo123!')
        report = GeneratedCsvReport.objects.create(task_id='manual-test')
        generate_users_csv(report.id)
        report.refresh_from_db()
        self.assertTrue(bool(report.report_file))

        uploaded_image = UploadedImage.objects.create(image=self._make_test_image())
        classify_uploaded_image(uploaded_image.id)
        uploaded_image.refresh_from_db()
        self.assertIn('Obraz', uploaded_image.classification_result)
