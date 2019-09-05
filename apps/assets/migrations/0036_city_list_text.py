# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0035_city_has_marts'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='list_text',
            field=models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 \u0441 \u0434\u0440\u0443\u0433\u0438\u043c\u0438 \u0422\u0426 (\u0435\u0441\u043b\u0438 \u0435\u0441\u0442\u044c)', blank=True),
            preserve_default=True,
        ),
    ]
