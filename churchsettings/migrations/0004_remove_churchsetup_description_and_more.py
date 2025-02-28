# Generated by Django 4.0.1 on 2022-04-23 18:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('churchsettings', '0003_churchsettings_church'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='churchsetup',
            name='description',
        ),
        migrations.AddField(
            model_name='churchsetup',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 4, 23, 18, 24, 34, 933876, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='churchsetup',
            name='email',
            field=models.EmailField(default='church@example.com', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='churchsetup',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
