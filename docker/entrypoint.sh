#!/bin/bash
set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create superuser if it doesn't exist
echo "Creating superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
from product.models import Measurement
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')

if not Measurement.objects.filter(measure="Unit").exists():
    Measurement.objects.create(measure="Unit")

EOF

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the development server
echo "Starting the development server..."
python manage.py runserver 0.0.0.0:8000
