@echo off
REM KinoMania Application Verification Script for Windows

echo.
echo 🎬 KinoMania - Application Verification
echo ========================================
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check Django installation
echo Checking Django...
python manage.py --version
echo.

REM Check migrations
echo Checking database migrations...
python manage.py showmigrations kino
echo.

REM Check database records
echo Checking database records...
python manage.py shell -c "from kino.models import Film, Seans, Rezerwacja; from django.contrib.auth.models import User; print(f'  - Films: {Film.objects.count()}'); print(f'  - Screenings: {Seans.objects.count()}'); print(f'  - Reservations: {Rezerwacja.objects.count()}'); print(f'  - Users: {User.objects.count()}')"
echo.

REM Check tests
echo Running tests...
python manage.py test kino -v 0
echo.

REM Check admin
echo Checking superuser...
python manage.py shell -c "from django.contrib.auth.models import User; admin = User.objects.filter(username='admin').first(); print(f'  - Admin user exists: {admin.username}' if admin else '  - No admin user found')"
echo.

echo ✓ Application verification complete!
echo.
echo To start the application:
echo   python manage.py runserver
echo.
echo Then open: http://localhost:8000/
echo.
pause
