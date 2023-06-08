release: python manage.py makemigrations && python manage.py migrate

web:  gunicorn home_furniture.wsgi:application