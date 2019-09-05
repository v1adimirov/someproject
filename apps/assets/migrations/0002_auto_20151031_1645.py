# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='map_latitude',
            field=models.CharField(default='54.19372551', max_length=255, verbose_name='\u0448\u0438\u0440\u043e\u0442\u0430 \u0446\u0435\u043d\u0442\u0440\u0430 \u043a\u0430\u0440\u0442\u044b'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='map_longitude',
            field=models.CharField(default='37.64137673', max_length=255, verbose_name='\u0434\u043e\u043b\u0433\u043e\u0442\u0430 \u0446\u0435\u043d\u0442\u0440\u0430 \u043a\u0430\u0440\u0442\u044b'),
            preserve_default=False,
        ),
    ]
