# Generated by Django 3.1.5 on 2021-03-18 18:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0013_auto_20210318_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculties',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 3, 19, 0, 25, 23, 44793)),
        ),
    ]