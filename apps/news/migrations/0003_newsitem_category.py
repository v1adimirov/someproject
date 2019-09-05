# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20151224_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='category',
            field=models.CharField(default='news', max_length=50, verbose_name='\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', choices=[(b'news', '\u041d\u043e\u0432\u043e\u0441\u0442\u0438'), (b'press', '\u0421\u041c\u0418 \u043e \u043d\u0430\u0441')]),
            preserve_default=False,
        ),
    ]
