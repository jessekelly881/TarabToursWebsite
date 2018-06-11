# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactrequest',
            name='body',
        ),
        migrations.RemoveField(
            model_name='contactrequest',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='contactrequest',
            name='last_name',
        ),
    ]
