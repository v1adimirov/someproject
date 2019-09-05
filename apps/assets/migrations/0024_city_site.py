# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0023_vologdacity_recipient_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='site',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0430\u0439\u0442 \u0422\u0420\u0426', blank=True),
            preserve_default=True,
        ),
    ]
