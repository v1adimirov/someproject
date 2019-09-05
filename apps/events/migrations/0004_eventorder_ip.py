# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventorder_brend'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventorder',
            name='ip',
            field=models.CharField(max_length=50, null=True, verbose_name='IP', blank=True),
            preserve_default=True,
        ),
    ]
