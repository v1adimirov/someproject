# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0053_auto_20170814_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citymart',
            name='image',
        ),
    ]
