# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0020_auto_20160507_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='vologdamart',
            name='call_metrica_target',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0446\u0435\u043b\u044c \u042f.\u041c\u0435\u0442\u0440\u0438\u043a\u0438 \u0434\u043b\u044f \u0437\u0430\u043a\u0430\u0437\u0430 \u0437\u0432\u043e\u043d\u043a\u0430', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vologdamart',
            name='metrica_target',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0446\u0435\u043b\u044c \u042f.\u041c\u0435\u0442\u0440\u0438\u043a\u0438 \u0434\u043b\u044f \u0437\u0430\u044f\u0432\u043a\u0438', blank=True),
            preserve_default=True,
        ),
    ]
