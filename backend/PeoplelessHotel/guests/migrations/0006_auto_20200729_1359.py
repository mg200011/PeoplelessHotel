# Generated by Django 3.0.8 on 2020-07-29 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0005_auto_20200728_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guests',
            name='image_sample_1',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='guests',
            name='image_sample_2',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='guests',
            name='image_sample_3',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
