# Generated by Django 4.0.1 on 2022-01-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0028_alter_member_marital_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='profile_photo',
            field=models.ImageField(default='default_profile_photo.jpg', upload_to='profile_photos'),
        ),
    ]
