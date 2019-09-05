# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0030_franchvologda_franchvologdafeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='vologdamart',
            name='franch_text',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u0441 \u0444\u0440\u0430\u043d\u0448\u0438\u0437\u0430\u043c\u0438', blank=True),
            preserve_default=True,
        ),
    ]
