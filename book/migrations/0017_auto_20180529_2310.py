# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_auto_20180529_2239'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Tour',
        ),
    ]
