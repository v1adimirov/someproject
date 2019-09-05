# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0056_auto_20170815_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='citymart',
            name='anchor',
            field=models.CharField(max_length=50, null=True, verbose_name='\u044f\u043a\u043e\u0440\u044c', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vologdamart',
            name='anchor',
            field=models.CharField(max_length=50, null=True, verbose_name='\u044f\u043a\u043e\u0440\u044c', blank=True),
            preserve_default=True,
        ),
    ]
