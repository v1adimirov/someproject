# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0009_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideritem',
            name='comment',
            field=models.CharField(default=b'', max_length=255, verbose_name='\u043f\u043e\u0434\u043f\u0438\u0441\u044c', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slideritem',
            name='date',
            field=models.CharField(default=b'', max_length=255, verbose_name='\u0434\u0430\u0442\u0430', blank=True),
            preserve_default=True,
        ),
    ]
