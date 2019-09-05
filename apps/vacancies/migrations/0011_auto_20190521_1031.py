# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0010_auto_20190521_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adv',
            name='description',
            field=models.TextField(default=b'', verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
    ]
