# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0013_auto_20190523_0916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resume',
            options={'ordering': ['-id'], 'verbose_name': '\u0440\u0435\u0437\u044e\u043c\u0435', 'verbose_name_plural': '\u0440\u0435\u0437\u044e\u043c\u0435'},
        ),
        migrations.RemoveField(
            model_name='resume',
            name='created_at',
        ),
    ]
