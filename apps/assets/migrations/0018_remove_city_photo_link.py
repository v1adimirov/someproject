# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0017_camera'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='photo_link',
        ),
    ]
