# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20180422_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booked_by',
            field=models.ForeignKey(default=1, to='book.Person'),
        ),
    ]
