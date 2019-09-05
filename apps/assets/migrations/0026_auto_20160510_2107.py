# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0025_auto_20160507_1616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['pk'], 'verbose_name': '\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f', 'verbose_name_plural': '\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438'},
        ),
        migrations.AddField(
            model_name='vologdacity',
            name='call_metrica_target',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0446\u0435\u043b\u044c \u042f.\u041c\u0435\u0442\u0440\u0438\u043a\u0438 \u0434\u043b\u044f \u0437\u0430\u0434\u0430\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441', blank=True),
            preserve_default=True,
        ),
    ]
