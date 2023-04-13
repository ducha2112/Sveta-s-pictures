# Generated by Django 4.1.6 on 2023-02-08 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_message_alter_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_type',
            field=models.CharField(choices=[('full', 'Полный пакет'), ('free', 'Бесплатный пакет')], default='free', max_length=30),
        ),
    ]
