# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenda', '0005_mart_arenda_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='mart',
            name='image',
            field=models.ImageField(upload_to=b'arenda', null=True, verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mart',
            name='link',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443 \u0422\u0426'),
            preserve_default=True,
        ),
    ]
