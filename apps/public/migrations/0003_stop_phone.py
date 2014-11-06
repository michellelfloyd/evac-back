# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20141029_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='stop',
            name='phone',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
