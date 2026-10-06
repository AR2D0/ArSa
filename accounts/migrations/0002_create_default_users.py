from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_users(apps, schema_editor):
    User = apps.get_model('accounts', 'User')

    if not User.objects.filter(username='arshia').exists():
        User.objects.create(
            username='arshia',
            email='arshia@arsa.local',
            display_name='Arshia',
            role='admin',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            password=make_password('@Rshia2007'),
        )

    if not User.objects.filter(username='samina').exists():
        User.objects.create(
            username='samina',
            email='samina@arsa.local',
            display_name='Samina',
            role='user',
            is_staff=False,
            is_superuser=False,
            is_active=True,
            password=make_password('kian2010'),
        )


def reverse_users(apps, schema_editor):
    User = apps.get_model('accounts', 'User')
    User.objects.filter(username__in=['arshia', 'samina']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users, reverse_users),
    ]