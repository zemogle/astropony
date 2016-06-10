# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name=b'date discovered')),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('discovery_date', models.DateTimeField(verbose_name=b'date discovered')),
                ('mass', models.FloatField()),
                ('radius', models.FloatField()),
                ('misson', models.ForeignKey(to='exoplanets.Mission')),
            ],
        ),
    ]
