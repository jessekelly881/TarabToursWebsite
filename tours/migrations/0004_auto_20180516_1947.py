# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_auto_20180423_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourtype',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
