# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20180422_0153'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactRequest',
        ),
    ]
