# Generated by Django 2.1.15 on 2020-07-29 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_reservations_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='status',
            field=models.CharField(choices=[('RESERVED', 'RESERVED'), ('CANCELED', 'CANCELED'), ('CHECKED_IN', 'CHECKED_IN'), ('CHECKED_OUT', 'CHECKED_OUT')], max_length=32),
        ),
    ]