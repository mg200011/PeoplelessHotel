# Generated by Django 3.0.8 on 2020-07-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0007_remove_guests_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='guests',
            name='rooms',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
