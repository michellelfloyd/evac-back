# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_auto_20141108_0243'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialConditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='person',
            name='specialConditions',
        ),
        migrations.AddField(
            model_name='person',
            name='special_conditions',
            field=models.ManyToManyField(to='public.SpecialConditions'),
            preserve_default=True,
        ),
    ]
