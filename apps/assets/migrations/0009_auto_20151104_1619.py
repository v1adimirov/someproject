# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_vologdacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vologdafeedback',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='vologdafeedback',
            name='longitude',
        ),
        migrations.AddField(
            model_name='vologdamart',
            name='latitude',
            field=models.CharField(default=52, max_length=255, verbose_name='\u0448\u0438\u0440\u043e\u0442\u0430'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vologdamart',
            name='longitude',
            field=models.CharField(default=48, max_length=255, verbose_name='\u0434\u043e\u043b\u0433\u043e\u0442\u0430'),
            preserve_default=False,
        ),
    ]
