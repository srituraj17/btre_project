# Generated by Django 3.0.8 on 2020-07-12 22:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0003_auto_20200712_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 12, 22, 4, 17, 369746)),
        ),
    ]
