# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_tour'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tour',
            options={'verbose_name': 'Tour'},
        ),
        migrations.AddField(
            model_name='tour',
            name='cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
