# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0031_vologdamart_franch_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='fb_link',
            field=models.CharField(max_length=255, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 Facebook', blank=True),
            preserve_default=True,
        ),
    ]
