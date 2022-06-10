# Generated by Django 4.0.1 on 2022-04-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pledges', '0007_itempledge_email_itempledge_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempledge',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='itempledge',
            name='phone_number',
            field=models.TextField(default='0234590897'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='memberitempledge',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='memberitempledge',
            name='phone_number',
            field=models.TextField(default=233503422990),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='membermonetarypledge',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='membermonetarypledge',
            name='phone_number',
            field=models.TextField(default=233503422990),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='monetarypledge',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='monetarypledge',
            name='phone_number',
            field=models.TextField(default=503422990),
            preserve_default=False,
        ),
    ]
