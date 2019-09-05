# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='cities',
            field=models.CharField(max_length=255, verbose_name='\u0433\u043e\u0440\u043e\u0434\u0430', blank=True),
            preserve_default=True,
        ),
    ]
