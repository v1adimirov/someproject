# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0014_auto_20151210_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vologdabrend',
            options={'ordering': ['weight', 'pk'], 'verbose_name': '\u0431\u0440\u0435\u043d\u0434', 'verbose_name_plural': '\u0431\u0440\u0435\u043d\u0434\u044b \u0442\u043e\u0440\u0433\u043e\u0432\u043e\u0433\u043e \u0446\u0435\u043d\u0442\u0440\u0430'},
        ),
    ]
