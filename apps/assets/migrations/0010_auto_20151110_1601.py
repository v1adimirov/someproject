# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0009_auto_20151104_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='photo_link',
            field=models.CharField(max_length=255, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0444\u043e\u0442\u043e\u043e\u0442\u0447\u0435\u0442\u044b', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
            preserve_default=True,
        ),
    ]
