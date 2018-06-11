# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20180422_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactrequest',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 4, 22, 1, 51, 59, 775342, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactrequest',
            name='requests_body',
            field=models.CharField(default='Blank', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactrequest',
            name='time',
            field=models.TimeField(default=datetime.datetime(2018, 4, 22, 1, 53, 2, 314405, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
