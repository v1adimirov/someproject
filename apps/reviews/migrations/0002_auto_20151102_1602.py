# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoreview',
            name='on_act',
            field=models.BooleanField(default=False, verbose_name='\u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u0442\u043e\u0440\u0433\u043e\u0432\u043e\u0433\u043e \u0446\u0435\u043d\u0442\u0440\u0430'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videoreview',
            name='on_main',
            field=models.BooleanField(default=False, verbose_name='\u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439'),
            preserve_default=True,
        ),
    ]
