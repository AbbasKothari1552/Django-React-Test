# Generated by Django 5.0.6 on 2024-07-06 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_customuser_is_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='otp',
        ),
    ]