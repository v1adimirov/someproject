# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0040_auto_20160614_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0430\u0434\u0440\u0435\u0441', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='area',
            field=models.CharField(max_length=255, null=True, verbose_name='\u043f\u043b\u043e\u0449\u0430\u0434\u044c', blank=True),
            preserve_default=True,
        ),
    ]
