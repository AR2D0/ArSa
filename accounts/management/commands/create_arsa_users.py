from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = 'Create default ArSa users (arshia + samina)'

    def handle(self, *args, **options):
        # Admin - Arshia
        if not User.objects.filter(username='arshia').exists():
            User.objects.create_superuser(
                username='arshia',
                email='arshia@arsa.local',
                password='@Rshia2007',
                display_name='Arshia',
                role='admin',
            )
            self.stdout.write(self.style.SUCCESS('Created admin: arshia'))
        else:
            self.stdout.write('Admin arshia already exists')

        # User - Samina
        if not User.objects.filter(username='samina').exists():
            User.objects.create_user(
                username='samina',
                email='samina@arsa.local',
                password='kian2010',
                display_name='Samina',
                role='user',
            )
            self.stdout.write(self.style.SUCCESS('Created user: samina'))
        else:
            self.stdout.write('User samina already exists')