# Generated by Django 5.0.6 on 2024-05-30 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_medicine_medicine_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='speaker_name',
            new_name='medicine_name',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='speaker_picture',
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_picture',
            field=models.ImageField(null=True, upload_to='static/medicine'),
        ),
    ]