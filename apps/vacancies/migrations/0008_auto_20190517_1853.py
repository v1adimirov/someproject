# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0007_auto_20190517_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactperson',
            name='phones',
            field=models.CharField(help_text=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80\xd0\xb0 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xbe\xd0\xb2 \xd1\x80\xd0\xb0\xd0\xb7\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8f\xd1\x8e\xd1\x82\xd1\x81\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x8f\xd1\x82\xd0\xbe\xd0\xb9', max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u044b'),
            preserve_default=True,
        ),
    ]
