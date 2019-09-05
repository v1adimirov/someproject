# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sliders', '0003_remove_mainslideritem_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainslideritem',
            name='link',
            field=models.CharField(max_length=500, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430', blank=True),
            preserve_default=True,
        ),
    ]
