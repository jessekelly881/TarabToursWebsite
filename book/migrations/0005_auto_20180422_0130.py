# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20180422_0121'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TourType',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booked_by',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
