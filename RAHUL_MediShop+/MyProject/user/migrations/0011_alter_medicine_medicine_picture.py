# Generated by Django 5.0.6 on 2024-05-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_medicine_medicine_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='medicine_picture',
            field=models.ImageField(null=True, upload_to='static/event/'),
        ),
    ]