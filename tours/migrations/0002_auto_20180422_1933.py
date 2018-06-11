# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tour',
            options={'verbose_name': 'Tour'},
        ),
        migrations.AlterModelOptions(
            name='tourtype',
            options={'verbose_name': 'Available Tour'},
        ),
        migrations.RemoveField(
            model_name='tour',
            name='type',
        ),
    ]
