# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0012_auto_20190521_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.EmailField(default=b'', max_length=255, verbose_name='Email', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience',
            field=models.TextField(default=b'', verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e \u043e \u0412\u0430\u0448\u0435\u043c \u043e\u043f\u044b\u0442\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resume',
            name='first_name',
            field=models.CharField(default=b'', max_length=255, verbose_name='\u0418\u043c\u044f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resume',
            name='last_name',
            field=models.CharField(default=b'', max_length=255, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resume',
            name='phone',
            field=models.CharField(default=b'', max_length=255, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True),
            preserve_default=True,
        ),
    ]
