# Generated by Django 2.2.6 on 2021-03-18 06:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0007_auto_20210318_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculties',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 3, 18, 12, 13, 26, 677875)),
        ),
    ]