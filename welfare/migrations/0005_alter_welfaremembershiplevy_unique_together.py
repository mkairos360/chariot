# Generated by Django 4.0.1 on 2022-04-10 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welfare', '0004_rename_month_levy_paid_welfaremembershiplevy_month_welfare_paid'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='welfaremembershiplevy',
            unique_together={('month', 'year')},
        ),
    ]
