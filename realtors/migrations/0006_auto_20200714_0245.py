# Generated by Django 3.0.8 on 2020-07-14 02:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0005_auto_20200712_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 14, 2, 45, 26, 3249)),
        ),
    ]
