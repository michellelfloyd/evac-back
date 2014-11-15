# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0007_pet_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='parent',
            field=models.ForeignKey(default=1, to='public.ToTake'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='parent',
            field=models.ForeignKey(default=1, to='public.ToTake'),
            preserve_default=False,
        ),
    ]
