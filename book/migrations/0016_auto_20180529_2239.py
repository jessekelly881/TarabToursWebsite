# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_tour'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='email_address',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default='name', max_length=100),
            preserve_default=False,
        ),
    ]
