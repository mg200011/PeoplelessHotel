# Generated by Django 3.0.8 on 2020-07-29 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0006_auto_20200729_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guests',
            name='birthdate',
        ),
    ]