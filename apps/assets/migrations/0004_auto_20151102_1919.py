# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20151102_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='city',
            field=models.ForeignKey(verbose_name=b'\xd0\xb3\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', blank=True, to='assets.City', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='email', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d', blank=True),
            preserve_default=True,
        ),
    ]
