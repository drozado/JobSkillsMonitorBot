# Generated by Django 3.1.7 on 2021-03-25 01:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210325_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='region',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='listing',
            name='date_listed',
            field=models.DateField(default=datetime.datetime(2021, 3, 25, 1, 31, 31, 150535, tzinfo=utc)),
        ),
    ]
