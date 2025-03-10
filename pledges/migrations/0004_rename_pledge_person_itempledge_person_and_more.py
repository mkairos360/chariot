# Generated by Django 4.0.1 on 2022-04-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pledges', '0003_remove_membermonetarypledge_contact_information'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itempledge',
            old_name='pledge_person',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='monetarypledge',
            old_name='pledge_person',
            new_name='person',
        ),
        migrations.AddField(
            model_name='memberitempledge',
            name='person',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membermonetarypledge',
            name='person',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
