# Generated by Django 5.0.6 on 2024-05-30 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_rename_speaker_name_medicine_medicine_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='hotel',
            new_name='shop',
        ),
        migrations.AlterField(
            model_name='placename',
            name='ppic',
            field=models.ImageField(null=True, upload_to='static/Shop/'),
        ),
    ]
