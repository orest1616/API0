# Generated by Django 4.1.6 on 2023-02-20 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VPO', '0004_organizer_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_organizer',
            old_name='json',
            new_name='json_data',
        ),
    ]
