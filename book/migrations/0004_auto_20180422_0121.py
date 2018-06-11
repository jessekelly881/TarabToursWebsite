# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20180422_0119'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tours',
            new_name='Tour',
        ),
    ]
