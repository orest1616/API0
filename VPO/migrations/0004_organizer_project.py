# Generated by Django 4.1.6 on 2023-02-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VPO', '0003_user_member_json_user_organizer_json'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_organizer', models.CharField(max_length=255)),
            ],
        ),
    ]