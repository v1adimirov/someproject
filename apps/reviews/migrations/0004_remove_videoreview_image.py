# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20151102_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoreview',
            name='image',
        ),
    ]
