# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0028_franchcity_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='franchcity',
            name='area',
            field=models.CharField(max_length=50, null=True, verbose_name='\u043f\u043b\u043e\u0449\u0430\u0434\u044c'),
            preserve_default=True,
        ),
    ]
