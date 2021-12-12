# Generated by Django 2.2.16 on 2021-09-14 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_confirmation_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='confirmation',
            old_name='code',
            new_name='confirmation_code',
        ),
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
