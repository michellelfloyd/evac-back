# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_auto_20141108_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='color',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='parent',
            field=models.ForeignKey(blank=True, to='public.ToTake', null=True),
            preserve_default=True,
        ),
    ]
