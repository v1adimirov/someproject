# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0032_city_fb_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='quetion_metrica_target',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0446\u0435\u043b\u044c \u042f.\u041c\u0435\u0442\u0440\u0438\u043a\u0438 \u0434\u043b\u044f \u0437\u0430\u0434\u0430\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441', blank=True),
            preserve_default=True,
        ),
    ]
