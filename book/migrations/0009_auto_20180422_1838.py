# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20180422_0203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='type',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='time',
        ),
        migrations.AddField(
            model_name='booking',
            name='date_time_booked',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 22, 18, 38, 49, 294202, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tour',
        ),
        migrations.DeleteModel(
            name='TourType',
        ),
    ]
