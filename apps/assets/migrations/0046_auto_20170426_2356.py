# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0045_citymartrecipientemail_cityrecipientemail_vologdamartrecipientemail_vologdarecipientemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='text2',
            field=models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0431\u043b\u043e\u043a 2', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='text3',
            field=models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0431\u043b\u043e\u043a 3', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='text4',
            field=models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0431\u043b\u043e\u043a 4', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='text5',
            field=models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0431\u043b\u043e\u043a 5', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='text',
            field=models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0431\u043b\u043e\u043a 1'),
            preserve_default=True,
        ),
    ]
