# Generated by Django 4.0.1 on 2022-01-17 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0023_remove_member_welfare_contributions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Welfare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welfare_title', models.CharField(max_length=255)),
                ('welfare_description', models.TextField(blank=True, null=True)),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WelfareContributions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_contributed', models.FloatField(default=0.0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_welfare_contributions', to='membership.member')),
                ('welfare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='welfare_contributions', to='welfare.welfare')),
            ],
        ),
    ]
