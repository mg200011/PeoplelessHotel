# Generated by Django 3.0.8 on 2020-07-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20200728_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='amenities',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]