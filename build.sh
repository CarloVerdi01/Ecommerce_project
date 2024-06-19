#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

DJANGO_SUPERUSER_PASSWORD=my_password ./manage.py createsuperuser \
    --no-input \
    --username=my_user \
    --email=my_user@domain.com

# Apply any outstanding database migrations
python manage.py migrate

