# Generated by Django 2.2.16 on 2021-09-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20210916_1633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-id'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=100, verbose_name='Код подтверждения'),
        ),
    ]
