# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenda', '0007_auto_20160512_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mart',
            name='arenda_type',
            field=models.PositiveIntegerField(default=1, null=True, verbose_name='\u0422\u0438\u043f \u043e\u0431\u044a\u0435\u043a\u0442\u0430 \u0434\u043b\u044f \u0437\u0430\u044f\u0432\u043a\u0438 \u043d\u0430 \u0430\u0440\u0435\u043d\u0434\u0443', blank=True, choices=[(1, '\u0434\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439'), (2, '\u0441\u0442\u0440\u043e\u044f\u0449\u0438\u0439\u0441\u044f')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mart',
            name='image',
            field=models.ImageField(upload_to=b'arenda', null=True, verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mart',
            name='link',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443 \u0422\u0426', blank=True),
            preserve_default=True,
        ),
    ]
