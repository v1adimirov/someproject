# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20151103_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='contacts',
            field=models.TextField(null=True, verbose_name='\u043e\u0431\u0449\u0438\u0435 \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u044b', blank=True),
            preserve_default=True,
        ),
    ]
