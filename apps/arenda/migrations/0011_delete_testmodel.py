# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenda', '0010_testmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]
