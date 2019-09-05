# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20151209_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventorder',
            name='brend',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0411\u0440\u0435\u043d\u0434'),
            preserve_default=True,
        ),
    ]
