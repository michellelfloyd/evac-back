# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_auto_20141105_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, max_length=6, null=True, choices=[(b'Male', b'M'), (b'Female', b'F')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='parent',
            field=models.ForeignKey(blank=True, to='public.ToTake', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='supplies',
            field=models.ManyToManyField(to='public.Supply', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='supplies',
            field=models.ManyToManyField(to='public.Supply', null=True, blank=True),
            preserve_default=True,
        ),
    ]
