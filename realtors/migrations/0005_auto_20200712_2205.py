# Generated by Django 3.0.8 on 2020-07-12 22:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0004_auto_20200712_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 12, 22, 5, 2, 770471)),
        ),
    ]
