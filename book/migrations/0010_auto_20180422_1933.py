# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_auto_20180422_1838'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Booking'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person'},
        ),
    ]
