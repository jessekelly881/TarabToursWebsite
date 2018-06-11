# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_auto_20180523_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='cost',
        ),
    ]
