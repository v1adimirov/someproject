# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0013_auto_20151209_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='contact_photo',
            field=models.ImageField(upload_to=b'assert', null=True, verbose_name='\u0444\u043e\u0442\u043e \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u043e\u0433\u043e \u043b\u0438\u0446\u0430', blank=True),
            preserve_default=True,
        ),
    ]
