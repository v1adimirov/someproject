# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0041_auto_20160614_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citymart',
            name='address',
        ),
        migrations.RemoveField(
            model_name='citymart',
            name='area',
        ),
    ]
