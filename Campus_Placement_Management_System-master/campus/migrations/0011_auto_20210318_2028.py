# Generated by Django 3.1.5 on 2021-03-18 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0010_auto_20210318_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculties',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 3, 18, 20, 28, 15, 292739)),
        ),
        migrations.AlterField(
            model_name='student',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]