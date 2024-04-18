release: python manage.py makemigrations && python manage.py migrate
web: gunicorn brainbox_api.wsgi:application --log-file -