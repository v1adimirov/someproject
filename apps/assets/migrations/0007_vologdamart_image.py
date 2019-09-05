# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_auto_20151104_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='vologdamart',
            name='image',
            field=models.ImageField(default='', upload_to=b'assets', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
            preserve_default=False,
        ),
    ]
