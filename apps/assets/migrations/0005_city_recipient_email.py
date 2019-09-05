# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20151102_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='recipient_email',
            field=models.EmailField(max_length=255, verbose_name='email \u0434\u043b\u044f \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432', blank=True),
            preserve_default=True,
        ),
    ]
