# Generated by Django 3.0.8 on 2020-07-12 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20200712_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='is_published',
        ),
    ]
