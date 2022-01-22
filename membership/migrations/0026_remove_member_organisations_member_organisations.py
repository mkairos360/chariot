# Generated by Django 4.0.1 on 2022-01-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churchorganisations', '0002_remove_churchorganisation_president'),
        ('membership', '0025_member_organisations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='organisations',
        ),
        migrations.AddField(
            model_name='member',
            name='organisations',
            field=models.ManyToManyField(blank=True, null=True, to='churchorganisations.ChurchOrganisation'),
        ),
    ]
