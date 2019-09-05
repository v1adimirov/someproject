# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenda', '0004_auto_20151112_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='mart',
            name='arenda_type',
            field=models.PositiveIntegerField(default=1, verbose_name='\u0422\u0438\u043f \u043e\u0431\u044a\u0435\u043a\u0442\u0430 \u0434\u043b\u044f \u0437\u0430\u044f\u0432\u043a\u0438 \u043d\u0430 \u0430\u0440\u0435\u043d\u0434\u0443', choices=[(1, '\u0434\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439'), (2, '\u0441\u0442\u0440\u043e\u044f\u0449\u0438\u0439\u0441\u044f')]),
            preserve_default=True,
        ),
    ]
