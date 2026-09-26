import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Crea un superusuario automáticamente desde variables de entorno'

    def handle(self, *args, **options):
        username = os.environ.get('ADMIN_USER', 'admin')
        password = os.environ.get('ADMIN_PASSWORD', 'admin1234')
        email = os.environ.get('ADMIN_EMAIL', 'admin@movilnet.com')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'✅ Superusuario "{username}" creado exitosamente'))
        else:
            self.stdout.write(self.style.WARNING(f'⚠️ El usuario "{username}" ya existe'))
