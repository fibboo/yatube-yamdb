# Generated by Django 2.2.16 on 2021-09-08 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Биография'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, 'user'), (1, 'moderator'), (2, 'admin'), (3, 'superuser')], default=0, verbose_name='Пользовательская роль'),
        ),
    ]
