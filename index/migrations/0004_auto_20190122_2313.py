# Generated by Django 2.1 on 2019-01-22 14:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20190122_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 22, 14, 13, 19, 388801, tzinfo=utc), verbose_name='date published'),
        ),
    ]