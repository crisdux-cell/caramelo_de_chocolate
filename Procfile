web: python manage.py migrate && python manage.py create_admin && gunicorn movilnet_config.wsgi:application --bind 0.0.0.0:$PORT
