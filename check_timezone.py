from django.core.management.base import BaseCommand
from django.db import connection
from django.utils import timezone

class Command(BaseCommand):
    help = 'Vérifie la configuration timezone'

    def handle(self, *args, **options):
        # Vérification PostgreSQL
        with connection.cursor() as cursor:
            cursor.execute("SHOW TIMEZONE")
            db_tz = cursor.fetchone()[0]
            self.stdout.write(f"Timezone PostgreSQL: {db_tz}")
            
            cursor.execute("SHOW log_timezone")
            log_tz = cursor.fetchone()[0]
            self.stdout.write(f"Log timezone: {log_tz}")

        # Vérification Django
        django_tz = str(timezone.get_current_timezone())
        self.stdout.write(f"Timezone Django: {django_tz}")

        # Validation
        if db_tz == 'UTC' and django_tz == 'UTC':
            self.stdout.write(self.style.SUCCESS("✓ Configuration UTC valide"))
        else:
            self.stdout.write(self.style.ERROR("× Problème de configuration timezone"))