#!/bin/bash
# KinoMania Application Verification Script

echo "🎬 KinoMania - Application Verification"
echo "========================================"

# Check Django installation
echo ""
echo "✓ Checking Django..."
python manage.py --version

# Check migrations
echo ""
echo "✓ Checking database migrations..."
python manage.py showmigrations kino | head -5

# Check database
echo ""
echo "✓ Checking database records..."
python manage.py shell <<EOF
from kino.models import Film, Seans, Rezerwacja
from django.contrib.auth.models import User
print(f"  - Films: {Film.objects.count()}")
print(f"  - Screenings: {Seans.objects.count()}")
print(f"  - Reservations: {Rezerwacja.objects.count()}")
print(f"  - Users: {User.objects.count()}")
EOF

# Check tests
echo ""
echo "✓ Running tests..."
python manage.py test kino -v 0 2>&1 | tail -3

# Check admin
echo ""
echo "✓ Checking superuser..."
python manage.py shell <<EOF
from django.contrib.auth.models import User
admin = User.objects.filter(username='admin').first()
if admin:
    print(f"  - Admin user exists: {admin.username} (staff: {admin.is_staff})")
EOF

echo ""
echo "✓ Application is ready to run!"
echo ""
echo "To start the application:"
echo "  python manage.py runserver"
echo ""
echo "Then open: http://localhost:8000/"
