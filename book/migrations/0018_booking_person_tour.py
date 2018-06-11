# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_auto_20180529_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time_booked', models.DateTimeField(auto_now_add=True)),
                ('confirmation_number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Booking',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'verbose_name': 'Tour',
            },
        ),
    ]
