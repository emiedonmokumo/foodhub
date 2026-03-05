from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = 'Create a single admin user using environment variables or defaults'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.getenv('ADMIN_USERNAME', 'admin')
        password = os.getenv('ADMIN_PASSWORD', 'ChangeMe123!')
        email = os.getenv('ADMIN_EMAIL', '')

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'Admin user "{username}" already exists'))
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f'Created admin user "{username}"'))
