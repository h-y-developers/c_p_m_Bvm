# Generated by Django 3.1.5 on 2021-03-18 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0007_auto_20210318_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculties',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 3, 18, 18, 42, 53, 982832)),
        ),
    ]