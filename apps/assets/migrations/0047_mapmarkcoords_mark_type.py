# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0046_auto_20170426_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapmarkcoords',
            name='mark_type',
            field=models.CharField(help_text='\u043e\u0441\u0442\u0430\u0432\u0442\u0435 \u043f\u043e\u043b\u0435 \u043d\u0435\u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u043c \u0435\u0441\u043b\u0438 \u044d\u0442\u043e \u043c\u0435\u0442\u043a\u0430 \u0422\u0426', max_length=100, null=True, verbose_name='\u0442\u0438\u043f \u043c\u0435\u0442\u043a\u0438', blank=True),
            preserve_default=True,
        ),
    ]
