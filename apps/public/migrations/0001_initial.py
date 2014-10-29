# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvacPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Evac Plan',
                'verbose_name_plural': 'Evac Plans',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Pet',
                'verbose_name_plural': 'Pets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startPoint', models.CharField(max_length=200)),
                ('transportMode', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Stop',
                'verbose_name_plural': 'Stops',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Supply',
                'verbose_name_plural': 'Supplies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmergencySupply',
            fields=[
                ('supply_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='public.Supply')),
            ],
            options={
                'verbose_name': 'Emergency Supply',
                'verbose_name_plural': 'Emergency Supplies',
            },
            bases=('public.supply',),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('supply_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='public.Supply')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
            bases=('public.supply',),
        ),
        migrations.CreateModel(
            name='TechAndValuable',
            fields=[
                ('supply_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='public.Supply')),
            ],
            options={
                'verbose_name': 'Tech And Valuable',
                'verbose_name_plural': 'Tech And Valuables',
            },
            bases=('public.supply',),
        ),
        migrations.CreateModel(
            name='ToTake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evacPlan', models.OneToOneField(to='public.EvacPlan')),
            ],
            options={
                'verbose_name': 'To Take',
                'verbose_name_plural': 'To Takes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TravelTool',
            fields=[
                ('supply_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='public.Supply')),
            ],
            options={
                'verbose_name': 'Travel Tool',
                'verbose_name_plural': 'Travel Tools',
            },
            bases=('public.supply',),
        ),
        migrations.AddField(
            model_name='route',
            name='destinations',
            field=models.ManyToManyField(to='public.Stop'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='route',
            name='route',
            field=models.OneToOneField(to='public.EvacPlan'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pet',
            name='parent',
            field=models.ForeignKey(to='public.ToTake'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pet',
            name='supplies',
            field=models.ManyToManyField(to='public.Supply'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='parent',
            field=models.ForeignKey(to='public.ToTake'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='supplies',
            field=models.ManyToManyField(to='public.Supply'),
            preserve_default=True,
        ),
    ]
