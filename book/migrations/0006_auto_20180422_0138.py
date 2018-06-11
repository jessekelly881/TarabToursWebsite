# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20180422_0130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email_address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TourType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=3000)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='booked_by',
            field=models.ForeignKey(default=0, to='book.Person'),
        ),
    ]
