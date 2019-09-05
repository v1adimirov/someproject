# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sliders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainslideritem',
            name='subtitle',
            field=models.CharField(max_length=255, verbose_name='\u043f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mainslideritem',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
            preserve_default=True,
        ),
    ]
