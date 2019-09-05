# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20151031_1645'),
        ('reviews', '0002_auto_20151102_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='city',
            field=models.ForeignKey(related_name='reviews', blank=True, to='assets.City', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videoreview',
            name='city',
            field=models.ForeignKey(related_name='videoreviews', blank=True, to='assets.City', null=True),
            preserve_default=True,
        ),
    ]
