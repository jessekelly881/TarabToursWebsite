# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_auto_20180516_1947'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tour',
        ),
    ]
