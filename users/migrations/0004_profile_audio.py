# Generated by Django 4.1.5 on 2023-02-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_approv'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='audio',
            field=models.FileField(default='default.mp3', upload_to='user_audio', verbose_name='Аудиотрек пользовтеля'),
        ),
    ]
