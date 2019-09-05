# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0004_auto_20190517_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='adv',
            name='weight',
            field=models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430'),
            preserve_default=True,
        ),
    ]
