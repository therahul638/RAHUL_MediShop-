# Generated by Django 5.0.6 on 2024-05-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_rename_event_des_imagegallery_medicine_des_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='medicine_picture',
            field=models.ImageField(null=True, upload_to='static/medicine/'),
        ),
    ]
