# Generated by Django 4.1.6 on 2023-02-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VPO', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User_organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
