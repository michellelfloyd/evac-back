# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0006_auto_20141111_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='count',
            field=models.CharField(max_length=3, null=True, blank=True),
            preserve_default=True,
        ),
    ]
