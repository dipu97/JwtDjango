# Generated by Django 5.1.5 on 2025-02-25 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_Staff',
            new_name='is_staff',
        ),
    ]
