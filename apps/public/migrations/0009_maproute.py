# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0008_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapRoute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('origin', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('waypoints', models.TextField()),
                ('waypoint_names', models.TextField()),
                ('travel_mode', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
