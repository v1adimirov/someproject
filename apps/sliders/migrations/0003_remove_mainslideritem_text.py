# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sliders', '0002_auto_20151027_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainslideritem',
            name='text',
        ),
    ]
