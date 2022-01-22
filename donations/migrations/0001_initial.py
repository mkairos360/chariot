# Generated by Django 4.0.1 on 2022-01-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount_donated', models.FloatField(default=0.0)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NonFinancialDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor', models.CharField(max_length=255)),
                ('item', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(blank=True, default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Material Donation',
                'verbose_name_plural': 'Material Donations',
            },
        ),
    ]
