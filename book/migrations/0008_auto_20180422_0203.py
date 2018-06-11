# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20180422_0142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='date_booked',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='time_booked',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booked_by',
        ),
        migrations.AddField(
            model_name='booking',
            name='confirmation_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='time',
            field=models.TimeField(default=datetime.datetime(2018, 4, 22, 2, 3, 37, 548926, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='type',
            field=models.ForeignKey(default=1, to='book.TourType'),
            preserve_default=False,
        ),
    ]
