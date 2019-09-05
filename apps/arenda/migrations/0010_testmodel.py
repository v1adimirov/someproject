# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenda', '0009_mart_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=255, verbose_name='email')),
            ],
            options={
                'verbose_name': 'test',
                'verbose_name_plural': 'test',
            },
            bases=(models.Model,),
        ),
    ]
