# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_booked', models.DateField()),
                ('time_booked', models.TimeField()),
            ],
        ),
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
            name='Tours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
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
            field=models.ForeignKey(to='book.Person'),
        ),
    ]
